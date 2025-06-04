import random
from sympy import symbols, Rational, Eq, solve, simplify, latex
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
    nums = list(range(1, 10))
    if neg:
        nums += [-x for x in nums]
    num = random.choice(nums)
    if frac and random.choice([True, False]):
        denom = random.randint(2, 5)
        num = Rational(num, denom)
    return num

def generate_find_n_question(level):
    config = LEVELS[level]
    a = get_random_number(config['pos'], config['neg'], config['frac'])
    d = get_random_number(config['pos'], config['neg'], config['frac'])
    n_val = random.randint(3, 7)

    # Compute S_n using formula
    S_n = Rational(n_val, 2) * (2 * a + (n_val - 1) * d)

    # Solve equation S = n/2 * [2a + (n - 1)d] for n
    expr = n/2 * (2 * a + (n - 1) * d)
    eq = Eq(expr, S_n)
    sol = solve(eq, n)
    n_solution = [s for s in sol if s.is_real and s > 0]
    n_final = simplify(n_solution[0]) if n_solution else "No valid solution"

    # Question
    question = (
        "Find the number of terms n for the arithmetic series: "
        f"a = ${latex(a)}$, d = ${latex(d)}$, Sₙ = ${latex(S_n)}$:\n\n"
        r"$S_n = \frac{n}{2} \left[2a + (n - 1)d\right]$"
    )

    answer = f"**Answer:** $" + latex(n_final) + "$"

    return question, answer

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        q, a = generate_find_n_question(level)
        questions.append({"question": q, "answer": a})
    return questions
