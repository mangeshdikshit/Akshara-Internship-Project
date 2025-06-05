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

QUESTION_TEMPLATES = [
    "Find the Taylor series expansion of ${}$ about $x = {}$ up to {} terms.",
    "Compute the Taylor series of ${}$ centered at $x = {}$ including {} terms.",
    "Determine the {}-term Taylor expansion for ${}$ at $x = {}$.",
    "What is the Taylor polynomial of ${}$ about $x = {}$ up to order {}?",
    "Write down the Taylor expansion of ${}$ around $x = {}$ using {} terms."
]

def generate_taylor_question(level):
    func_name, func_expr = random.choice(LEVELS[level])
    a = random.choice([0, 1]) if level < 6 else 0  # Center of expansion
    n = random.randint(3 + level // 2, 5 + level)  # Terms in expansion

    taylor_expansion = series(func_expr, x, a, n).removeO()

    template = random.choice(QUESTION_TEMPLATES)
    question = template.format(func_name, a, n)
    question += "\n\n$$\n" + f"{func_name} \\approx " + latex(taylor_expansion) + "\n$$"

    answer = "**Answer:**\n\nThe Taylor expansion is:\n\n"
    answer += "$$\n" + latex(taylor_expansion) + "\n$$"

    return {"question": question, "answer": answer}

def generate(level, num_questions):
    return [generate_taylor_question(level) for _ in range(num_questions)]
