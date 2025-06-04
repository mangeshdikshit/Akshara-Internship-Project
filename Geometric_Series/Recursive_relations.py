import random
from sympy import symbols, Sum, Rational, simplify, latex
from sympy.abc import i

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
    coeff_range = [1, 2]  # Reduced range to 1 and 2
    if neg:
        coeff_range += [-x for x in coeff_range]
    coeff = random.choice(coeff_range)
    if frac and random.choice([True, False]):
        denom = random.randint(2, 3)  # Simpler denominator
        coeff = Rational(coeff, denom)
    return coeff

def generate_recursive_expression(pos=True, neg=True, frac=False):
    a0 = get_random_coeff(pos, neg, frac)
    r = get_random_coeff(pos=True, neg=False, frac=True)
    n = random.randint(3, 5)  # Fewer terms for easier computation
    expr = a0 * r**i
    return expr, a0, r, n

def generate_question(level):
    config = LEVELS[level]
    var = i
    expr, a0, r, n = generate_recursive_expression(config['pos'], config['neg'], config['frac'])

    summation = Sum(expr, (var, 0, n))
    answer = simplify(summation.doit())

    sum_str = f"\\sum_{{{var}=0}}^{{{n}}} "
    expr_str = latex(expr)

    templates = [
        f"Given a recursive sequence defined as $a_0 = {latex(a0)}$ and $a_n = {latex(a0)}({latex(r)})^n$, evaluate the total sum up to the given index:",
        f"Consider a sequence with initial term $a_0 = {latex(a0)}$ and common ratio ${latex(r)}$. What is the value of the sum up to $n = {n}$?",
        f"The geometric sequence starts with $a_0 = {latex(a0)}$ and follows $a_n = a_0 r^n$ where $r = {latex(r)}$. Find the sum from $i = 0$ to $i = {n}$.",
        f"Evaluate the finite sum of the recursive geometric sequence: $a_0 = {latex(a0)}$, $r = {latex(r)}$, for $n = 0$ to $n = {n}$.",
        f"A geometric progression is defined recursively. If $a_0 = {latex(a0)}$ and $r = {latex(r)}$, calculate the sum from $i = 0$ to $i = {n}$."
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
