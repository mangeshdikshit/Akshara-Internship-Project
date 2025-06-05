import random
from sympy import symbols, Limit, Sum, sin, cos, tan, exp, log, oo, latex
from sympy.abc import i

# Level-wise categorization of expressions for divergence testing
LEVELS = {
    1: {'expressions': [(1 + 1/i), (i / (i - 0.5))]},  # Clear non-zero limit → diverges
    2: {'expressions': [(i / (i + 1))]},              # Limit → 1 ≠ 0
    3: {'expressions': [(1 / (1 + sin(i)))]},         # Bounded away from 0
    4: {'expressions': [(sin(i)), (cos(i))]},         # Oscillating terms → test inconclusive
    5: {'expressions': [(i / (i**2 + 1))]},           # Limit = 0 → test inconclusive
    6: {'expressions': [(1 / (i + 1)), (log(i) / i)]},# Limit = 0 → test inconclusive
    7: {'expressions': [(exp(-i)), (tan(1/i))]}       # Fast decay or complex behavior
}

# Question templates
TEMPLATES = [
    "Use the divergence test to determine whether the following series diverges:",
    "Apply the nth-term divergence test on the following series:",
    "Does the series diverge by the test for divergence?",
    "Determine the behavior of the series using the divergence test:",
    "Test for divergence using the limit of the general term:",
    "Analyze convergence using the divergence (term) test:",
    "What does the divergence test tell us about the following series?"
]

def generate_question(level):
    expr = random.choice(LEVELS[level]['expressions'])
    series = Sum(expr, (i, 1, oo))

    try:
        limit_expr = Limit(expr, i, oo).doit()
    except:
        limit_expr = "undefined"

    # Apply divergence test logic
    if isinstance(limit_expr, str):
        result = "The divergence test is inconclusive due to undefined limit behavior."
    elif limit_expr != 0:
        result = "The series diverges because the limit of the general term is not 0."
    elif limit_expr == 0:
        result = "The divergence test is inconclusive because the limit is 0."
    else:
        result = "The divergence test is inconclusive."

    # Format LaTeX question and answer
    question_text = random.choice(TEMPLATES) + "\n\n"
    question_text += "$\n" + latex(series) + "\n$"

    answer_text = "**Answer:**\n\n"
    answer_text += f"The limit of the general term is: $\\lim_{{i \\to \\infty}} {latex(expr)} = {latex(limit_expr)}$\n\n"
    answer_text += result

    return {
        "question": question_text,
        "answer": answer_text,
        "level": level
    }

def generate_divergence_test_questions(level, num_questions):
    qa_list = []
    for _ in range(num_questions):
        qa = generate_question(level)
        qa_list.append(qa)
    return qa_list

