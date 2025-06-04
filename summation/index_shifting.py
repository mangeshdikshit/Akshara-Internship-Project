from IPython.display import Markdown
import random
import fractions
from sympy import symbols, latex, Rational

def generate_fraction(min_value, max_value):
    numerator = random.randint(min_value, max_value)
    denominator = random.randint(1, max_value)
    return Rational(numerator, denominator)

def generate_index_shifting_question(level):
    if level not in [f"Level {i}" for i in range(1, 8)]:
        raise ValueError(f"Invalid level: {level}. Expected Level 1 to Level 7.")
    
    i, j, k, l = symbols('i j k l')

    if level == "Level 1":
        i_start = random.randint(1, 10)
        i_end = i_start + random.randint(1, 3)
        shift_value = i_start - 1
        j_end = i_end - i_start + 1

        question = f"Rewrite the summation \n\n $\\sum_{{i={i_start}}}^{{{i_end}}} {latex(i)}$ \n\n in terms of an index j starting from 1, in the form \n\n $\\sum_{{j=1}}^{{{j_end}}} ({latex(j)} + c)$.\n\n Find c."
        answer = str(shift_value)
        return question, answer

    elif level == "Level 2":
        i_start = random.randint(-10, 10)
        i_end = i_start + random.randint(1, 3)
        shift_value = i_start - 1
        j_end = i_end - i_start + 1

        question = f"Transform the summation \n\n $\\sum_{{i={i_start}}}^{{{i_end}}} {latex(i)}$ \n\n using index shifting to start from j = 1, in the form \n\n $\\sum_{{j=1}}^{{{j_end}}} ({latex(j)} + c)$. \n\n Find c."
        answer = str(shift_value)
        return question, answer

    elif level == "Level 3":
        i_start = random.choice([random.randint(-5, 5), generate_fraction(-5, 5)])
        i_end = i_start + random.choice([random.randint(1, 3), generate_fraction(1, 3)])
        shift_value = i_start - 1
        j_end = i_end - i_start + 1

        question = f"Convert the summation \n\n $\\sum_{{i={latex(i_start)}}}^{{{latex(i_end)}}} {latex(i)}$ \n\n into \n\n $\\sum_{{j=1}}^{{{latex(j_end)}}} ({latex(j)} + c)$. \n\n Find c."
        answer = str(shift_value)
        return question, answer

    elif level == "Level 4":
        i_start = random.randint(1, 5)
        i_end = i_start + random.randint(1, 3)
        j_start = random.randint(1, 5)
        j_end = j_start + random.randint(1, 3)
        si, sj = i_start - 1, j_start - 1
        k_end = i_end - i_start + 1
        j_new_end = j_end - j_start + 1

        question = f"Rewrite the double summation \n\n $\\sum_{{j={j_start}}}^{{{j_end}}} \\sum_{{i={i_start}}}^{{{i_end}}} {latex(i*j)} $ \n\n using new indices k, j starting from 1, in the form \n\n $\\sum_{{j=1}}^{{{j_new_end}}} \\sum_{{k=1}}^{{{k_end}}} ({latex(k)} + c_1)({latex(j)} + c_2)$. \n\n Find (c_1, c_2)."
        answer = f"({si}, {sj})"
        return question, answer

    elif level == "Level 5":
        i_start = random.randint(-5, 5)
        i_end = i_start + random.randint(1, 3)
        j_start = random.randint(-5, 5)
        j_end = j_start + random.randint(1, 3)
        si, sj = i_start - 1, j_start - 1
        k_end = i_end - i_start + 1
        j_new_end = j_end - j_start + 1

        question = f"Shift the indices of the double summation \n\n $\\sum_{{j={j_start}}}^{{{j_end}}} \\sum_{{i={i_start}}}^{{{i_end}}} {latex(i*j)}$ \n\n so both summations start from 1, in the form \n\n $\\sum_{{j=1}}^{{{j_new_end}}} \\sum_{{k=1}}^{{{k_end}}} ({latex(k)} + c_1)({latex(j)} + c_2)$. \n\n Find (c_1, c_2)."
        answer = f"({si}, {sj})"
        return question, answer

    elif level == "Level 6":
        i_start = random.choice([random.randint(-3, 3), generate_fraction(-3, 3)])
        i_end = i_start + random.choice([random.randint(1, 3), generate_fraction(1, 3)])
        j_start = random.choice([random.randint(-3, 3), generate_fraction(-3, 3)])
        j_end = j_start + random.choice([random.randint(1, 3), generate_fraction(1, 3)])
        si, sj = i_start - 1, j_start - 1
        k_end = i_end - i_start + 1
        j_new_end = j_end - j_start + 1

        question = f"Using index shifting, rewrite \n\n $\\sum_{{j={latex(j_start)}}}^{{{latex(j_end)}}} \\sum_{{i={latex(i_start)}}}^{{{latex(i_end)}}} {latex(i*j)}$ \n\n so both summations start from 1, in the form \n\n $\\sum_{{j=1}}^{{{latex(j_new_end)}}} \\sum_{{k=1}}^{{{latex(k_end)}}} ({latex(k)} + c_1)({latex(j)} + c_2)$. \n\n Find (c_1, c_2)."
        answer = f"({si}, {sj})"
        return question, answer

    elif level == "Level 7":
        i_start = random.choice([random.randint(-3, 3), generate_fraction(-3, 3)])
        i_end = i_start + random.choice([random.randint(1, 3), generate_fraction(1, 3)])
        j_start = random.choice([random.randint(-3, 3), generate_fraction(-3, 3)])
        j_end = j_start + random.choice([random.randint(1, 3), generate_fraction(1, 3)])
        k_start = random.choice([random.randint(-3, 3), generate_fraction(-3, 3)])
        k_end = k_start + random.choice([random.randint(1, 3), generate_fraction(1, 3)])
        si, sj, sk = i_start - 1, j_start - 1, k_start - 1
        l_end = k_end - k_start + 1
        j_new_end = j_end - j_start + 1
        k_new_end = i_end - i_start + 1

        question = f"Using index shifting, rewrite \n\n $\\sum_{{k={latex(k_start)}}}^{{{latex(k_end)}}} \\sum_{{j={latex(j_start)}}}^{{{latex(j_end)}}} \\sum_{{i={latex(i_start)}}}^{{{latex(i_end)}}} {latex(i*j*k)} $ \n\n so all summations start from 1, in the form \n\n $\\sum_{{j=1}}^{{{latex(j_new_end)}}} \\sum_{{k=1}}^{{{latex(k_new_end)}}} \\sum_{{l=1}}^{{{latex(l_end)}}} ({latex(k)} + c_1)({latex(j)} + c_2)({latex(l)} + c_3)$. \n\n Find (c_1, c_2, c_3)."
        answer = f"({si}, {sj}, {sk})"
        return question, answer

def generate_questions(level, count):
    results = []
    for _ in range(count):
        question, answer = generate_index_shifting_question(level)
        results.append(f"{question}\n\n**Answer:** {answer}\n---\n")
    return results
