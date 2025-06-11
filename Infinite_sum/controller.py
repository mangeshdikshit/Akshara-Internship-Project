import random 
from .approximating_sums import get_partial_sums_questions
from .common_infinite_series import get_convergent_series_questions
from .convergent_geometric_series import generate_geometric_series
from .use_of_convergence_tests import generate_convergence_tests

levels = [f"Level {i}" for i in range(1, 8)] # Levels 1 to 7

def generate_all_mixed_questions(level_str: str, total_questions: int):
    
    try:
        level_num = int(level_str.split()[-1])
        if not (1 <= level_num <= 7):
            raise ValueError("Level number must be between 1 and 7.")
    except (IndexError, ValueError) as e:
        return [f"Error: Invalid level string provided: '{level_str}'. It should be like 'Level X' where X is 1-7. Details: {e}"]

    if total_questions <= 0:
        return ["Error: Total number of questions must be a positive integer."] 

    output_lines = []
    output_lines.append(f"# Mixed Series Questions: {level_str} (Total: {total_questions})\n")

    sub_topic_generators = [
        ("Approximating Sums Using Partial Sums", get_partial_sums_questions),
        ("Evaluating Convergent Geometric and Harmonic Series", get_convergent_series_questions),
        ("Advanced Geometric Series Evaluation", generate_geometric_series),
        ("Basic Convergence Tests", generate_convergence_tests),
    ]

    num_sub_topics = len(sub_topic_generators)
    base_count = total_questions // num_sub_topics
    extras = total_questions % num_sub_topics
    counts = [base_count + (1 if i < extras else 0) for i in range(num_sub_topics)]
    question_counter = 1

    for i, (title, generator_func) in enumerate(sub_topic_generators):
        num_q_for_this_module = counts[i]
        if num_q_for_this_module == 0:
            continue

        output_lines.append(f"\n## {i+1}. {title}\n")
        
        try:
            questions_data = generator_func(level_num, num_q_for_this_module)
            if not isinstance(questions_data, list):
                output_lines.append(f"Error: Generator for '{title}' did not return a list.\n")
                continue
                
            for q_data in questions_data:
                if not isinstance(q_data, dict) or 'question' not in q_data or 'answer' not in q_data:
                    output_lines.append(f"Warning: Invalid question data format from '{title}'. Skipping this question.\n") 
                    continue
                output_lines.append(f"**Q{question_counter}.** {q_data['question']}\n")
                output_lines.append(f"{q_data['answer']}\n")
                question_counter += 1
        except Exception as e:
            output_lines.append(f"Error generating questions for '{title}': {e}\n")
            
    if question_counter == 1 and total_questions > 0 and not any("Error:" in line for line in output_lines if "##" not in line):
         output_lines.append("\nWarning: No questions were allocated or generated successfully for any sub-topic. This might be due to a very small total_questions value or issues with all generators.\n")

    return output_lines

def run_topic_main():
    
    print("Available Levels for Mixed Series Questions:") # Title change
    for i, level_display_name in enumerate(levels, 1):
        print(f"{i}. {level_display_name}")
    
    level_choice_str_input = input(f"Enter the number for the desired level (1-{len(levels)}): ").strip()
    selected_level_str = ""
    try:
        level_choice_int = int(level_choice_str_input)
        if 1 <= level_choice_int <= len(levels):
            selected_level_str = levels[level_choice_int - 1] # Get "Level X" string
        else:
            return [f"Error: Invalid level choice. Please enter a number between 1 and {len(levels)}."]
    except ValueError:
        # Return error list, like the reference controller
        return [f"Error: Invalid input for level choice. Please enter a number."]

    try:
        total_questions_desired = int(input("Enter the total number of questions you want: ").strip())
        if total_questions_desired <= 0:
            # Return error list, like the reference controller
            return ["Error: Number of questions must be a positive integer."] # Message made consistent
    except ValueError:
        # Return error list, like the reference controller
        return ["Error: Invalid input for number of questions. Please enter an integer."] # Message made consistent
    
   
    print(f"\nGenerating {total_questions_desired} questions for {selected_level_str}...") 
    
    return generate_all_mixed_questions(selected_level_str, total_questions_desired)

