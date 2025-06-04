import random


from .approximating_sums import get_partial_sums_questions
from .common_infinite_series import get_convergent_series_questions
from .convergent_geometric_series import generate_geometric_series
from .use_of_convergence_tests import generate_convergence_tests

levels = [f"Level {i}" for i in range(1, 8)] # Levels 1 to 7

def generate_all_mixed_questions(level_str: str, total_questions: int):
    """
    Generates a mixed set of questions from different series topics for a given level.
    """
    try:
        level_num = int(level_str.split()[-1])
        if not (1 <= level_num <= 7):
            raise ValueError("Level number must be between 1 and 7.")
    except (IndexError, ValueError) as e:
        return [f"Error: Invalid level string provided: {level_str}. {e}"]

    if total_questions <= 0:
        return ["Error: Total number of questions must be positive."]

    output_lines = []
    output_lines.append(f"# Mixed Series Questions: {level_str} (Total: {total_questions})\n")

    # Define the sub-topic generators and their titles
    # Each generator function should accept (level_num, num_q_for_this_module)
    # and return a list of {'question': str, 'answer': str}
    sub_topic_generators = [
        ("Approximating Sums Using Partial Sums", get_partial_sums_questions),
        ("Evaluating Convergent Geometric and Harmonic Series", get_convergent_series_questions),
        ("Advanced Geometric Series Evaluation", generate_geometric_series),
        ("Basic Convergence Tests", generate_convergence_tests),
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
                continue
                
            for q_data in questions_data:
                if not isinstance(q_data, dict) or 'question' not in q_data or 'answer' not in q_data:
                    output_lines.append(f"Warning: Invalid question data format from '{title}'.\n")
                    continue
                output_lines.append(f"**Q{question_counter}.** {q_data['question']}\n")
                output_lines.append(f"{q_data['answer']}\n") # Assuming answer includes "Answer:" prefix
                question_counter += 1
        except Exception as e:
            output_lines.append(f"Error generating questions for '{title}': {e}\n")

    return output_lines

def run_topic_main():
    
    # print("Welcome to the Series Question Generator!")
    # print("This tool will generate questions from various series topics.\n")
    print("Available Levels:")
    for i, lvl_str in enumerate(levels, 1):
        print(f"{i}. {lvl_str}")

    while True:
        try:
            choice = int(input(f"\nEnter the number corresponding to the desired level (1-{len(levels)}): "))
            if 1 <= choice <= len(levels):
                selected_level_str = levels[choice - 1]
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(levels)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            total_questions_desired = int(input("Enter the total number of questions you want: "))
            if total_questions_desired > 0:
                break
            else:
                print("Please enter a positive number for the total questions.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"\nGenerating {total_questions_desired} questions for {selected_level_str}...")
    
    generated_output_lines = generate_all_mixed_questions(selected_level_str, total_questions_desired)
    
    return generated_output_lines