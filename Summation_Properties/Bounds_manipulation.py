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
    "Use the bounds manipulation property of summation to rewrite and evaluate:",
    "Rewrite the summation with shifted bounds and simplify:",
    "Apply index shifting to transform and evaluate the summation:",
    "Evaluate the summation by shifting its index appropriately:",
    "Change the index variable and limits, then compute the sum:"
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

    # Single summation: Levels 1–3
    if level in [1, 2, 3]:
        a = random.randint(1, 4)
        b = a + random.randint(3, 5)
        shift = random.randint(1, 3)

        coeff = get_random_coeff(**config)
        expr = coeff * i
        new_var = symbols('j')

        sum_original = Sum(expr, (i, a, b))
        shifted_expr = expr.subs(i, new_var - shift)
        sum_shifted = Sum(shifted_expr, (new_var, a + shift, b + shift))
        simplified = simplify(sum_original.doit())

        question = (
            f"{template}\n\n"
            f"$\\sum_{{i={a}}}^{{{b}}} {latex(expr)}$"
        )
        answer = (
            f"**Answer:**\n"
            f"$\\sum_{{i={a}}}^{{{b}}} {latex(expr)} = "
            f"\\sum_{{j={a + shift}}}^{{{b + shift}}} {latex(shifted_expr)} = "
            f"{latex(simplified)}$"
        )
    
    # Double summation: Levels 4–6
    elif level in [4, 5, 6]:
        a1 = random.randint(1, 4)
        b1 = a1 + random.randint(3, 5)
        a2 = random.randint(1, 3)
        b2 = a2 + random.randint(2, 4)
        s1 = random.randint(1, 3)
        s2 = random.randint(1, 3)

        c1 = get_random_coeff(**config)
        c2 = get_random_coeff(**config)
        expr = c1 * i + c2 * j

        new_i, new_j = symbols('m n')
        sum_original = Sum(Sum(expr, (i, a1, b1)), (j, a2, b2))
        shifted_expr = expr.subs({i: new_i - s1, j: new_j - s2})
        sum_shifted = Sum(Sum(shifted_expr, (new_i, a1 + s1, b1 + s1)), (new_j, a2 + s2, b2 + s2))
        simplified = simplify(sum_original.doit())

        question = (
            f"{template}\n\n"
            f"$\\sum_{{j={a2}}}^{{{b2}}} \\sum_{{i={a1}}}^{{{b1}}} {latex(expr)}$"
        )
        answer = (
            f"**Answer:**\n"
            f"$\\sum_{{j={a2}}}^{{{b2}}} \\sum_{{i={a1}}}^{{{b1}}} {latex(expr)} = "
            f"\\sum_{{n={a2 + s2}}}^{{{b2 + s2}}} \\sum_{{m={a1 + s1}}}^{{{b1 + s1}}} "
            f"{latex(shifted_expr)} = {latex(simplified)}$"
        )

    # Triple summation: Level 7
    else:
        a1 = random.randint(1, 3)
        b1 = a1 + random.randint(2, 4)
        a2 = random.randint(1, 3)
        b2 = a2 + random.randint(2, 4)
        a3 = random.randint(1, 2)
        b3 = a3 + random.randint(2, 3)
        s1 = random.randint(1, 2)
        s2 = random.randint(1, 2)
        s3 = random.randint(1, 2)

        c1 = get_random_coeff(**config)
        c2 = get_random_coeff(**config)
        c3 = get_random_coeff(**config)
        expr = c1 * i + c2 * j + c3 * k

        m, n, p = symbols('m n p')
        sum_original = Sum(Sum(Sum(expr, (i, a1, b1)), (j, a2, b2)), (k, a3, b3))
        shifted_expr = expr.subs({i: m - s1, j: n - s2, k: p - s3})
        sum_shifted = Sum(Sum(Sum(shifted_expr, (m, a1 + s1, b1 + s1)), (n, a2 + s2, b2 + s2)), (p, a3 + s3, b3 + s3))
        simplified = simplify(sum_original.doit())

        question = (
            f"{template}\n\n"
            f"$\\sum_{{k={a3}}}^{{{b3}}} \\sum_{{j={a2}}}^{{{b2}}} \\sum_{{i={a1}}}^{{{b1}}} {latex(expr)}$"
        )
        answer = (
            f"**Answer:**\n"
            f"$\\sum_{{k={a3}}}^{{{b3}}} \\sum_{{j={a2}}}^{{{b2}}} \\sum_{{i={a1}}}^{{{b1}}} {latex(expr)} = "
            # f"\\sum_{{p={a3 + s3}}}^{{{b3 + s3}}} \\sum_{{n={a2 + s2}}}^{{{b2 + s2}}} "
            # f"\\sum_{{m={a1 + s1}}}^{{{b1 + s1}}} {latex(shifted_expr)} = 
            f"{latex(simplified)}$"
        )

    return {"question": question, "answer": answer}

def generate(level, num_questions):
    return [generate_question(level) for _ in range(num_questions)]
