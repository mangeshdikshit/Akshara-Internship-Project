import random
from sympy import symbols, Sum, Rational, latex, simplify
from sympy.abc import i, j, k  # i is used as the summation variable

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
    coeff_range = [1, 2]  # Simplified to small values
    if neg:
        coeff_range += [-x for x in coeff_range]
    coeff = random.choice(coeff_range)
    if frac and random.choice([True, False]):
        denom = random.randint(2, 3)  # Simpler denominator
        coeff = Rational(coeff, denom)
    return coeff

def get_growth_or_decay_rate():
    if random.choice(['growth', 'decay']) == 'growth':
        num = random.choice([11, 12])  # 1.1 or 1.2
        denom = 10
        label = "growth"
    else:
        num = random.choice([8, 9])  # 0.8 or 0.9
        denom = 10
        label = "decay"
    r = Rational(num, denom)
    return r, label

def generate_growth_decay_expr(var, pos=True, neg=True, frac=False):
    a = get_random_coeff(pos, neg, frac)
    r, label = get_growth_or_decay_rate()
    n = random.randint(2, 4)  # Keep sum to 3–5 terms
    expr = a * r**var
    return expr, a, r, n, label

def generate_question(level):
    allow_pos = LEVELS[level]['pos']
    allow_neg = LEVELS[level]['neg']
    allow_frac = LEVELS[level]['frac']

    var = i
    expr, initial_a, ratio_r, num_stages_n, type_label = generate_growth_decay_expr(
        var, 
        pos=allow_pos, 
        neg=allow_neg, 
        frac=allow_frac
    )

    summation = Sum(expr, (var, 0, num_stages_n))
    answer = simplify(summation.doit())

    sum_str = f"\\sum_{{{latex(var)}=0}}^{{{latex(num_stages_n)}}} "
    expr_str = latex(expr)

    templates = [
        f"Evaluate the following geometric series representing a {type_label} model:",
        f"A quantity changes following a {type_label} trend. Compute the total sum after {num_stages_n + 1} stages (from stage 0 to stage {num_stages_n}):",
        f"In a {type_label} scenario, evaluate the accumulated amount from time step 0 to {num_stages_n}:",
        f"Given a {type_label} situation, determine the total amount over the following geometric progression from index 0 to {num_stages_n}:",
        f"Find the total change in the {type_label} model, which has {num_stages_n + 1} terms, using this geometric series:"
    ]

    question_latex = random.choice(templates) + "\n\n"
    question_latex += "$\n" + sum_str + expr_str + "\n$"

    answer_latex = "**Answer:** \n$" + latex(answer) + "$"

    return question_latex, answer_latex

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        current_level = level if isinstance(level, int) and 1 <= level <= 7 else 1
        q, a = generate_question(current_level)
        questions.append({"question": q, "answer": a})
    return questions
