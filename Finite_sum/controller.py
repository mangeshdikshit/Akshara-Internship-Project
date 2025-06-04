# controller.py for Finite Sum Topics

import math

from .General_polynomial_sum_forms import generate_general_poly_sums
from .Piecewise_defined_summand import generate_questions as generate_piecewise
from .Sum_of_first_n_natural_numbers import generate_question_answer_string as generate_first_n_natural
from .Sum_of_squares_and_cubes import generate_questions as generate_squares_cubes
from .Sums_with_custom_bounds import generate_questions as generate_custom_bounds

topics = [
    ("General Polynomial Sum Forms", generate_general_poly_sums),
    ("Piecewise Defined Summand", generate_piecewise),
    ("Sum of First n Natural Numbers", generate_first_n_natural),
    ("Sum of Squares and Cubes", generate_squares_cubes),
    ("Sums with Custom Bounds", generate_custom_bounds),
]

levels = [f"Level {i}" for i in range(1, 8)]

def run_topic_main():
    print("Available Levels:")
    for i, lvl in enumerate(levels, 1):
        print(f"{i}. {lvl}")

    while True:
        try:
            choice = int(input("\nEnter the number corresponding to the level: "))
            if 1 <= choice <= len(levels):
                level = choice
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

    # Divide questions as evenly as possible
    base = total_questions // 5
    extras = total_questions % 5
    counts = [base + (1 if i < extras else 0) for i in range(5)]

    output_lines = [f"# Finite Sum Questions for {selected_level} (Total: {total_questions})\n"]

    question_counter = 1

    for idx, (topic_name, generator) in enumerate(topics):
        count = counts[idx]
        if count == 0:
            continue

        output_lines.append(f"\n## {idx+1}. {topic_name}\n")

        if topic_name == "General Polynomial Sum Forms":
            section = generator(level, count)
            output_lines.append(section)

        elif topic_name == "Piecewise Defined Summand":
            questions = generator(level, count)
            for qa in questions:
                output_lines.append(f"**Q{question_counter}.** {qa['question']}\n")
                output_lines.append(f"{qa['answer']}\n")
                question_counter += 1

        elif topic_name == "Sum of First n Natural Numbers":
            section = generator(level, count)
            output_lines.append(section)

        elif topic_name == "Sum of Squares and Cubes":
            section = generator(level, count)
            output_lines.append(section)

        elif topic_name == "Sums with Custom Bounds":
            questions = generator(level, count)
            for qa in questions:
                question_counter = 1
                output_lines.append(f"**Q{question_counter}.** {qa['question']}\n")
                output_lines.append(f"{qa['answer']}\n")
                question_counter += 1

    return output_lines

if __name__ == "__main__":
    lines = run_topic_main()
    print("\n".join(lines))
