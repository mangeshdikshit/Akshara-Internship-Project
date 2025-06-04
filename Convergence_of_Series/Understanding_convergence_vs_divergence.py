import random
from sympy import symbols, Sum, Rational, simplify, latex, oo, factorial
from sympy.abc import i

# Level setup
LEVELS = {
    1: {'type': 'p_series'},
    2: {'type': 'geometric'},
    3: {'type': 'alternating'},
    4: {'type': 'factorial'},
    5: {'type': 'harmonic'},
    6: {'type': 'comparison'},
    7: {'type': 'mixed'}
}

def generate_series(level_type):
    if level_type == 'p_series':
        p = round(random.uniform(0.5, 3), 3)
        expr = 1 / i**Rational(str(p))
        conclusion = "converges" if p > 1 else "diverges"
        reason = f"This is a p-series with p = {p}."
    
    elif level_type == 'geometric':
        r = round(random.uniform(0.1, 2), 3)
        expr = r**i
        if abs(r) < 1:
            conclusion = "converges"
        else:
            conclusion = "diverges"
        reason = f"This is a geometric series with ratio r = {r}."
    
    elif level_type == 'alternating':
        p = round(random.uniform(0.5, 2.5), 3)
        expr = (-1)**i / i**Rational(str(p))
        conclusion = "converges" if p > 0 else "diverges"
        reason = f"This is an alternating series with decreasing terms (p = {p})."
    
    elif level_type == 'factorial':
        expr = 1 / factorial(i)
        conclusion = "converges"
        reason = "Factorial in denominator leads to rapid decay."
    
    elif level_type == 'harmonic':
        expr = 1 / i
        conclusion = "diverges"
        reason = "Harmonic series diverges (p = 1)."
    
    elif level_type == 'comparison':
        p = round(random.uniform(0.9, 1.1), 3)
        expr = 1 / (i * (i + 1)**Rational(str(p)))
        conclusion = "diverges" if p <= 1 else "converges"
        reason = f"Compare with p-series behavior around p = 1."
    
    elif level_type == 'mixed':
        return generate_series(random.choice(['p_series', 'geometric', 'factorial']))
    
    return expr, conclusion, reason

def generate_question(level):
    config = LEVELS[level]
    expr, conclusion, reason = generate_series(config['type'])
    summation = Sum(expr, (i, 1, oo))
    
    templates = [
        "Determine whether the following series converges or diverges:",
        "Analyze the convergence of this infinite series:",
        "Decide if the given series converges or diverges:",
        "Examine the following series and state whether it converges or diverges:",
        "Using appropriate tests, determine the convergence behavior of the series:"
    ]
    
    question_latex = random.choice(templates) + "\n\n"
    question_latex += "$\n" + latex(summation) + "\n$"

    answer_latex = f"**Answer:** The series **{conclusion}**. {reason}"

    return question_latex, answer_latex

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        q, a = generate_question(level)
        questions.append({"question": q, "answer": a})
    return questions
