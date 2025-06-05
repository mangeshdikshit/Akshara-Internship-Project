import random
from sympy import symbols, series, sin, cos, exp, log, tan, atan, sqrt, latex
from sympy.abc import x

# Define function levels for increasing difficulty (all expansions about 0 for Maclaurin)
LEVELS = {
    1: [("e^x", exp(x))],
    2: [("sin(x)", sin(x)), ("cos(x)", cos(x))],
    3: [("ln(1+x)", log(1 + x))],
    4: [("1/(1+x)", 1 / (1 + x))],
    5: [("sqrt(1+x)", sqrt(1 + x))],
    6: [("tan(x)", tan(x))],
    7: [("arctan(x)", atan(x))]
}

# Fresh question templates that do NOT include the answer/expansion
QUESTION_TEMPLATES = [
    "Using Maclaurin series, expand ${}$ up to {} non-zero terms.",
    "What is the Maclaurin series (about $x=0$) for ${}$ including {} terms?",
    "Using power series, find the Maclaurin expansion of ${}$ with {} terms.",
    "Derive the first {} terms of the Maclaurin series for ${}$.",
    "Find the first {} terms in the Maclaurin expansion of ${}$ about $x = 0$."
]

def generate_maclaurin_question(level):
    func_name, func_expr = random.choice(LEVELS[level])
    a = 0  # Maclaurin series is always about 0
    n = random.randint(3 + level // 2, 5 + level)

    maclaurin_expansion = series(func_expr, x, a, n).removeO()

    template = random.choice(QUESTION_TEMPLATES)

    # Determine argument order based on template style
    if '{}' in template and template.index('{}') < template.rindex('{}'):
        question = template.format(n, func_name)
    else:
        question = template.format(func_name, n)

    answer = f"**Answer:**\n\nThe Maclaurin expansion is:\n\n"
    answer += "$$\n" + f"{func_name} \\approx " + latex(maclaurin_expansion) + "\n$$"

    return {"question": question, "answer": answer}

def generate(level, num_questions):
    return [generate_maclaurin_question(level) for _ in range(num_questions)]
