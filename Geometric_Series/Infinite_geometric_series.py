import random
from sympy import symbols, Sum, Rational, latex, simplify, oo
from sympy.abc import i, j, k

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

def get_random_coeff(pos=True, neg=True, frac=False):
    coeff_range = list(range(1, 6))
    if neg:
        coeff_range += [-x for x in coeff_range]
    coeff = random.choice(coeff_range)
    if frac and random.choice([True, False]):
        denom = random.randint(2, 5)
        coeff = Rational(coeff, denom)
    return coeff

def get_random_ratio():
    num = random.randint(1, 4)
    denom = random.randint(num + 1, num + 4)
    r = Rational(num, denom)
    if random.choice([True, False]):
        r *= -1
    return r  # ensures |r| < 1

def generate_infinite_geometric_expr(var, pos=True, neg=True, frac=False):
    a = get_random_coeff(pos, neg, frac)
    r = get_random_ratio()
    expr = a * r**var
    return expr, a, r

def generate_question(level):
    config = LEVELS[level]
    var = i
    expr, a, r = generate_infinite_geometric_expr(var, config['pos'], config['neg'], config['frac'])

    summation = Sum(expr, (var, 0, oo))
    answer = simplify(summation.doit())

    sum_str = f"\\sum_{{{var}=0}}^{{\\infty}} "
    expr_str = latex(expr)

    templates = [
        "Evaluate the following infinite geometric series:",
        "Compute the sum of the infinite geometric progression below:",
        "Determine the value of this converging geometric series:",
        "Find the sum of the infinite geometric series (|r| < 1):",
        "Calculate the value of the following convergent series:"
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
