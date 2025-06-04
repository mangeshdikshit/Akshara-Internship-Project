from .Finding_number_of_terms import generate as generate_find_n
from .Finding_sum_given_terms import generate as generate_sum_given_terms
from .Formula_of_Arithmetic_Series import generate as generate_evaluate_sigma
from .Reallife_applications import generate as generate_real_life_payment

levels = [f"Level {i}" for i in range(1, 8)] # Levels 1 to 7

def generate_all_arithmetic_questions(level_str: str, total_questions: int):
    
    try:
        level_num = int(level_str.split()[-1])
        if not (1 <= level_num <= 7):
            raise ValueError("Level number must be between 1 and 7.")
    except (IndexError, ValueError) as e:
        return [f"Error: Invalid level string provided: {level_str}. {e}"]

    if total_questions <= 0:
        return ["Error: Total number of questions must be positive."]

    output_lines = []
    output_lines.append(f"# Arithmetic Series Questions: {level_str} (Total: {total_questions})\n")

    sub_topic_generators = [
        ("Finding the Number of Terms (n)", generate_find_n),
        ("Sum Given First Term, Difference, and Number of Terms", generate_sum_given_terms),
        ("Evaluating Arithmetic Series in Sigma Notation", generate_evaluate_sigma),
        ("Real-Life Applications of Arithmetic Series (Payments)", generate_real_life_payment),
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
                # To maintain consistent output structure (list of strings), add the error as a line.
                # And potentially skip adding more questions from this generator if the format is wrong.
                continue # Skip processing if the data format is incorrect
                
            for q_data in questions_data:
                if not isinstance(q_data, dict) or 'question' not in q_data or 'answer' not in q_data:
                    output_lines.append(f"Warning: Invalid question data format from '{title}'. Skipping this question.\n")
                    continue # Skip this particular malformed question data
                output_lines.append(f"**Q{question_counter}.** {q_data['question']}\n")
                output_lines.append(f"{q_data['answer']}\n") # Assuming answer includes "Answer:" prefix
                question_counter += 1
        except Exception as e:
            output_lines.append(f"Error generating questions for '{title}': {e}\n")

    return output_lines

def run_topic_main():
    """
    Entry point for main.py to generate arithmetic series questions.
    Prompts user for level and number of questions, then returns output lines.
    """
    print("Available Levels:")
    for level in levels:
        print(level)
    level_str = input("Enter the level (e.g., 'Level 1'): ").strip()
    try:
        total_questions = int(input("Enter the total number of questions: ").strip())
    except ValueError:
        return ["Error: Invalid number of questions."]
    return generate_all_arithmetic_questions(level_str, total_questions)