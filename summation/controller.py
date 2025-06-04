from .eval import generate_summation_question, evaluate_summation
from .index_shifting import generate_index_shifting_question

levels = [f"Level {i}" for i in range(1, 8)]

def generate_questions(level: str, total_questions: int):
    output_lines = []
    output_lines.append(f"# Combined Summation Questions for {level} (Total: {total_questions})\n")

    half = total_questions // 2
    remaining = total_questions - half

    # Direct Evaluation
    output_lines.append(f"## Direct Evaluation Questions ({level})\n")
    for i in range(half):
        question, answer_fn = generate_summation_question(level)
        answer = evaluate_summation(answer_fn)
        output_lines.append(f"**Q{i+1}.** {question}\n")
        output_lines.append(f"**Answer:** {answer}\n")

    # Index Shifting
    output_lines.append(f"\n## Index Shifting Questions ({level})\n")
    for i in range(remaining):
        question, answer = generate_index_shifting_question(level)
        output_lines.append(f"**Q{i+1+half}.** {question}\n")
        output_lines.append(f"**Answer:** `{answer}`\n")

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

    return generate_questions(selected_level, total_questions)
