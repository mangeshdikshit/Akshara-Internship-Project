import random
from sympy import Sum, Rational, latex, simplify
from sympy.abc import i, j, k

# Level settings: only for double/triple summations
LEVELS = {
    1: {'dims': 2, 'pos': True, 'neg': False, 'frac': False},
    2: {'dims': 2, 'pos': True, 'neg': True, 'frac': False},
    3: {'dims': 2, 'pos': True, 'neg': True, 'frac': True},
    4: {'dims': 3, 'pos': True, 'neg': False, 'frac': False},
    5: {'dims': 3, 'pos': True, 'neg': True, 'frac': False},
    6: {'dims': 3, 'pos': True, 'neg': True, 'frac': True},
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

def generate_application_expression(vars, pos=True, neg=True, frac=False):
    expr = 0
    num_terms = random.randint(2, 3)
    for _ in range(num_terms):
        term = 0
        for var in vars:
            coeff = get_random_coeff(pos, neg, frac)
            term += coeff * var
        const = get_random_coeff(pos, neg, frac)
        expr += const * term
    return expr

def generate_question_application_linearity(level):
    config = LEVELS[level]
    dims = config['dims']
    vars_map = [i, j, k][:dims]
    limits = [(var, 1, random.randint(3, 5)) for var in vars_map]
    expr = generate_application_expression(vars_map, config['pos'], config['neg'], config['frac'])

    # Apply nested summation
    summation = expr
    for lim in reversed(limits):
        summation = Sum(summation, lim)

    answer = simplify(summation.doit())

    # Template variation
    templates = [
        "Evaluate the expression using linearity for nested summations:",
        "Apply linearity properties to simplify the double/triple summation:",
        "Use linearity of summations to compute the following:",
        "Simplify and evaluate using summation rules:",
        "Apply linearity across dimensions to evaluate:"
    ]
    template = random.choice(templates)

    # LaTeX formatting
    sum_str = ''.join([f"\\sum_{{{v}={lo}}}^{{{hi}}} " for (v, lo, hi) in limits])
    expr_str = latex(expr)

    question_latex = f"{template}\n\n$\n{sum_str}{expr_str}\n$"
    answer_latex = f"**Answer:** {answer}"
    return question_latex, answer_latex

def generate_questions(level, num_questions):
    results = []
    for _ in range(num_questions):
        question, answer = generate_question_application_linearity(level)
        results.append({'question': question, 'answer': answer})
    return results
