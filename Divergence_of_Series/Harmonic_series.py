import random
from sympy import symbols, Sum, Rational, latex, oo
from sympy.abc import i

# Level configuration (levels are illustrative, all based on harmonic series)
LEVELS = {
    1: {'variant': 'basic'},
    2: {'variant': 'shifted'},
    3: {'variant': 'scaled'},
    4: {'variant': 'alt_shift'},
    5: {'variant': 'alt_scaled'},
    6: {'variant': 'harmonic_plus_const'},
    7: {'variant': 'general'}
}

QUESTION_TEMPLATES = [
    "Determine whether the following series converges or diverges:",
    "Does the following infinite series converge or diverge?",
    "Analyze the convergence behavior of the given series:",
    "Check if the following harmonic-style series converges or diverges:",
    "Apply known divergence tests and determine the behavior of this series:",
    "Evaluate the convergence/divergence of the series shown below:",
    "Classify the infinite series as convergent or divergent:",
    "Using the harmonic series knowledge, determine the convergence:"
]

def generate_harmonic_series(variant):
    if variant == 'basic':
        expr = 1 / i
        desc = "This is the standard harmonic series."
    elif variant == 'shifted':
        shift = random.randint(1, 5)
        expr = 1 / (i + shift)
        desc = f"This is a shifted harmonic series with shift = {shift}."
    elif variant == 'scaled':
        scale = random.randint(2, 6)
        expr = 1 / (scale * i)
        desc = f"This is a scaled harmonic series with scale = {scale}."
    elif variant == 'alt_shift':
        expr = 1 / (i + 1)
        desc = "This is the harmonic series starting from i = 2 (i + 1)."
    elif variant == 'alt_scaled':
        expr = 2 / i
        desc = "This is 2 times the harmonic series."
    elif variant == 'harmonic_plus_const':
        expr = 1 / i + Rational(1, 10)
        desc = "Harmonic series plus a constant."
    elif variant == 'general':
        expr = random.choice([1 / i, 2 / (i + 1), 3 / (2 * i)])
        desc = "A general form of harmonic-style series."
    else:
        expr = 1 / i
        desc = "Standard harmonic series (fallback)."

    return expr, desc

def generate_question(level):
    config = LEVELS[level]
    expr, explanation = generate_harmonic_series(config['variant'])
    summation = Sum(expr, (i, 1, oo))

    question_template = random.choice(QUESTION_TEMPLATES)
    question_latex = question_template + "\n\n"
    question_latex += "$\n" + latex(summation) + "\n$"

    answer_latex = "**Answer:** The series **diverges**. " + explanation

    return question_latex, answer_latex, level

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        question, answer, lvl = generate_question(level)
        questions.append({"question": question, "answer": answer})
    return questions
