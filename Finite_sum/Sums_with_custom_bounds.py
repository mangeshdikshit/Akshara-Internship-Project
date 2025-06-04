import random
from sympy import symbols, Sum, Rational, latex, simplify
from sympy.abc import i, j, k

# Levels configuration
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
    coeff_range = list(range(1, 10))
    if neg:
        coeff_range += [-x for x in coeff_range]
    coeff = random.choice(coeff_range)
    if frac and random.choice([True, False]):
        denom = random.randint(2, 5)
        coeff = Rational(coeff, denom)
    return coeff

def get_custom_bounds():
    lower = random.randint(-3, 3)
    upper = lower + random.randint(2, 5)
    return lower, upper

def generate_expression(vars, pos=True, neg=True, frac=False):
    template = random.choice(['linear', 'quadratic', 'mixed', 'nested'])
    expr = 0

    if template == 'linear':
        for var in vars:
            coeff = get_random_coeff(pos, neg, frac)
            expr += coeff * var
        expr += get_random_coeff(pos, neg, frac)

    elif template == 'quadratic':
        for var in vars:
            coeff = get_random_coeff(pos, neg, frac)
            expr += coeff * var**2
        expr += get_random_coeff(pos, neg, frac)

    elif template == 'mixed':
        for var in vars:
            coeff1 = get_random_coeff(pos, neg, frac)
            coeff2 = get_random_coeff(pos, neg, frac)
            expr += coeff1 * var + coeff2 * var**2
        expr += get_random_coeff(pos, neg, frac)

    elif template == 'nested':
        if len(vars) >= 2:
            v1, v2 = vars[0], vars[1]
            expr = get_random_coeff(pos, neg, frac) * v1 * v2
        else:
            expr = get_random_coeff(pos, neg, frac) * vars[0]
        expr += get_random_coeff(pos, neg, frac)

    return expr

def generate_question(level):
    config = LEVELS[level]
    dims = config['dims']
    vars_map = [i, j, k][:dims]

    # Custom bounds for each summation variable
    limits = []
    for var in vars_map:
        lower, upper = get_custom_bounds()
        limits.append((var, lower, upper))

    expr = generate_expression(vars_map, config['pos'], config['neg'], config['frac'])

    # Build the sympy Sum object
    summation = expr
    for lim in reversed(limits):
        summation = Sum(summation, lim)

    # Compute result
    answer = simplify(summation.doit())

    # Format LaTeX manually with one clean limit per operator
    sum_str = ''.join([f"\\sum_{{{var}={lo}}}^{{{hi}}} " for var, lo, hi in limits])
    expr_str = latex(expr)

    question_latex = "Evaluate the following finite sum with custom bounds:\n\n"
    question_latex += "$\n" + sum_str + expr_str + "\n$"

    answer_latex = "**Answer:** $" + latex(answer) + "$"

    return {"question": question_latex, "answer": answer_latex}

def generate_questions(level, count=10):
    questions = []
    for _ in range(count):
        questions.append(generate_question(level))
    return questions
