import random
from sympy import symbols, Sum, Rational, simplify, latex, Pow
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

def get_custom_bounds():
    lower = 1
    upper = random.randint(4, 8)
    return lower, upper

def generate_geometric_expr(var, pos=True, neg=True, frac=False):
    a = get_random_coeff(pos, neg, frac)
    r = get_random_coeff(pos, True, frac)
    if r == 1 or r == -1:
        r += 1
    expr = a * Pow(r, var - 1)
    return expr, a, r

def generate_question(level):
    config = LEVELS[level]
    dims = config['dims']
    vars_map = [i, j, k][:dims]

    main_var = vars_map[0]
    lower, upper = get_custom_bounds()
    limits = [(main_var, lower, upper)]

    expr, a, r = generate_geometric_expr(main_var, config['pos'], config['neg'], config['frac'])

    summation = Sum(expr, (main_var, lower, upper))
    answer = simplify(summation.doit())

    sum_str = f"\\sum_{{{main_var}={lower}}}^{{{upper}}} "
    expr_str = latex(expr)

    templates = [
        "Evaluate the following finite geometric series:",
        "Find the sum of the geometric series below:",
        "Compute the total of this geometric sequence:",
        "What is the result of the following geometric sum?",
        "Calculate the value of the following geometric expression:"
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
