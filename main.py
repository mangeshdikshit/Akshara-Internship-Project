import os
import importlib


topics = {
    "1": ("Summation", "summation.controller"),
    "2": ("Summation_Properties", "Summation_Properties.controller"),
    "3": ("linearity", "linearity.controller"),
    "4": ("Finite_sum", "Finite_sum.controller"),
    "5": ("Infinite_sum", "Infinite_sum.controller"),
    "6": ("Arithmetic_Series", "Arithmetic_Series.controller"),
    "7": ("Geometric_Series", "Geometric_Series.controller"),
    "8": ("Convergence_of_Series", "Convergence_of_Series.controller"),
    "9": ("Divergence_of_Series", "Divergence_of_Series.controller"),
    "10": ("Fourier_series", "Fourier_series.controller"),
    # Add more topics if needed
}

def main():
    with open("output.md", "w", encoding="utf-8"):
        pass

    print("Available Topics:")
    for key, (name, _) in topics.items():
        print(f"{key}. {name}")

    while True:
        choice = input("\nEnter the topic number: ").strip()
        if choice in topics:
            topic_name, module_path = topics[choice]
            break
        else:
            print("Invalid choice. Try again.")

    module = importlib.import_module(module_path)
    output_lines = module.run_topic_main()

    # Write to markdown file
    with open("output.md", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))


    print(f"\n [OK] Output written to output.md for topic: {topic_name}")

if __name__ == "__main__":
    main()
