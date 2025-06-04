import random
from sympy import symbols, summation, Rational, latex, simplify
from sympy.abc import i

# === Random Coefficient Generator ===

def gen_random_coeff():
    if random.random() < 0.7:
        return random.choice([x for x in range(-5, 6) if x != 0])
    else:
        num = random.randint(1, 5)
        den = random.randint(2, 6)
        coeff = Rational(num, den)
        return -coeff if random.random() < 0.5 else coeff

# === Level Functions ===

def poly_level(degree, n_range):
    n = random.randint(*n_range)
    expr = sum(gen_random_coeff() * i**d for d in range(degree, -1, -1))
    result = summation(expr, (i, 1, n))
    question = f"Evaluate the sum:\n\n$\\sum_{{i=1}}^{{{n}}} \\left({latex(expr)}\\right)$"
    answer = f"**Answer:**\n${latex(simplify(result))}$"
    return question, answer

# === Level Dispatcher ===

def get_poly_level_function(level):
    if level == 1:
        return lambda: poly_level(1, (4, 10))  # simple linear
    elif level == 2:
        return lambda: poly_level(1, (8, 15))  # longer linear
    elif level == 3:
        return lambda: poly_level(2, (4, 10))  # basic quadratic
    elif level == 4:
        return lambda: poly_level(2, (6, 12))  # longer quadratic
    elif level == 5:
        return lambda: poly_level(3, (3, 7))   # cubic
    elif level == 6:
        return lambda: poly_level(3, (5, 8))   # more complex cubic
    elif level == 7:
        return lambda: poly_level(4, (3, 6))   # quartic
    else:
        raise ValueError("Level must be between 1 and 7")

# === Generator Function ===

def generate_general_poly_sums(level, num_questions):
    func = get_poly_level_function(level)
    output = []
    for qid in range(1, num_questions + 1):
        q, a = func()
        output.append(f"**Q{qid}**. \n{q}\n\n{a}\n\n---")
    return "\n\n".join(output)

# Example usage:
# print(generate_general_poly_sums(level=3, num_questions=2))
