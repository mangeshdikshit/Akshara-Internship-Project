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
    "Use the distributive property of summation to evaluate:",
    "Apply summation distribution over addition and simplify the result:",
    "Break the sum into simpler parts using the distributive rule and compute:",
    "Distribute the summation over the expression and evaluate:",
    "Use the linearity of summation to simplify and solve:"
]

def get_random_term(pos=True, neg=True, frac=False):
    values = list(range(1, 6))
    if neg:
        values += [-x for x in values]
    val = random.choice(values)
    if frac and random.choice([True, False]):
        val = Rational(val, random.randint(2, 5))
    return val

def generate_question(level):
    config = LEVELS[level]
    template = random.choice(QUESTION_TEMPLATES)

    # Levels 1–3: Single summation
    if level in [1, 2, 3]:
        a = get_random_term(**config)
        b = get_random_term(**config)
        n = random.randint(4, 8)

        term1 = a * i
        term2 = b
        expr = term1 + term2

        simplified = simplify(Sum(expr, (i, 1, n)).doit())

        question = f"{template}\n\n$\\sum_{{i=1}}^{{{n}}} {latex(expr)}$"
        answer = (
            f"**Answer:**\n"
            f"$\\sum_{{i=1}}^{{{n}}} {latex(expr)} = "
            f"\\sum_{{i=1}}^{{{n}}} {latex(term1)} + \\sum_{{i=1}}^{{{n}}} {latex(term2)}"
            f" = {latex(simplified)}$"
        )

    # Levels 4–6: Double summation
    elif level in [4, 5, 6]:
        a1 = get_random_term(**config)
        a2 = get_random_term(**config)
        b = get_random_term(**config)

        n = random.randint(3, 5)
        m = random.randint(3, 5)

        term1 = a1 * i
        term2 = a2 * j
        term3 = b
        expr = term1 + term2 + term3

        simplified = simplify(Sum(Sum(expr, (i, 1, n)), (j, 1, m)).doit())

        question = f"{template}\n\n$\\sum_{{j=1}}^{{{m}}} \\sum_{{i=1}}^{{{n}}} {latex(expr)}$"
        answer = (
            f"**Answer:**\n"
            f"$\\sum_{{j=1}}^{{{m}}} \\sum_{{i=1}}^{{{n}}} {latex(expr)} = "
            f"\\sum_{{j=1}}^{{{m}}} \\sum_{{i=1}}^{{{n}}} {latex(term1)} + "
            f"\\sum_{{j=1}}^{{{m}}} \\sum_{{i=1}}^{{{n}}} {latex(term2)} + "
            f"\\sum_{{j=1}}^{{{m}}} \\sum_{{i=1}}^{{{n}}} {latex(term3)}"
            f" = {latex(simplified)}$"
        )

    # Level 7: Triple summation
    else:
        a1 = get_random_term(**config)
        a2 = get_random_term(**config)
        a3 = get_random_term(**config)
        b = get_random_term(**config)

        n = random.randint(2, 4)
        m = random.randint(2, 4)
        l = random.randint(2, 4)

        term1 = a1 * i
        term2 = a2 * j
        term3 = a3 * k
        term4 = b
        expr = term1 + term2 + term3 + term4

        simplified = simplify(Sum(Sum(Sum(expr, (i, 1, n)), (j, 1, m)), (k, 1, l)).doit())

        question = (
            f"{template}\n\n$\\sum_{{k=1}}^{{{l}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{i=1}}^{{{n}}} {latex(expr)}$"
        )
        answer = (
            f"**Answer:**\n"
            f"$\\sum_{{k=1}}^{{{l}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{i=1}}^{{{n}}} {latex(expr)} = "
            # f"\\sum_{{k=1}}^{{{l}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{i=1}}^{{{n}}} {latex(term1)} + "
            # f"\\sum_{{k=1}}^{{{l}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{i=1}}^{{{n}}} {latex(term2)} + "
            # f"\\sum_{{k=1}}^{{{l}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{i=1}}^{{{n}}} {latex(term3)} + "
            # f"\\sum_{{k=1}}^{{{l}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{i=1}}^{{{n}}} {latex(term4)}"
            f"{latex(simplified)}$"
        )

    return {"question": question, "answer": answer}

def generate(level, num_questions):
    return [generate_question(level) for _ in range(num_questions)]
