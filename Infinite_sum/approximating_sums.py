import random
from sympy import symbols, S, Sum, oo, latex

n = symbols('n', integer=True, positive=True)

# === Helper: partial sum of geometric series ===
def partial_sum_geometric(a, r, k):
    if r == 1:
        return a * (k + 1)
    else:
        return a * (1 - r**(k + 1)) / (1 - r)

# === Level Generators for Approximating Sums Using Partial Sums ===

def partial_sum_geom_question():
    a = random.randint(1, 5)
    r = random.choice([S(1)/2, S(1)/3])
    k = random.randint(3, 6)
    expr = a * r**n
    partial_sum = partial_sum_geometric(a, r, k)
    q = f"Find the partial sum of the geometric series \n\n $\\sum_{{n=0}}^\\infty {latex(expr)}$ \n\n up to {k} terms (i.e., $S_{{{k}}}$)."
    a_str = f"**Answer:** $S_{{{k}}} = {latex(partial_sum)}$"
    return q, a_str

def partial_sum_harmonic_question():
    k = random.randint(4, 7)
    q = f"Find the partial sum of the harmonic series \n\n $\\sum_{{n=1}}^\\infty \\frac{{1}}{{n}}$ \n\n up to {k} terms (i.e., $S_{{{k}}}$)."
    a_str = f"**Answer:** $S_{{{k}}} = \\sum_{{n=1}}^{k} \\frac{{1}}{{n}}$ (approximate numerically if needed)."
    return q, a_str

def partial_sum_alternating_geom_question():
    a = random.randint(1, 3)
    r = S(-1)/2
    k = random.randint(3, 6)
    expr = a * r**n
    partial_sum = partial_sum_geometric(a, r, k)
    q = f"Find the partial sum of the alternating geometric series \n\n $\\sum_{{n=0}}^\\infty {latex(expr)}$ \n\n up to {k} terms (i.e., $S_{{{k}}}$)."
    a_str = f"**Answer:** $S_{{{k}}} = {latex(partial_sum)}$"
    return q, a_str

def partial_sum_power_series_question():
    x = random.choice([S(1)/2, S(1)/3])
    k = random.randint(3, 5)
    expr = n * x**n
    q = f"Find the partial sum of the series \n\n $\\sum_{{n=1}}^\\infty n \\left({latex(x)}\\right)^n$ \n\n up to {k} terms (i.e., $S_{{{k}}}$)."
    a_str = f"**Answer:** $S_{{{k}}} = \\sum_{{n=1}}^{k} n \\left({latex(x)}\\right)^n$ (evaluate numerically if needed)."
    return q, a_str

# === Return Q&A Based on Level and Question Count ===

def get_partial_sums_questions(level: int, num_questions: int):
    generators_by_level = {
        1: [partial_sum_geom_question],
        2: [partial_sum_harmonic_question],
        3: [partial_sum_alternating_geom_question],
        4: [partial_sum_power_series_question],
        5: [partial_sum_geom_question, partial_sum_harmonic_question],
        6: [partial_sum_geom_question, partial_sum_harmonic_question, partial_sum_alternating_geom_question],
        7: [partial_sum_geom_question, partial_sum_harmonic_question, partial_sum_alternating_geom_question, partial_sum_power_series_question],
    }

    if level not in generators_by_level:
        raise ValueError("Level must be between 1 and 7.")

    generators = generators_by_level[level]
    results = []
    for _ in range(num_questions):
        func = random.choice(generators)
        q, a = func()
        results.append({"question": q, "answer": a})
    
    return results
