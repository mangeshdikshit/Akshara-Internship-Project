import random
from sympy import symbols, Rational, latex, simplify
from sympy.abc import n

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

def generate_sum_given_terms_question(level):
    config = LEVELS[level]
    a = get_random_number(config['pos'], config['neg'], config['frac'])
    d = get_random_number(config['pos'], config['neg'], config['frac'])
    n_val = random.randint(4, 8)

    # Sum formula: Sₙ = n/2 × [2a + (n−1)d]
    sum_expr = Rational(n_val, 2) * (2 * a + (n_val - 1) * d)
    simplified_sum = simplify(sum_expr)

    # LaTeX formatted question and answer
    question_latex = (
        "Find the sum of the arithmetic series given: "
        f"a = ${latex(a)}$, d = ${latex(d)}$, n = ${n_val}$:\n\n"
        r"$S_n = \frac{n}{2} \left[2a + (n - 1)d\right]$" + "\n"
    )

    answer_latex = f"**Answer:** $" + latex(simplified_sum) + "$"

    return question_latex, answer_latex

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        q, a = generate_sum_given_terms_question(level)
        questions.append({"question": q, "answer": a})
    return questions
