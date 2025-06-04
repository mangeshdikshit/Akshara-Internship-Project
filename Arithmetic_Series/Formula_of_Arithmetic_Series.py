import random
from sympy import symbols, Sum, simplify, latex, Rational
from sympy.abc import i

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

def get_random_number(pos=True, neg=False, frac=False):
    nums = list(range(1, 11))
    if neg:
        nums += [-x for x in nums]
    num = random.choice(nums)
    if frac and random.choice([True, False]):
        denom = random.randint(2, 5)
        num = Rational(num, denom)
    return num

def generate_arithmetic_series_question(level):
    config = LEVELS[level]
    a = get_random_number(config['pos'], config['neg'], config['frac'])
    d = get_random_number(config['pos'], config['neg'], config['frac'])
    n = random.randint(4, 8)

    expr = a + (i - 1) * d
    summation = Sum(expr, (i, 1, n))
    answer = simplify(summation.doit())

    # LaTeX rendering for single-line equation
    question_latex = (
        r"Evaluate the arithmetic series: "
        + r"$\sum_{i=1}^{%d} \left(%s + (i - 1) \cdot %s\right)$"
        % (n, latex(a), latex(d))
    )
    answer_latex = r"**Answer:** $" + latex(answer) + r"$"

    return question_latex, answer_latex

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        q, a = generate_arithmetic_series_question(level)
        questions.append({"question": q, "answer": a})
    return questions
