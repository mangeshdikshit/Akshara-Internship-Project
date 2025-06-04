

from .Basic_comparison_test import generate as generate_comparison_p
from .Conditions_for_convergence import generate as generate_conv_general
from .Geometric_test import generate as generate_geom_conv_sum
from .pseries_test import generate as generate_p_series_specific
from .Understanding_convergence_vs_divergence import generate as generate_conv_basic # Fifth module

levels = [f"Level {i}" for i in range(1, 8)] # Levels 1 to 7

def generate_all_convergence_questions_controller(level_str: str, total_questions: int):
    """
    Generates a mixed set of convergence test questions for a given level.
    """
    try:
        level_num = int(level_str.split()[-1])
        if not (1 <= level_num <= 7):
            raise ValueError("Level number must be between 1 and 7.")
    except (IndexError, ValueError) as e:
        return [f"Error: Invalid level string provided: '{level_str}'. It should be like 'Level X' where X is 1-7. Details: {e}"]

    if total_questions <= 0:
        return ["Error: Total number of questions must be a positive integer."]

    output_lines = []
    output_lines.append(f"# Convergence Test Questions: {level_str} (Total: {total_questions})\n")

    # Define the sub-topic generators and their titles - using all 5 provided modules
    sub_topic_generators = [
        ("Comparison Test with p-Series", generate_comparison_p),
        ("General Convergence Tests (with Hints)", generate_conv_general),
        ("Geometric Series Convergence and Sum", generate_geom_conv_sum),
        ("Specific p-Series Test", generate_p_series_specific),
        ("Basic Convergence Tests (Mixed Types)", generate_conv_basic),
    ]

    num_sub_topics = len(sub_topic_generators) # This will be 5

    # Distribute questions as evenly as possible among the available sub-topics
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

    return output_lines

def run_topic_main():
    
    print("Available Levels for Convergence Tests:")
    for i, level_display_name in enumerate(levels, 1):
        print(f"{i}. {level_display_name}")
    
    level_choice_str = input(f"Enter the number for the desired level (1-{len(levels)}): ").strip()
    selected_level_str = ""
    try:
        level_choice_int = int(level_choice_str)
        if 1 <= level_choice_int <= len(levels):
            selected_level_str = levels[level_choice_int - 1]
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
    
    return generate_all_convergence_questions_controller(selected_level_str, total_questions)

