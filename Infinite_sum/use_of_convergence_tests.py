import random
from sympy import symbols, S, latex
from sympy.abc import n

# === Basic Convergence Test Generators (Grouped by Level) ===

def level_1_geometric_ratio():
    r = random.choice([S(1)/2, S(-1)/3, S(2)/3, S(-3)/2])
    expr = r**n
    series_str = f"\\sum_{{n=0}}^\\infty {latex(expr)}"
    q = f"Determine if the series \n\n ${series_str}$ \n\n converges or diverges."
    if abs(r) < 1:
        ans = "Converges (since the common ratio $|r| < 1$)."
    else:
        ans = "Diverges (since the common ratio $|r| \\geq 1$)."
    a_str = f"**Answer:** {ans}"
    return q, a_str

def level_2_p_series():
    p = random.choice([S(1)/2, 1, 3/2, 2])
    expr = 1 / n**p
    series_str = f"\\sum_{{n=1}}^\\infty \\frac{{1}}{{n^{latex(p)}}}"
    q = f"Determine if the series \n\n ${series_str}$ \n\n converges or diverges."
    if p > 1:
        ans = f"Converges (p-series with $p = {latex(p)} > 1$)."
    else:
        ans = f"Diverges (p-series with $p = {latex(p)} \\leq 1$)."
    a_str = f"**Answer:** {ans}"
    return q, a_str

def level_3_divergence_nth_term():
    term_choice = random.choice([S(1), (-1)**n, 2])
    series_str = f"\\sum_{{n=1}}^\\infty {latex(term_choice)}"
    q = f"Determine if the series \n\n ${series_str}$ \n\n converges or diverges."
    a_str = "**Answer:** Diverges (terms do not tend to zero, so series diverges by the divergence test)."
    return q, a_str

def level_4_alternating_series():
    expr = (-1)**n / (n + 1)
    series_str = f"\\sum_{{n=1}}^\\infty {latex(expr)}"
    q = f"Determine if the series \n\n ${series_str}$ \n\n converges or diverges."
    a_str = "**Answer:** Converges (alternating series with terms decreasing to zero)."
    return q, a_str

def level_5_borderline_p_series():
    # Close to the convergence boundary for p-series
    p = S(1) + S(1)/10  # slightly > 1
    expr = 1 / n**p
    series_str = f"\\sum_{{n=1}}^\\infty \\frac{{1}}{{n^{latex(p)}}}"
    q = f"Determine if the series \n\n ${series_str}$ \n\n converges or diverges."
    a_str = f"**Answer:** Converges (p-series with $p = {latex(p)} > 1$)."
    return q, a_str

def level_6_geometric_edge_case():
    # r = 1 or r = -1: diverges
    r = random.choice([1, -1])
    expr = r**n
    series_str = f"\\sum_{{n=0}}^\\infty {latex(expr)}"
    q = f"Determine if the geometric series \n\n ${series_str}$ \n\n converges or diverges."
    a_str = "**Answer:** Diverges (common ratio $|r| = 1$, so the series diverges)."
    return q, a_str

def level_7_mixed_behavior():
    # A combination of convergence types (e.g. alternating + divergent)
    expr = (-1)**n * n / (n + 1)
    series_str = f"\\sum_{{n=1}}^\\infty {latex(expr)}"
    q = f"Determine if the series \n\n ${series_str}$ \n\n converges or diverges."
    a_str = "**Answer:** Diverges (although it is alternating, terms do not decrease to 0)."
    return q, a_str

# === Function Pool by Level ===

level_funcs = {
    1: [level_1_geometric_ratio],
    2: [level_2_p_series],
    3: [level_3_divergence_nth_term],
    4: [level_4_alternating_series],
    5: [level_5_borderline_p_series],
    6: [level_6_geometric_edge_case],
    7: [level_7_mixed_behavior]
}

# === Main Interface ===

def generate_convergence_tests(level, num_questions):
    if level not in level_funcs:
        raise ValueError("Level must be between 1 and 7.")
    
    func_choices = level_funcs[level]
    questions = []

    for _ in range(num_questions):
        func = random.choice(func_choices)
        q, a = func()
        questions.append({"question": q, "answer": a})

    return questions
