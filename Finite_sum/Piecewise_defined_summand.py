import random
from sympy import symbols, Sum, Rational, Piecewise, Eq, Mod, simplify, Abs, latex
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
    upper = lower + random.randint(3, 6)
    return lower, upper

def generate_piecewise_expression(var, pos=True, neg=True, frac=False):
    template = random.choice(['linear', 'quadratic', 'abs', 'mixed'])

    if template == 'linear':
        expr_even = get_random_coeff(pos, neg, frac) * var + get_random_coeff(pos, neg, frac)
        expr_odd = get_random_coeff(pos, neg, frac) * var + get_random_coeff(pos, neg, frac)

    elif template == 'quadratic':
        expr_even = get_random_coeff(pos, neg, frac) * var**2 + get_random_coeff(pos, neg, frac)
        expr_odd = get_random_coeff(pos, neg, frac) * var + get_random_coeff(pos, neg, frac)

    elif template == 'abs':
        expr_even = Abs(get_random_coeff(pos, neg, frac) * var + get_random_coeff(pos, neg, frac))
        expr_odd = Abs(get_random_coeff(pos, neg, frac) * var - get_random_coeff(pos, neg, frac))

    elif template == 'mixed':
        expr_even = get_random_coeff(pos, neg, frac) * var + get_random_coeff(pos, neg, frac)
        expr_odd = get_random_coeff(pos, neg, frac) * var**2 + get_random_coeff(pos, neg, frac) * var

    pw_expr = Piecewise((expr_even, Eq(Mod(var, 2), 0)), (expr_odd, True))
    return pw_expr

def generate_question(level):
    config = LEVELS[level]
    dims = config['dims']
    vars_map = [i, j, k][:dims]

    outer_var = vars_map[0]
    lower, upper = get_custom_bounds()
    limits = [(outer_var, lower, upper)]

    if dims >= 2:
        for v in vars_map[1:]:
            lo, hi = get_custom_bounds()
            limits.append((v, lo, hi))

    expr = generate_piecewise_expression(outer_var, config['pos'], config['neg'], config['frac'])

    # Add interactions with inner variables
    for var in vars_map[1:]:
        coeff = get_random_coeff(config['pos'], config['neg'], config['frac'])
        expr += coeff * var

    # Build summation
    summation = expr
    for lim in reversed(limits):
        summation = Sum(summation, lim)

    # Compute answer
    answer = simplify(summation.doit())

    # LaTeX formatting
    sum_str = ''.join([f"\\sum_{{{v}={lo}}}^{{{hi}}} " for v, lo, hi in limits])
    expr_str = latex(expr)

    question_latex = "Evaluate the following finite sum with a piecewise-defined summand:\n\n"
    question_latex += "$\n" + sum_str + expr_str + "\n$"

    answer_latex = "**Answer:** $" + latex(answer) + "$"

    return {"question": question_latex, "answer": answer_latex}

def generate_questions(level, count=10):
    return [generate_question(level) for _ in range(count)]
