

from .Finite_geometric_series_formula import generate as generate_finite_geometric
from .growth_models import generate as generate_growth_decay
from .Infinite_geometric_series import generate as generate_infinite_geometric
from .Recursive_relations import generate as generate_recursive_sum

levels = [f"Level {i}" for i in range(1, 8)] # Levels 1 to 7

def generate_all_geometric_questions_controller(level_str: str, total_questions: int):
    
    try:
        level_num = int(level_str.split()[-1])
        if not (1 <= level_num <= 7):
            raise ValueError("Level number must be between 1 and 7.")
    except (IndexError, ValueError) as e:
        # Return error message as a list of strings, consistent with question output format
        return [f"Error: Invalid level string provided: '{level_str}'. It should be like 'Level X' where X is 1-7. Details: {e}"]

    if total_questions <= 0:
        return ["Error: Total number of questions must be a positive integer."]

    output_lines = []
    output_lines.append(f"# Geometric Series Questions: {level_str} (Total: {total_questions})\n")

    # Define the sub-topic generators and their titles
    sub_topic_generators = [
        ("Finite Geometric Series Evaluation", generate_finite_geometric),
        ("Geometric Series in Growth/Decay Models", generate_growth_decay),
        ("Infinite Geometric Series Summation", generate_infinite_geometric),
        ("Sum of Recursive Geometric Sequences", generate_recursive_sum),
    ]

    num_sub_topics = len(sub_topic_generators)

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
            questions_data = generator_func(level_num, num_q_for_this_module)
            if not isinstance(questions_data, list):
                output_lines.append(f"Error: Generator for '{title}' did not return a list.\n")
                continue # Skip processing this sub-topic if the data format is incorrect
                
            for q_data in questions_data:
                if not isinstance(q_data, dict) or 'question' not in q_data or 'answer' not in q_data:
                    output_lines.append(f"Warning: Invalid question data format from '{title}'. Skipping this question.\n")
                    continue # Skip this particular malformed question data
                output_lines.append(f"**Q{question_counter}.** {q_data['question']}\n")
                # Assuming answer from modules includes formatting like "**Answer:** $$...$$"
                output_lines.append(f"{q_data['answer']}\n") 
                question_counter += 1
        except Exception as e:
            output_lines.append(f"Error generating questions for '{title}': {e}\n")

    return output_lines

def run_topic_main():
    """
    Entry point for generating geometric series questions.
    Prompts user for level and number of questions, then returns output lines.
    """
    print("Available Levels for Geometric Series:")
    for i, level_display_name in enumerate(levels, 1):
        # Presenting a numeric choice that maps to the string
        print(f"{i}. {level_display_name}")
    
    level_choice_str = input(f"Enter the number for the desired level (1-{len(levels)}): ").strip()
    selected_level_str = ""
    try:
        level_choice_int = int(level_choice_str)
        if 1 <= level_choice_int <= len(levels):
            selected_level_str = levels[level_choice_int - 1] # Get "Level X" string
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
    return generate_all_geometric_questions_controller(selected_level_str, total_questions)