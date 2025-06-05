import random
from sympy import symbols, series, sin, cos, exp, log, tan, atan, sqrt, latex, diff, factorial
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

def taylor_remainder(f, a, n, x_val):
    """
    Calculates the Lagrange remainder (error estimation) of the Taylor series expansion
    of function f at point a up to degree n evaluated at x_val.
    """
    deriv = diff(f, x, n + 1)
    M = abs(deriv.subs(x, x_val))
    error_bound = M * abs(x_val - a)**(n + 1) / factorial(n + 1)
    return error_bound

QUESTION_TEMPLATES = [
    "Estimate the error of approximating ${}$ using its Taylor polynomial of degree {} at $x = {}$ centered at $x = {}$.",
    "Find the Lagrange remainder for the Taylor approximation of ${}$ at $x = {}$, degree {}, about $x = {}$.",
    "What is the error bound when approximating ${}$ by its degree {} Taylor polynomial centered at $x = {}$ evaluated at $x = {}$?",
    "Determine the maximum error when using a Taylor polynomial of degree {} for ${}$ centered at $x = {}$ at $x = {}$.",
    "Compute the error estimate of ${}$ using Taylor expansion up to degree {} around $x = {}$, evaluated at $x = {}$."
]

def generate_taylor_error_question(level):
    func_name, func_expr = random.choice(LEVELS[level])
    a = random.choice([0, 1]) if level < 6 else 0
    n = random.randint(3 + level // 2, 5 + level)
    x_val = round(random.uniform(a - 1, a + 1), 3)

    taylor_poly = series(func_expr, x, a, n).removeO()
    error_estimate = round(taylor_remainder(func_expr, a, n, x_val).evalf(), 3)

    # Choose a question template
    template = random.choice(QUESTION_TEMPLATES)
    question = template.format(func_name, n, x_val, a)
    question += "\n\n$$\n" + f"{func_name} \\approx " + latex(taylor_poly) + "\n$$"

    answer = f"**Answer:**\n\nThe estimated error bound is approximately:\n\n"
    answer += "$$\n" + latex(error_estimate) + "\n$$"

    return {"question": question, "answer": answer}

def generate(level, num_questions):
    return [generate_taylor_error_question(level) for _ in range(num_questions)]
