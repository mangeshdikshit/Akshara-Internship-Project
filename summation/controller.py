

from .eval import generate_summation_question, evaluate_summation
from .index_shifting import generate_index_shifting_question

levels = [f"Level {i}" for i in range(1, 8)] # Levels 1 to 7

def generate_questions_controller(level_str: str, total_questions: int): # Renamed for clarity
    """
    Generates a mixed set of questions on direct summation evaluation and index shifting.
    """
    try:
        
        parts = level_str.split()
        if len(parts) != 2 or parts[0] != "Level":
            raise ValueError("Level string format is incorrect.")
        level_num_from_str = int(parts[-1]) # Use this if your sub-modules expect an int level
        if not (1 <= level_num_from_str <= 7): # Or however many levels your sub-modules support
            raise ValueError("Level number out of supported range (1-7).")
    except (IndexError, ValueError) as e:
        return [f"Error: Invalid level string provided: '{level_str}'. It should be like 'Level X' where X is 1-7. Details: {e}"]

    if total_questions <= 0:
        return ["Error: Total number of questions must be a positive integer."]

    output_lines = []
    output_lines.append(f"# Combined Summation Questions: {level_str} (Total: {total_questions})\n")

   

    num_sub_topics = 2 # Direct Evaluation and Index Shifting

    # Distribute questions as evenly as possible
    base_count = total_questions // num_sub_topics
    extras = total_questions % num_sub_topics
    
    # counts[0] for Direct Evaluation, counts[1] for Index Shifting
    counts = [base_count, base_count] 
    if extras > 0:
        counts[0] += 1 # Give extra to the first category, or distribute as preferred
        if extras > 1: # if more than 2 topics and more extras
            counts[1] +=1


    question_counter = 1

    # 1. Direct Evaluation
    if counts[0] > 0:
        output_lines.append(f"\n## 1. Direct Evaluation Questions ({level_str})\n")
        try:
            for _ in range(counts[0]):
                
                question, answer_fn = generate_summation_question(level_str) # Or level_num_from_str
                answer = evaluate_summation(answer_fn)
                output_lines.append(f"**Q{question_counter}.** {question}\n")
                output_lines.append(f"**Answer:** {answer}\n") # Original answer format was just {answer}
                question_counter += 1
        except Exception as e:
            output_lines.append(f"Error generating Direct Evaluation questions for {level_str}: {e}\n")

    # 2. Index Shifting
    if counts[1] > 0:
        output_lines.append(f"\n## 2. Index Shifting Questions ({level_str})\n")
        try:
            for _ in range(counts[1]):
                # Pass level_str or level_num_from_str
                question, answer = generate_index_shifting_question(level_str) # Or level_num_from_str
                output_lines.append(f"**Q{question_counter}.** {question}\n")
                output_lines.append(f"**Answer:** `{answer}`\n") # Original was `answer`
                question_counter += 1
        except Exception as e:
            output_lines.append(f"Error generating Index Shifting questions for {level_str}: {e}\n")
            
    # If no questions were generated at all due to counts being zero for all.
    if question_counter == 1 and total_questions > 0:
         output_lines.append("\nWarning: No questions were allocated to any sub-topic. This might be due to a very small total_questions value.\n")


    return output_lines

def run_topic_main():
    
    print("Available Levels for Combined Summation Questions:")
    for i, level_display_name in enumerate(levels, 1):
        # Presenting a numeric choice that maps to the string
        print(f"{i}. {level_display_name}")
    
    level_choice_str_input = input(f"Enter the number for the desired level (1-{len(levels)}): ").strip()
    selected_level_str_output = "" # This will hold "Level X"
    
    try:
        level_choice_int = int(level_choice_str_input)
        if 1 <= level_choice_int <= len(levels):
            selected_level_str_output = levels[level_choice_int - 1] # Get "Level X" string
        else:
            return [f"Error: Invalid level choice. Please enter a number between 1 and {len(levels)}."]
    except ValueError:
        return [f"Error: Invalid input for level choice. Please enter a number."]

    try:
        total_questions = int(input("Enter the total number of questions: ").strip())
        if total_questions <= 0:
            return ["Error: Number of questions must be a positive integer."]
    except ValueError:
        return ["Error: Invalid input for number of questions. Please enter an integer."]
    
    # Call the main generation function with the "Level X" string
    return generate_questions_controller(selected_level_str_output, total_questions)

