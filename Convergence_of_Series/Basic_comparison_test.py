import random
from sympy import symbols, Sum, Rational, simplify, latex, oo
from sympy.abc import i

# Level setup
LEVELS = {
    1: {'dims': 1, 'pos': True, 'neg': False, 'frac': False},
    2: {'dims': 1, 'pos': True, 'neg': True, 'frac': False},
    3: {'dims': 1, 'pos': True, 'neg': True, 'frac': True},
    4: {'dims': 2, 'pos': True, 'neg': False, 'frac': False},
    5: {'dims': 2, 'pos': True, 'neg': True, 'frac': False},
    6: {'dims': 2, 'pos': True, 'neg': True, 'frac': True},
    7: {'dims': 3, 'pos': True, 'neg': True, 'frac': True}
}

def get_random_p(comparison=True):
    if comparison:
        return Rational(random.randint(2, 5), random.randint(1, 3))
    else:
        return Rational(random.randint(1, 10), random.randint(1, 3))

def generate_comparison_question(level):
    config = LEVELS[level]

    p_ref = get_random_p(comparison=True)
    reference_series = 1 / i**p_ref

    delta = random.choice([-1, 1]) * Rational(random.randint(1, 2), random.randint(2, 4))
    p_test = p_ref + delta
    test_series = 1 / i**p_test

    sum_expr = Sum(test_series, (i, 1, oo))

    if p_test > 1:
        conclusion = "The series converges by comparison with a convergent p-series."
    else:
        conclusion = "The series diverges by comparison with a divergent p-series."

    templates = [
        "Using the basic comparison test, determine whether the following series converges or diverges:",
        "Analyze the behavior of the following infinite series using the comparison test:",
        "Apply the comparison test to evaluate the convergence of this series:",
        "Does the following infinite series converge or diverge? Use the basic comparison test to justify your answer:",
        "Determine the nature (convergent/divergent) of the following series by comparing it with a standard p-series:",
        "Is the series convergent or divergent? Use comparison test principles:",
        "Use a p-series comparison to decide whether the following sum converges:"
    ]

    question_latex = random.choice(templates) + "\n\n"
    question_latex += "$\n\\sum_{i=1}^{\\infty} " + latex(test_series) + "\n$"

    ref_info = f"(Compared with $\\sum 1/i^{{{latex(p_ref)}}}$)"
    answer_latex = f"**Answer:** \n{conclusion} {ref_info}"

    return question_latex, answer_latex

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        q, a = generate_comparison_question(level)
        questions.append({"question": q, "answer": a})
    return questions
