import random
from sympy import symbols, Sum, latex, oo, simplify
from sympy.abc import i

# Levels (to vary p and formats slightly)
LEVELS = {
    1: {'p_range': [0.2, 0.5]},
    2: {'p_range': [0.6, 0.9]},
    3: {'p_range': [1.0, 1.0]},
    4: {'p_range': [0.1, 0.9]},
    5: {'p_range': [0.3, 1.0]},
    6: {'p_range': [0.5, 1.0]},
    7: {'p_range': [0.8, 1.0]}
}

QUESTION_TEMPLATES = [
    "Determine whether the following p-series converges or diverges:",
    "Is the infinite series shown below convergent or divergent?",
    "Analyze the behavior of the following series:",
    "Does this p-series converge or diverge? Justify your answer.",
    "Evaluate the convergence status of the given p-series:",
    "Classify the following series as convergent or divergent:",
    "Using your knowledge of p-series, determine the behavior of this series:",
    "Apply the p-series test to check if the following sum converges or diverges:"
]

def generate_divergent_p_series(level):
    p_min, p_max = LEVELS[level]['p_range']
    p_val = round(random.uniform(p_min, p_max), 3)
    expr = 1 / (i ** p_val)
    summation = Sum(expr, (i, 1, oo))

    # Explanation
    if p_val == 1.0:
        reason = "This is the harmonic series (p = 1), which diverges."
    else:
        reason = f"This is a p-series with p = {p_val} ≤ 1, so it diverges."

    return summation, reason, level

def generate_question(level):
    summation, explanation, lvl = generate_divergent_p_series(level)
    template = random.choice(QUESTION_TEMPLATES)
    question_latex = template + "\n\n"
    question_latex += "$\n" + latex(summation) + "\n$"
    answer_latex = "**Answer:** The series **diverges**. " + explanation
    return question_latex, answer_latex, lvl

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        question, answer, lvl = generate_question(level)
        questions.append({"question": question, "answer": answer})
    return questions
