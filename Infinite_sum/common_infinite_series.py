import random
from sympy import symbols, Sum, oo, latex, S
from sympy.abc import n

# === Helper to generate convergent geometric series ===
def convergent_sum(a, r):
    if abs(r) < 1:
        return a / (1 - r)
    return "Diverges"

# === Harmonic sum function (using explicit sum) ===
def harmonic_sum(n_terms):
    k = symbols('k', integer=True)
    return Sum(1/k, (k, 1, n_terms)).doit()

# === Level-based question generators ===

# --- Geometric Series Levels 1 to 4 ---
def level_1_simple_integer_ratio():
    a = random.randint(1, 10)
    r = random.choice([S(1)/2, S(1)/3])
    expr = a * r**n
    s = convergent_sum(a, r)
    return (
        f"Evaluate the infinite sum: $\\sum_{{n=0}}^\\infty {latex(expr)}$",
        f"**Answer:** ${latex(s)}$"
    )

def level_2_negative_ratio():
    a = random.randint(1, 10)
    r = random.choice([-S(1)/2, -S(1)/3])
    expr = a * r**n
    s = convergent_sum(a, r)
    return (
        f"Evaluate the infinite sum: $\\sum_{{n=0}}^\\infty {latex(expr)}$",
        f"**Answer:** ${latex(s)}$"
    )

def level_3_fractional_start():
    a = S(random.randint(1, 10)) / random.randint(2, 6)
    r = S(random.randint(1, 6)) / random.randint(4, 6)
    expr = a * r**n
    s = convergent_sum(a, r)
    return (
        f"Evaluate the infinite sum: $\\sum_{{n=0}}^\\infty {latex(expr)}$",
        f"**Answer:** ${latex(s)}$"
    )

def level_4_including_sign_alternation():
    a = random.randint(1, 10)
    r = -S(1)/2
    expr = a * r**n
    s = convergent_sum(a, r)
    return (
        f"Evaluate the alternating geometric series: $\\sum_{{n=0}}^\\infty {latex(expr)}$",
        f"**Answer:** ${latex(s)}$"
    )

# --- Harmonic Series Levels 5 to 7 ---
def level_5_harmonic_sum_small():
    n_terms = random.randint(3, 10)
    return (
        f"Calculate the finite harmonic sum: $H_{{{n_terms}}} = \\sum_{{k=1}}^{{{n_terms}}} \\frac{{1}}{{k}}$",
        f"**Answer:** ${latex(harmonic_sum(n_terms))}$"
    )

def level_6_harmonic_sum_large():
    n_terms = random.randint(8, 10)
    return (
        f"Calculate the finite harmonic sum: $H_{{{n_terms}}} = \\sum_{{k=1}}^{{{n_terms}}} \\frac{{1}}{{k}}$",
        f"**Answer:** ${latex(harmonic_sum(n_terms))}$"
    )

def level_7_harmonic_divergence():
    return (
        "Does the infinite harmonic series $\\sum_{n=1}^\\infty \\frac{1}{n}$ converge or diverge?",
        "**Answer:** It diverges."
    )

# === Unified function to get questions ===

def get_convergent_series_questions(level: int, num_questions: int):
    level_funcs = {
        1: [level_1_simple_integer_ratio],
        2: [level_2_negative_ratio],
        3: [level_3_fractional_start],
        4: [level_4_including_sign_alternation],
        5: [level_5_harmonic_sum_small],
        6: [level_6_harmonic_sum_large],
        7: [level_7_harmonic_divergence],
    }

    if level not in level_funcs:
        raise ValueError("Level must be between 1 and 7")

    func_choices = level_funcs[level]
    questions = []

    for _ in range(num_questions):
        func = random.choice(func_choices)
        q, a = func()
        questions.append({"question": q, "answer": a})

    return questions
