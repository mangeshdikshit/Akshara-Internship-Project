import random
from sympy import symbols, Sum, Limit, sin, cos, log, simplify, oo, latex
from sympy.abc import i

# Define divergent series expressions per level
LEVELS = {
    1: {'expressions': [1, 1 / i]},  # Basic p-series and constants
    2: {'expressions': [log(i), (i + 1) / i]},  # Logarithmic and rational expressions
    3: {'expressions': [1 / (i**0.5), (1 + 1/i)**i]},  # p-series with p <= 1, exponential behavior
    4: {'expressions': [i]},  # Linear growth
    5: {'expressions': [i**2]},  # Quadratic growth
    6: {'expressions': [2**i]},  # Exponential growth
    7: {'expressions': [sin(i), cos(i)]},  # Oscillatory non-converging expressions
}

# Templates for questions
TEMPLATES = [
    "Determine whether the following infinite series converges to a finite value:",
    "Does the series below have a finite sum?",
    "Analyze the convergence behavior of the given infinite series:",
    "State whether the following series converges or diverges:",
    "Examine if the series below converges or diverges:",
    "Consider the following series. Does it converge or diverge?",
    "Investigate the convergence of the following series:"
]

def generate_question(level):
    expr = random.choice(LEVELS[level]['expressions'])
    series = Sum(expr, (i, 1, oo))

    # Compute the limit of general term (if possible)
    try:
        limit_expr = Limit(expr, i, oo).doit()
    except:
        limit_expr = "undefined"

    # Decide reasoning
    if isinstance(limit_expr, str) or limit_expr != 0:
        result = "The series does not converge to a finite sum."
    else:
        result = "Although the general term approaches 0, the series still diverges due to insufficient decay."

    # Format question and answer
    question_text = random.choice(TEMPLATES) + "\n\n"
    question_text += "$\n" + latex(series) + "\n$"

    answer_text = "**Answer:**\n\n"
    answer_text += f"General term: $a_i = {latex(expr)}$\n\n"
    if not isinstance(limit_expr, str):
        answer_text += f"Limit of general term: $\\lim_{{i \\to \\infty}} a_i = {latex(limit_expr)}$\n\n"
    answer_text += result

    return {
        "question": question_text,
        "answer": answer_text,
        "level": level
    }

def generate_divergent_series_questions(level, num_questions):
    qa_list = []
    for _ in range(num_questions):
        qa = generate_question(level)
        qa_list.append(qa)
    return qa_list

