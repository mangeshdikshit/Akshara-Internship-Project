import random
from sympy import symbols, Sum, Rational, latex, simplify
from sympy.abc import i, j, k

# Configuration for levels
LEVELS = {
    1: {'dims': 1, 'terms': 2, 'pos': True, 'neg': False, 'frac': False},
    2: {'dims': 1, 'terms': 2, 'pos': True, 'neg': True, 'frac': False},
    3: {'dims': 1, 'terms': 2, 'pos': True, 'neg': True, 'frac': True},
    4: {'dims': 2, 'terms': 2, 'pos': True, 'neg': False, 'frac': False},
    5: {'dims': 2, 'terms': 2, 'pos': True, 'neg': True, 'frac': False},
    6: {'dims': 2, 'terms': 2, 'pos': True, 'neg': True, 'frac': True},
    7: {'dims': 3, 'terms': 2, 'pos': True, 'neg': True, 'frac': True}
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

def generate_expression(vars, num_terms=2, pos=True, neg=True, frac=False):
    expr = 0
    for _ in range(num_terms):
        term = 0
        for var in vars:
            coeff = get_random_coeff(pos, neg, frac)
            term += coeff * var
        const = get_random_coeff(pos, neg, frac)
        expr += const * term
    return expr

def generate_question_sum_of_sum(level):
    config = LEVELS[level]
    dims = config['dims']
    num_terms = config['terms']
    vars_map = [i, j, k][:dims]
    limits = [(var, 1, random.randint(3, 6)) for var in vars_map]

    expr = generate_expression(vars_map, num_terms, config['pos'], config['neg'], config['frac'])
    summation = expr
    for lim in reversed(limits):
        summation = Sum(summation, lim)

    answer = simplify(summation.doit())

    # Template variety
    templates = [
        "Evaluate using the linearity property (sum of a sum):",
        "Compute the value using summation rules:",
        "Find the result of the following nested summation:",
        "Simplify using the distributive nature of summation:",
        "Use summation linearity to compute:"
    ]
    template = random.choice(templates)

    sum_str = ''.join([f"\\sum_{{{v}={lo}}}^{{{hi}}} " for (v, lo, hi) in limits])
    expr_str = latex(expr)
    question_latex = f"{template}\n\n$\n{sum_str}{expr_str}\n$"

    answer_latex = f"**Answer:** {answer}"
    return question_latex, answer_latex

def generate_questions(level, num_questions):
    results = []
    for _ in range(num_questions):
        question, answer = generate_question_sum_of_sum(level)
        results.append({'question': question, 'answer': answer})
    return results

# Example of generating questions
# questions = generate_questions(3, 5)
# for q in questions:
#     print(q['question'])
#     print(q['answer'])
