
from .sum_of_sum import generate_questions as generate_sum_of_sum
from .Constant_multiples import generate_questions as generate_constant_multiple
from .Combining_linear_terms import generate_questions as generate_combining_terms
from .Application_in_double_and_triple_summations import generate_questions as generate_application_linearity

levels = [f"Level {i}" for i in range(1, 8)] # Levels 1 to 7

def generate_all_linearity_questions_controller(level_str: str, total_questions: int): # Renamed for clarity
   
    try:
        # Validate level_str format and extract level_num
        parts = level_str.split()
        if len(parts) != 2 or parts[0] != "Level":
            raise ValueError("Level string format is incorrect.")
        level_num_from_str = int(parts[-1]) 
        if not (1 <= level_num_from_str <= 7): # Assuming your sub-modules support levels 1-7
            raise ValueError("Level number out of supported range (1-7).")
    except (IndexError, ValueError) as e:
        
        return [f"Error: Invalid level string provided: '{level_str}'. It should be like 'Level X' where X is 1-7. Details: {e}"]

    if total_questions <= 0:
        return ["Error: Total number of questions must be a positive integer."]

    output_lines = []
    output_lines.append(f"# Linearity-Based Summation Questions: {level_str} (Total: {total_questions})\n")

   
    sub_topic_generators = [
        ("Sum of a Sum", generate_sum_of_sum),
        ("Constant Multiple Property", generate_constant_multiple),
        ("Combining Linear Terms in Summation", generate_combining_terms),
        ("Application of Linearity in Nested Summations", generate_application_linearity),
    ]

    num_sub_topics = len(sub_topic_generators) # Should be 4

    # Distribute questions as evenly as possible
    base_count = total_questions // num_sub_topics
    extras = total_questions % num_sub_topics
    counts = [base_count + (1 if i < extras else 0) for i in range(num_sub_topics)]

    question_counter = 1

    for i, (title, generator_func) in enumerate(sub_topic_generators):
        num_q_for_this_module = counts[i]
        if num_q_for_this_module == 0: # Skip if no questions allocated
            continue

        output_lines.append(f"\n## {i+1}. {title}\n")
        
        try:
            
            questions_data = generator_func(level_num_from_str, num_q_for_this_module)
            
            if not isinstance(questions_data, list):
                output_lines.append(f"Error: Generator for '{title}' did not return a list.\n")
                continue 
                
            for q_data in questions_data:
                if not isinstance(q_data, dict) or 'question' not in q_data or 'answer' not in q_data:
                    output_lines.append(f"Warning: Invalid question data format from '{title}'. Skipping this question.\n")
                    continue 
                output_lines.append(f"**Q{question_counter}.** {q_data['question']}\n")
                output_lines.append(f"{q_data['answer']}\n") # Original was just {q['answer']}
                question_counter += 1
        except Exception as e:
            output_lines.append(f"Error generating questions for '{title}' (Level {level_num_from_str}): {e}\n")
            
    
    if question_counter == 1 and total_questions > 0:
         output_lines.append("\nWarning: No questions were allocated to any sub-topic. This might be due to a very small total_questions value.\n")

    return output_lines

def run_topic_main():
   
    print("Available Levels for Linearity-Based Summation Questions:")
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
            # Return error as a list of strings
            return [f"Error: Invalid level choice. Please enter a number between 1 and {len(levels)}."]
    except ValueError:
        return [f"Error: Invalid input for level choice. Please enter a number."]

    try:
        total_questions = int(input("Enter the total number of questions: ").strip())
        if total_questions <= 0:
            return ["Error: Number of questions must be a positive integer."]
    except ValueError:
        return ["Error: Invalid input for number of questions. Please enter an integer."]
    
   
    return generate_all_linearity_questions_controller(selected_level_str_output, total_questions)

