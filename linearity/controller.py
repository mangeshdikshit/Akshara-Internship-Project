# controller.py

from .sum_of_sum import generate_questions as generate_sum_of_sum
from .Constant_multiples import generate_questions as generate_constant_multiple
from .Combining_linear_terms import generate_questions as generate_combining_terms
from .Application_in_double_and_triple_summations import generate_questions as generate_application_linearity

levels = [f"Level {i}" for i in range(1, 8)]

def generate_all_linearity_questions(level: str, total_questions: int):
    level_num = int(level.split()[-1])
    output_lines = []
    output_lines.append(f"# Linearity-Based Summation Questions for {level} (Total: {total_questions})\n")

    # Distribute questions equally (or as evenly as possible)
    base_count = total_questions // 4
    extras = total_questions % 4
    counts = [base_count + (1 if i < extras else 0) for i in range(4)]

    question_counter = 1

    # 1. Sum of a Sum
    output_lines.append("## 1. Sum of a Sum\n")
    questions = generate_sum_of_sum(level_num, counts[0])
    for q in questions:
        output_lines.append(f"**Q{question_counter}.** {q['question']}\n")
        output_lines.append(f"{q['answer']}\n")
        question_counter += 1

    # 2. Constant Multiple
    output_lines.append("\n## 2. Constant Multiple\n")
    questions = generate_constant_multiple(level_num, counts[1])
    for q in questions:
        output_lines.append(f"**Q{question_counter}.** {q['question']}\n")
        output_lines.append(f"{q['answer']}\n")
        question_counter += 1

    # 3. Combining Terms
    output_lines.append("\n## 3. Combining Terms\n")
    questions = generate_combining_terms(level_num, counts[2])
    for q in questions:
        output_lines.append(f"**Q{question_counter}.** {q['question']}\n")
        output_lines.append(f"{q['answer']}\n")
        question_counter += 1

    # 4. Application of Linearity (Nested)
    output_lines.append("\n## 4. Application of Linearity (Nested)\n")
    questions = generate_application_linearity(level_num, counts[3])
    for q in questions:
        output_lines.append(f"**Q{question_counter}.** {q['question']}\n")
        output_lines.append(f"{q['answer']}\n")
        question_counter += 1

    return output_lines

def run_topic_main():
    print("Available Levels:")
    for i, lvl in enumerate(levels, 1):
        print(f"{i}. {lvl}")

    while True:
        try:
            choice = int(input("\nEnter the number corresponding to the level: "))
            if 1 <= choice <= len(levels):
                selected_level = levels[choice - 1]
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            total_questions = int(input("Enter total number of questions: "))
            if total_questions > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

    output_lines = generate_all_linearity_questions(selected_level, total_questions)
    return output_lines

if __name__ == "__main__":
    run_topic_main()
