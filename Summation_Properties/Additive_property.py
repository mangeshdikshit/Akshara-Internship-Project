import random
from sympy import symbols, Sum, Rational, simplify, latex
from sympy.abc import i, j, k

# Level setup
LEVELS = {
    1: {'pos': True, 'neg': False, 'frac': False},
    2: {'pos': True, 'neg': True, 'frac': False},
    3: {'pos': True, 'neg': True, 'frac': True},
    4: {'pos': True, 'neg': False, 'frac': False},
    5: {'pos': True, 'neg': True, 'frac': False},
    6: {'pos': True, 'neg': True, 'frac': True},
    7: {'pos': True, 'neg': True, 'frac': True}
}

QUESTION_TEMPLATES = [
    "Use the additive property of summation to evaluate the following:",
    "Break the sum using summation linearity and compute the value:",
    "Evaluate the following sum using properties of summation:",
    "Apply the linearity property of summation to find the result:",
    "Use distributive property of summation to simplify and compute:"
]

def get_random_term(pos=True, neg=True, frac=False):
    coeffs = list(range(1, 6))
    if neg:
        coeffs += [-x for x in coeffs]
    coeff = random.choice(coeffs)
    if frac and random.choice([True, False]):
        coeff = Rational(coeff, random.randint(2, 4))
    return coeff

def generate_question(level):
    config = LEVELS[level]
    template = random.choice(QUESTION_TEMPLATES)

    if level in [1, 2, 3]:  # Single summation
        a = get_random_term(**config)
        b = get_random_term(**config)
        n = random.randint(4, 8)

        term1 = a * i
        term2 = b
        expr = term1 + term2

        sum_expr = Sum(expr, (i, 1, n))
        simplified = simplify(sum_expr.doit())

        question_latex = f"{template}\n\n$\n\\sum_{{i=1}}^{{{n}}} {latex(expr)}\n$"
        answer_latex = (
            f"**Answer:**\n"
            f"$\\sum_{{i=1}}^{{{n}}} {latex(expr)} = "
            f"\\sum_{{i=1}}^{{{n}}} {latex(term1)} + \\sum_{{i=1}}^{{{n}}} {latex(term2)} = {latex(simplified)}$"
        )

    elif level in [4, 5, 6]:  # Double summation
        a = get_random_term(**config)
        b = get_random_term(**config)
        c = get_random_term(**config)

        n1 = random.randint(3, 6)
        n2 = random.randint(2, 5)

        term1 = a * i
        term2 = b * j
        term3 = c
        expr = term1 + term2 + term3

        sum_expr = Sum(Sum(expr, (i, 1, n1)), (j, 1, n2))
        simplified = simplify(sum_expr.doit())

        question_latex = (
            f"{template}\n\n"
            f"$\n\\sum_{{j=1}}^{{{n2}}} \\sum_{{i=1}}^{{{n1}}} {latex(expr)}\n$"
        )
        answer_latex = (
            f"**Answer:**\n"
            f"$\\sum_{{j=1}}^{{{n2}}} \\sum_{{i=1}}^{{{n1}}} {latex(expr)} = "
            f"\\sum_{{j=1}}^{{{n2}}} \\sum_{{i=1}}^{{{n1}}} {latex(term1)} + "
            f"\\sum_{{j=1}}^{{{n2}}} \\sum_{{i=1}}^{{{n1}}} {latex(term2)} + "
            f"\\sum_{{j=1}}^{{{n2}}} \\sum_{{i=1}}^{{{n1}}} {latex(term3)} = {latex(simplified)}$"
        )

    else:  # Level 7 - Triple summation
        a = get_random_term(**config)
        b = get_random_term(**config)
        c = get_random_term(**config)
        d = get_random_term(**config)

        n1 = random.randint(2, 4)
        n2 = random.randint(2, 4)
        n3 = random.randint(2, 4)

        term1 = a * i
        term2 = b * j
        term3 = c * k
        term4 = d
        expr = term1 + term2 + term3 + term4

        sum_expr = Sum(Sum(Sum(expr, (i, 1, n1)), (j, 1, n2)), (k, 1, n3))
        simplified = simplify(sum_expr.doit())

        question_latex = (
            f"{template}\n\n"
            f"$\n\\sum_{{k=1}}^{{{n3}}} \\sum_{{j=1}}^{{{n2}}} "
            f"\\sum_{{i=1}}^{{{n1}}} {latex(expr)}\n$"
        )
        answer_latex = (
            f"**Answer:**\n"
            f"$\\sum_{{k=1}}^{{{n3}}} \\sum_{{j=1}}^{{{n2}}} \\sum_{{i=1}}^{{{n1}}} {latex(expr)} = "
            # f"\\sum_{{k=1}}^{{{n3}}} \\sum_{{j=1}}^{{{n2}}} \\sum_{{i=1}}^{{{n1}}} {latex(term1)} + "
            # f"\\sum_{{k=1}}^{{{n3}}} \\sum_{{j=1}}^{{{n2}}} \\sum_{{i=1}}^{{{n1}}} {latex(term2)} + "
            # f"\\sum_{{k=1}}^{{{n3}}} \\sum_{{j=1}}^{{{n2}}} \\sum_{{i=1}}^{{{n1}}} {latex(term3)} + "
            # f"\\sum_{{k=1}}^{{{n3}}} \\sum_{{j=1}}^{{{n2}}} \\sum_{{i=1}}^{{{n1}}} {latex(term4)} 
            f" {latex(simplified)}$"
        )

    return {"question": question_latex, "answer": answer_latex}

def generate(level, num_questions):
    return [generate_question(level) for _ in range(num_questions)]
