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
    "Using the property of splitting and merging summation ranges, evaluate:",
    "Break the summation into two parts and compute the result:",
    "Apply the summation range splitting identity to simplify and evaluate:",
    "Divide the sum into two simpler sums, then find the total:",
    "Use summation partitioning property to evaluate:"
]

def get_random_coeff(pos=True, neg=True, frac=False):
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

    if level in [1, 2, 3]:  # Single summation
        a = random.randint(1, 3)
        c = random.randint(a + 4, a + 6)
        b = random.randint(a + 1, c - 1)

        coeff = get_random_coeff(**config)
        expr = coeff * i

        simplified = simplify(Sum(expr, (i, a, c)).doit())

        question = f"{template}\n\n$\\sum_{{i={a}}}^{{{c}}} {latex(expr)}$"
        answer = (
            "**Answer:**\n"
            f"$\\sum_{{i={a}}}^{{{c}}} {latex(expr)} = "
            f"\\sum_{{i={a}}}^{{{b}}} {latex(expr)} + "
            f"\\sum_{{i={b+1}}}^{{{c}}} {latex(expr)} = "
            f"{latex(simplified)}$"
        )

    elif level in [4, 5, 6]:  # Double summation, split inner
        a = random.randint(1, 3)
        c = random.randint(a + 3, a + 5)
        b = random.randint(a + 1, c - 1)
        m = random.randint(2, 4)

        coeff1 = get_random_coeff(**config)
        coeff2 = get_random_coeff(**config)

        expr = coeff1 * i + coeff2 * j
        simplified = simplify(Sum(Sum(expr, (i, a, c)), (j, 1, m)).doit())

        question = f"{template}\n\n$\\sum_{{j=1}}^{{{m}}} \\sum_{{i={a}}}^{{{c}}} {latex(expr)}$"
        answer = (
            "**Answer:**\n"
            f"$\\sum_{{j=1}}^{{{m}}} \\sum_{{i={a}}}^{{{c}}} {latex(expr)} = "
            f"\\sum_{{j=1}}^{{{m}}} \\sum_{{i={a}}}^{{{b}}} {latex(expr)} + "
            f"\\sum_{{j=1}}^{{{m}}} \\sum_{{i={b+1}}}^{{{c}}} {latex(expr)} = "
            f"{latex(simplified)}$"
        )

    else:  # Level 7: Triple summation, split innermost
        a = random.randint(1, 2)
        c = random.randint(a + 2, a + 4)
        b = random.randint(a + 1, c - 1)
        m = random.randint(2, 3)
        l = random.randint(2, 3)

        coeff1 = get_random_coeff(**config)
        coeff2 = get_random_coeff(**config)
        coeff3 = get_random_coeff(**config)

        expr = coeff1 * i + coeff2 * j + coeff3 * k
        simplified = simplify(Sum(Sum(Sum(expr, (i, a, c)), (j, 1, m)), (k, 1, l)).doit())

        question = f"{template}\n\n$\\sum_{{k=1}}^{{{l}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{i={a}}}^{{{c}}} {latex(expr)}$"
        answer = (
            "**Answer:**\n"
            f"$\\sum_{{k=1}}^{{{l}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{i={a}}}^{{{c}}} {latex(expr)} = "
            # f"\\sum_{{k=1}}^{{{l}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{i={a}}}^{{{b}}} {latex(expr)} + "
            # f"\\sum_{{k=1}}^{{{l}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{i={b+1}}}^{{{c}}} {latex(expr)} = "
            f"{latex(simplified)}$"
        )

    return {"question": question, "answer": answer}

def generate(level, num_questions):
    return [generate_question(level) for _ in range(num_questions)]
