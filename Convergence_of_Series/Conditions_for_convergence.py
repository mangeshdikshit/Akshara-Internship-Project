import random
from sympy import symbols, Sum, Rational, simplify, latex, oo, factorial
from sympy.abc import i

# Level configuration for types of series and convergence conditions
LEVELS = {
    1: {'type': 'p_series', 'description': "p-series: Sum of 1/n^p converges if p > 1"},
    2: {'type': 'geometric', 'description': "Geometric series: Sum of r^n converges if |r| < 1"},
    3: {'type': 'alternating', 'description': "Alternating series test: converges if terms decrease to 0"},
    4: {'type': 'factorial', 'description': "Factorial denominator leads to convergence"},
    5: {'type': 'harmonic', 'description': "Harmonic series diverges (p = 1)"},
    6: {'type': 'comparison', 'description': "Comparison test with p-series"},
    7: {'type': 'mixed', 'description': "Mixed types chosen randomly"},
}

def generate_series(level_type):
    if level_type == 'p_series':
        p_float = round(random.uniform(0.5, 3), 3)
        expr = 1 / i**Rational(str(p_float))
        conclusion = "converges" if p_float > 1 else "diverges"
        reason = f"Because it is a p-series with p = {p_float}."
    
    elif level_type == 'geometric':
        r_float = round(random.uniform(0.1, 2), 3)
        expr = r_float**i
        conclusion = "converges" if abs(r_float) < 1 else "diverges"
        reason = f"Because it is a geometric series with common ratio r = {r_float}."
    
    elif level_type == 'alternating':
        p_float = round(random.uniform(0.5, 2.5), 3)
        expr = (-1)**i / i**Rational(str(p_float))
        conclusion = "converges" if p_float > 0 else "diverges"
        reason = f"Alternating series with terms decreasing to zero (p = {p_float})."
    
    elif level_type == 'factorial':
        expr = 1 / factorial(i)
        conclusion = "converges"
        reason = "Factorial in the denominator causes rapid decay, ensuring convergence."
    
    elif level_type == 'harmonic':
        expr = 1 / i
        conclusion = "diverges"
        reason = "Harmonic series diverges (p = 1)."
    
    elif level_type == 'comparison':
        p_float = round(random.uniform(0.9, 1.1), 3)
        expr = 1 / (i * (i + 1)**Rational(str(p_float)))
        conclusion = "converges" if p_float > 1 else "diverges"
        reason = "Comparison test with p-series near p = 1." 
    
    elif level_type == 'mixed':
        return generate_series(random.choice(['p_series', 'geometric', 'factorial']))
    
    return expr, conclusion, reason

def generate_question(level):
    config = LEVELS[level]
    expr, conclusion, reason = generate_series(config['type'])
    summation = Sum(expr, (i, 1, oo)) 
    
    templates = [
        "Determine whether the following infinite series converges or diverges:",
        "Is the infinite series below convergent or divergent? Justify your answer:",
        "Based on known convergence tests, state whether the series converges or diverges:",
        "Analyze the convergence behavior of the given series:",
        "Using your understanding of convergence criteria, evaluate this series:",
        "Does the following sum converge? Support your answer with reasoning:",
        "Classify the following series as convergent or divergent:"
    ]

    question_latex = random.choice(templates) + "\n\n"
    question_latex += "$\n" + latex(summation) + "\n$\n\n"
    question_latex += f"*Hint: {config['description']}*\n"

    answer_latex = f"**Answer:** The series **{conclusion}**. {reason}"

    return question_latex, answer_latex

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        q, a = generate_question(level)
        questions.append({"question": q, "answer": a})
    return questions
