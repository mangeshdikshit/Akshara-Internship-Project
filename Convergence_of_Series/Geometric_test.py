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

def get_random_ratio():
    numerators = list(range(1, 9))
    denominators = list(range(2, 10))
    r = Rational(random.choice(numerators), random.choice(denominators))
    if random.choice([True, False]):
        r = -r
    return r

def get_random_a0(pos=True, neg=True, frac=False):
    coeff_range = list(range(1, 10))
    if neg:
        coeff_range += [-x for x in coeff_range]
    a0 = random.choice(coeff_range)
    if frac and random.choice([True, False]):
        denom = random.randint(2, 5)
        a0 = Rational(a0, denom)
    return a0

def generate_question(level):
    config = LEVELS[level]

    r = get_random_ratio()
    a0 = get_random_a0(config['pos'], config['neg'], config['frac'])

    expr = a0 * r**i
    summation = Sum(expr, (i, 0, float('inf')))
    answer = simplify(a0 / (1 - r))

    sum_str = f"\\sum_{{i=0}}^{{\\infty}}"
    expr_str = latex(expr)

    templates = [
        "Determine whether the following geometric series converges. If it does, find its sum:",
        "Evaluate the convergence of the geometric series given below. If convergent, compute the sum:",
        "Does the following geometric series converge? If so, what is the value it converges to?",
        "Analyze the convergence of this geometric series and provide the sum if it exists:",
        "Apply the geometric series test to determine if the series below converges, and find the sum if applicable:"
    ]

    question_latex = random.choice(templates) + "\n\n"
    question_latex += "$\n" + sum_str + expr_str + "\n$"

    answer_latex = "**Answer:** \n$" + latex(answer) + "$"

    return question_latex, answer_latex

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        q, a = generate_question(level)
        questions.append({"question": q, "answer": a})
    return questions
