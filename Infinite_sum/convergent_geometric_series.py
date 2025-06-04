import random
from sympy import symbols, latex, S
from sympy.abc import n

# === Helper to compute convergent geometric sum ===

def convergent_sum(a, r):
    if abs(r) < 1:
        return a / (1 - r)
    return "Diverges"

# === Individual Level Functions ===

def level_1_simple_integer_ratio():
    a = random.randint(1, 10)
    r = random.choice([S(1)/2, S(1)/3])
    expr = a * r**n
    s = convergent_sum(a, r)
    q = f"Evaluate the infinite sum: $\\sum_{{n=0}}^\\infty {latex(expr)}$"
    a_str = f"**Answer:** ${latex(s)}$"
    return q, a_str

def level_2_negative_ratio():
    a = random.randint(1, 10)
    r = random.choice([-S(1)/2, -S(1)/3])
    expr = a * r**n
    s = convergent_sum(a, r)
    q = f"Evaluate the infinite sum: $\\sum_{{n=0}}^\\infty {latex(expr)}$"
    a_str = f"**Answer:** ${latex(s)}$"
    return q, a_str

def level_3_fractional_start():
    a = S(random.randint(1, 10)) / random.randint(2, 6)
    r = S(random.randint(1, 7)) / random.randint(4, 6)
    expr = a * r**n
    s = convergent_sum(a, r)
    q = f"Evaluate the infinite sum: $\\sum_{{n=0}}^\\infty {latex(expr)}$"
    a_str = f"**Answer:** ${latex(s)}$"
    return q, a_str

def level_4_including_sign_alternation():
    a = random.randint(1, 10)
    r = -S(1)/2
    expr = a * r**n
    s = convergent_sum(a, r)
    q = f"Evaluate the alternating geometric series: $\\sum_{{n=0}}^\\infty {latex(expr)}$"
    a_str = f"**Answer:** ${latex(s)}$"
    return q, a_str

def level_5_index_shifted():
    a = random.randint(1, 10)
    r = S(1)/3
    shift = random.randint(1, 5)
    expr = a * r**(n - shift)
    s = convergent_sum(a * r**(-shift), r)
    q = f"Evaluate the infinite sum (index starts at {shift}): $\\sum_{{n={shift}}}^\\infty {latex(expr)}$"
    a_str = f"**Answer:** ${latex(s)}$"
    return q, a_str

def level_6_mixed_fractional_negative():
    a = S(random.randint(1, 10)) / random.randint(2, 6)
    r = -S(random.randint(1, 15)) / random.randint(3, 6)
    expr = a * r**n
    s = convergent_sum(a, r)
    q = f"Evaluate the infinite sum: $\\sum_{{n=0}}^\\infty {latex(expr)}$"
    a_str = f"**Answer:** ${latex(s)}$"
    return q, a_str

def level_7_large_denominator_ratio():
    a = 1
    r = S(1)/10
    expr = a * r**n
    s = convergent_sum(a, r)
    q = f"Evaluate the infinite sum with small common ratio: $\\sum_{{n=0}}^\\infty {latex(expr)}$"
    a_str = f"**Answer:** ${latex(s)}$"
    return q, a_str

# === Function Pool by Level ===

level_funcs = {
    1: [level_1_simple_integer_ratio],
    2: [level_2_negative_ratio],
    3: [level_3_fractional_start],
    4: [level_4_including_sign_alternation],
    5: [level_5_index_shifted],
    6: [level_6_mixed_fractional_negative],
    7: [level_7_large_denominator_ratio]
}

# === Main Interface ===

def generate_geometric_series(level, num_questions):
    if level not in level_funcs:
        raise ValueError("Level must be between 1 and 7.")
    
    func_choices = level_funcs[level]
    questions = []

    for _ in range(num_questions):
        func = random.choice(func_choices)
        q, a = func()
        questions.append({"question": q, "answer": a})

    return questions
