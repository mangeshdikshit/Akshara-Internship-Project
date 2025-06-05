import random
from sympy import series, sin, cos, exp, log, tan, atan, sqrt, latex
from sympy.abc import x

# Define function levels for increasing difficulty
LEVELS = {
    1: [("e^x", exp(x))],
    2: [("sin(x)", sin(x)), ("cos(x)", cos(x))],
    3: [("ln(1+x)", log(1 + x))],
    4: [("1/(1+x)", 1 / (1 + x))],
    5: [("sqrt(1+x)", sqrt(1 + x))],
    6: [("tan(x)", tan(x))],
    7: [("arctan(x)", atan(x))]
}

# More instructional / application-oriented templates
QUESTION_TEMPLATES = [
    "Use Taylor's theorem to expand ${}$ about $x = {}$ using {} terms.",
    "Approximate the function ${}$ near $x = {}$ with a Taylor polynomial of {} terms.",
    "Using {} terms, write the Taylor expansion of ${}$ centered at $x = {}$.",
    "Construct the {}-term Taylor polynomial for ${}$ around $x = {}$.",
    "Generate the Taylor series of ${}$ expanded about $x = {}$ up to {} terms."
]

def generate_taylor_question(level):
    func_name, func_expr = random.choice(LEVELS[level])
    a = random.choice([0, 1]) if level < 6 else 0  # Center of expansion
    n = random.randint(3 + level // 2, 5 + level)  # Number of terms

    taylor_expansion = series(func_expr, x, a, n).removeO()

    template = random.choice(QUESTION_TEMPLATES)

    # Adjust argument order for templates that start with number first
    if template.startswith("Using") or template.startswith("Construct") or template.startswith("Generate"):
        question = template.format(n, func_name, a)
    else:
        question = template.format(func_name, a, n)

    answer = "**Answer:**\n\nThe Taylor expansion is:\n\n"
    answer += "$$\n" + f"{func_name} \\approx " + latex(taylor_expansion) + "\n$$"

    return {"question": question, "answer": answer}

def generate(level, num_questions):
    return [generate_taylor_question(level) for _ in range(num_questions)]
