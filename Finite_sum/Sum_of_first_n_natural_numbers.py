import random
from sympy import symbols, summation, Rational, latex, simplify
from sympy.abc import i, j, k

# === Level Functions (Return question-answer pair as strings) ===

def level_1_single_positive():
    n = random.randint(5, 15)
    expr = i
    result = summation(expr, (i, 1, n))
    q = f"Evaluate the sum of first {n} natural numbers:\n\n$\\sum_{{i=1}}^{{{n}}} i$"
    a = f"**Answer:**\n${latex(simplify(result))}$"
    return q, a

def level_2_single_pos_neg():
    n = random.randint(5, 10)
    coeff = random.choice([1, -1, 2, -2, 3, -3])
    expr = coeff * i
    result = summation(expr, (i, 1, n))
    q = f"Evaluate the sum:\n\n$\\sum_{{i=1}}^{{{n}}} {latex(expr)}$"
    a = f"**Answer:**\n${latex(simplify(result))}$"
    return q, a

def level_3_single_frac():
    n = random.randint(3, 7)
    coeff = Rational(random.randint(-5, 5), random.randint(2, 6))
    expr = coeff * i
    result = summation(expr, (i, 1, n))
    q = f"Evaluate the fractional sum:\n\n$\\sum_{{i=1}}^{{{n}}} {latex(expr)}$"
    a = f"**Answer:**\n${latex(simplify(result))}$"
    return q, a

def level_4_double_positive():
    m = random.randint(2, 5)
    n = random.randint(2, 5)
    expr = i + j
    result = summation(summation(expr, (j, 1, n)), (i, 1, m))
    q = f"Evaluate the double sum:\n\n$\\sum_{{i=1}}^{{{m}}} \\sum_{{j=1}}^{{{n}}} (i + j)$"
    a = f"**Answer:**\n${latex(simplify(result))}$"
    return q, a

def level_5_double_pos_neg():
    m = random.randint(2, 5)
    n = random.randint(2, 5)
    expr = random.choice([i - j, -i + j, -i - j, 2*i - 3*j])
    result = summation(summation(expr, (j, 1, n)), (i, 1, m))
    q = f"Evaluate the double sum:\n\n$\\sum_{{i=1}}^{{{m}}} \\sum_{{j=1}}^{{{n}}} ({latex(expr)})$"
    a = f"**Answer:**\n${latex(simplify(result))}$"
    return q, a

def level_6_double_frac():
    m = random.randint(2, 3)
    n = random.randint(2, 3)
    coeff_i = Rational(random.randint(1, 4), random.randint(2, 5))
    coeff_j = Rational(random.randint(1, 4), random.randint(2, 5))
    expr = coeff_i*i + coeff_j*j
    result = summation(summation(expr, (j, 1, n)), (i, 1, m))
    q = f"Evaluate the fractional double sum:\n\n$\\sum_{{i=1}}^{{{m}}} \\sum_{{j=1}}^{{{n}}} ({latex(expr)})$"
    a = f"**Answer:**\n${latex(simplify(result))}$"
    return q, a

def level_7_triple_mixed():
    m = n = p = 2
    expr = Rational(1, 2)*i + Rational(-1, 3)*j + Rational(1, 4)*k
    result = summation(summation(summation(expr, (k, 1, p)), (j, 1, n)), (i, 1, m))
    q = f"Evaluate the triple sum:\n\n$\\sum_{{i=1}}^2 \\sum_{{j=1}}^2 \\sum_{{k=1}}^2 \\left(\\frac{{1}}{{2}}i - \\frac{{1}}{{3}}j + \\frac{{1}}{{4}}k\\right)$"
    a = f"**Answer:**\n${latex(simplify(result))}$"
    return q, a

# === Dispatcher ===

LEVEL_FUNCTIONS = {
    1: level_1_single_positive,
    2: level_2_single_pos_neg,
    3: level_3_single_frac,
    4: level_4_double_positive,
    5: level_5_double_pos_neg,
    6: level_6_double_frac,
    7: level_7_triple_mixed
}

# === Main Callable Function ===

def generate_question_answer_string(level: int, num_questions: int = 2) -> str:
    if level not in LEVEL_FUNCTIONS:
        raise ValueError("Level must be between 1 and 7.")
    
    func = LEVEL_FUNCTIONS[level]
    output = []
    for qid in range(1, num_questions + 1):
        q, a = func()
        output.append(f"**Q{qid}.** \n{q}\n\n{a}\n\n---")
    
    return "\n\n".join(output)
