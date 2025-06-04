import random
from sympy import symbols, Sum, Rational, simplify, latex
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

def get_random_p():
    # Choose p randomly in (0.2, 3.0), rational format
    numer = random.randint(1, 9)
    denom = random.randint(1, 5)
    p = Rational(numer, denom)
    if random.random() < 0.5:
        p += random.randint(0, 2)  # shift p upward sometimes
    return p

def generate_question(level):
    config = LEVELS[level]

    p = get_random_p()
    expr = 1 / i**p
    summation = Sum(expr, (i, 1, float('inf')))

    # p-series convergence condition: converges if p > 1
    if p > 1:
        result = "The series converges."
    else:
        result = "The series diverges."

    # Build LaTeX string
    sum_str = f"\\sum_{{i=1}}^{{\\infty}}"
    expr_str = latex(expr)

    templates = [
        "Determine whether the following p-series converges or diverges:",
        "Analyze the convergence behavior of the given p-series:",
        "Does this p-series converge or diverge? Justify based on the value of p:",
        "Examine the series and determine if it converges or diverges:",
        "Using the p-series test, evaluate whether the series below converges:"
    ]

    question_latex = random.choice(templates) + "\n\n"
    question_latex += "$\n" + sum_str + expr_str + "\n$"

    answer_latex = "**Answer:** \n" + result

    return question_latex, answer_latex

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        q, a = generate_question(level)
        questions.append({"question": q, "answer": a})
    return questions
