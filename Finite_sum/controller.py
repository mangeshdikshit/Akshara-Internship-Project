

import math 

from .General_polynomial_sum_forms import generate_general_poly_sums
from .Piecewise_defined_summand import generate_questions as generate_piecewise
from .Sum_of_first_n_natural_numbers import generate_question_answer_string as generate_first_n_natural
from .Sum_of_squares_and_cubes import generate_questions as generate_squares_cubes
from .Sums_with_custom_bounds import generate_questions as generate_custom_bounds

topics = [ # This list defines the order and generators
    ("General Polynomial Sum Forms", generate_general_poly_sums),
    ("Piecewise Defined Summand", generate_piecewise),
    ("Sum of First n Natural Numbers", generate_first_n_natural),
    ("Sum of Squares and Cubes", generate_squares_cubes),
    ("Sums with Custom Bounds", generate_custom_bounds),
]

levels = [f"Level {i}" for i in range(1, 8)] # Levels 1 to 7

def generate_all_finite_sum_questions_controller(level_str: str, total_questions: int):
    
    try:
        parts = level_str.split()
        if len(parts) != 2 or parts[0] != "Level":
            raise ValueError("Level string format is incorrect.")
        level_num_from_str = int(parts[-1]) 
        if not (1 <= level_num_from_str <= 7):
            raise ValueError("Level number out of supported range (1-7).")
    except (IndexError, ValueError) as e:
        return [f"Error: Invalid level string provided: '{level_str}'. It should be like 'Level X' where X is 1-7. Details: {e}"]

    if total_questions <= 0:
        return ["Error: Total number of questions must be a positive integer."]

    output_lines = []
    output_lines.append(f"# Finite Sum Questions: {level_str} (Total: {total_questions})\n")

    num_sub_topics = len(topics) # Should be 5

    base_count = total_questions // num_sub_topics
    extras = total_questions % num_sub_topics
    counts = [base_count + (1 if i < extras else 0) for i in range(num_sub_topics)]

    question_counter = 1 # Global question counter

    for idx, (topic_name, generator_func) in enumerate(topics):
        num_q_for_this_module = counts[idx]
        if num_q_for_this_module == 0:
            continue

        output_lines.append(f"\n## {idx+1}. {topic_name}\n")

        try:
            
            if topic_name in ["General Polynomial Sum Forms", 
                              "Sum of First n Natural Numbers", 
                              "Sum of Squares and Cubes"]:
                
                section_string = generator_func(level_num_from_str, num_q_for_this_module)
                if isinstance(section_string, str):
                    output_lines.append(section_string)
                    
                else:
                    output_lines.append(f"Error: Generator for '{topic_name}' did not return a string as expected.\n")

            elif topic_name in ["Piecewise Defined Summand", "Sums with Custom Bounds"]:
               
                questions_data = generator_func(level_num_from_str, num_q_for_this_module)
                if not isinstance(questions_data, list):
                    output_lines.append(f"Error: Generator for '{topic_name}' did not return a list.\n")
                    continue
                
                
                if topic_name == "Sums with Custom Bounds":  
                    pass 


                for q_data in questions_data:
                    if not isinstance(q_data, dict) or 'question' not in q_data or 'answer' not in q_data:
                        output_lines.append(f"Warning: Invalid question data format from '{topic_name}'. Skipping this question.\n")
                        continue
                    
                    output_lines.append(f"**Q{question_counter}.** {q_data['question']}\n")
                    output_lines.append(f"{q_data['answer']}\n")
                    question_counter += 1
            else:
                output_lines.append(f"Warning: Unknown topic '{topic_name}' encountered in configuration.\n")

        except Exception as e:
            output_lines.append(f"Error generating questions for '{topic_name}' (Level {level_num_from_str}): {e}\n")
    
    if question_counter == 1 and total_questions > 0 and not any("Error:" in line for line in output_lines if "##" not in line):
         output_lines.append("\nWarning: No questions were allocated or generated successfully for any sub-topic. This might be due to a very small total_questions value or issues with all generators.\n")


    return output_lines

def run_topic_main():
    
    print("Available Levels for Finite Sum Questions:")
    for i, level_display_name in enumerate(levels, 1):
        print(f"{i}. {level_display_name}")
    
    level_choice_str_input = input(f"Enter the number for the desired level (1-{len(levels)}): ").strip()
    selected_level_str_output = "" 
    
    try:
        level_choice_int = int(level_choice_str_input)
        if 1 <= level_choice_int <= len(levels):
            selected_level_str_output = levels[level_choice_int - 1]
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
    
    return generate_all_finite_sum_questions_controller(selected_level_str_output, total_questions)

