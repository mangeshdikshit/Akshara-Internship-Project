import random
from sympy import symbols, Sum, Rational, latex, simplify
from sympy.abc import i, j, k

# Levels configuration for combining linear terms
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
    coeff_range = list(range(1, 5))
    if neg:
        coeff_range += [-x for x in coeff_range]
    coeff = random.choice(coeff_range)
    if frac and random.choice([True, False]):
        denom = random.randint(2, 5)
        coeff = Rational(coeff, denom)
    return coeff

def generate_combining_expression(vars, pos=True, neg=True, frac=False):
    expr = 0
    num_terms = random.randint(2, 3)
    for _ in range(num_terms):
        term = 0
        for var in vars:
            coeff = get_random_coeff(pos, neg, frac)
            term += coeff * var
        expr += term
    return expr

def generate_question_combining_terms(level):
    config = LEVELS[level]
    dims = config['dims']
    vars_map = [i, j, k][:dims]
    limits = [(var, 1, random.randint(3, 6)) for var in vars_map]
    expr = generate_combining_expression(vars_map, config['pos'], config['neg'], config['frac'])

    # Build nested Sum
    summation = expr
    for lim in reversed(limits):
        summation = Sum(summation, lim)

    # Compute simplified answer
    answer = simplify(summation.doit())

    # Template variations
    templates = [
        "Evaluate by combining linear terms inside the summation:",
        "Use the linearity of summation to simplify and compute:",
        "Simplify the summation by combining like terms:",
        "Apply the linearity rule to the sum of multiple terms:",
        "Combine all linear expressions and evaluate the sum:"
    ]
    template = random.choice(templates)

    # Manual LaTeX construction
    sum_str = ''.join([f"\\sum_{{{v}={lo}}}^{{{hi}}} " for (v, lo, hi) in limits])
    expr_str = latex(expr)

    question_latex = f"{template}\n\n$\n{sum_str}{expr_str}\n$"
    answer_latex = f"**Answer:** {answer}"
    return question_latex, answer_latex

def generate_questions(level, num_questions):
    results = []
    for _ in range(num_questions):
        question, answer = generate_question_combining_terms(level)
        results.append({'question': question, 'answer': answer})
    return results
