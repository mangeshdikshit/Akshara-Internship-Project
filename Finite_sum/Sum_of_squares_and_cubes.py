import random
from sympy import summation, Rational, latex
from sympy.abc import i, j, k

# === Level Functions (Return question + answer in formatted string) ===

def level_1_single_natural():
    n = random.randint(5, 15)
    choice = random.choice(["i", "i**2", "i**3"])
    expr = eval(choice)
    result = summation(expr, (i, 1, n))
    q = f"Evaluate:\n\n$\\sum_{{i=1}}^{{{n}}} {latex(expr)}$\n\n**Answer:**\n${latex(result)}$"
    return q

def level_2_single_neg():
    n = random.randint(5, 10)
    choice = random.choice(["i", "i**2", "i**3"])
    coeff = random.choice([-1, -2, -3])
    expr = coeff * eval(choice)
    result = summation(expr, (i, 1, n))
    q = f"Evaluate:\n\n$\\sum_{{i=1}}^{{{n}}} {latex(expr)}$\n\n**Answer:**\n${latex(result)}$"
    return q

def level_3_single_frac():
    n = random.randint(3, 7)
    choice = random.choice(["i", "i**2", "i**3"])
    coeff = Rational(random.randint(1, 4), random.randint(2, 5))
    expr = coeff * eval(choice)
    result = summation(expr, (i, 1, n))
    q = f"Evaluate the fractional sum:\n\n$\\sum_{{i=1}}^{{{n}}} {latex(expr)}$\n\n**Answer:**\n${latex(result)}$"
    return q

def level_4_double_natural():
    m, n = random.randint(2, 5), random.randint(2, 5)
    expr = random.choice([i + j, i**2 + j**2, i**3 + j**3])
    result = summation(summation(expr, (j, 1, n)), (i, 1, m))
    q = f"Evaluate:\n\n$\\sum_{{i=1}}^{{{m}}} \\sum_{{j=1}}^{{{n}}} {latex(expr)}$\n\n**Answer:**\n${latex(result)}$"
    return q

def level_5_double_neg():
    m, n = random.randint(2, 5), random.randint(2, 5)
    expr = random.choice([-i - j, -2*i + j, -i**2 - j**2])
    result = summation(summation(expr, (j, 1, n)), (i, 1, m))
    q = f"Evaluate:\n\n$\\sum_{{i=1}}^{{{m}}} \\sum_{{j=1}}^{{{n}}} {latex(expr)}$\n\n**Answer:**\n${latex(result)}$"
    return q

def level_6_double_frac():
    m, n = random.randint(2, 3), random.randint(2, 3)
    ci = Rational(random.randint(1, 4), random.randint(2, 5))
    cj = Rational(random.randint(1, 4), random.randint(2, 5))
    expr = ci*i + cj*j
    result = summation(summation(expr, (j, 1, n)), (i, 1, m))
    q = f"Evaluate the fractional double sum:\n\n$\\sum_{{i=1}}^{{{m}}} \\sum_{{j=1}}^{{{n}}} ({latex(expr)})$\n\n**Answer:**\n${latex(result)}$"
    return q

def level_7_triple_mixed():
    m = n = p = 2
    expr = Rational(1, 2)*i + Rational(-1, 3)*j + Rational(1, 4)*k
    result = summation(summation(summation(expr, (k, 1, p)), (j, 1, n)), (i, 1, m))
    q = f"Evaluate the triple sum:\n\n$\\sum_{{i=1}}^2 \\sum_{{j=1}}^2 \\sum_{{k=1}}^2 \\left({latex(expr)}\\right)$\n\n**Answer:**\n${latex(result)}$"
    return q

# === Dispatcher Function (returns combined string of all questions) ===

LEVEL_FUNCTIONS = {
    1: level_1_single_natural,
    2: level_2_single_neg,
    3: level_3_single_frac,
    4: level_4_double_natural,
    5: level_5_double_neg,
    6: level_6_double_frac,
    7: level_7_triple_mixed
}

def generate_questions(level: int, num_questions: int = 2) -> str:
    if level not in LEVEL_FUNCTIONS:
        raise ValueError("Level must be between 1 and 7.")
    func = LEVEL_FUNCTIONS[level]
    output = []
    for qid in range(1, num_questions + 1):
        qa = func()
        output.append(f"**Q{qid}.** \n{qa}\n\n---")
    return "\n\n".join(output)
