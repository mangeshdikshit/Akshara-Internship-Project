import random
from sympy import symbols, sin, cos, pi, integrate, simplify, latex, Piecewise, Abs
from sympy.abc import x, n

TEMPLATES = [
    "Find the Fourier sine and cosine coefficients for:\n\n{}",
    "Determine the values of $a_0$, $a_n$, and $b_n$ for the function:\n\n{}",
    "Compute the Fourier series coefficients of the function:\n\n{}",
    "Calculate the Fourier coefficients over the interval $[-\\pi, \\pi]$ for:\n\n{}",
    "What are the values of $a_0$, $a_n$, and $b_n$ for the given function:\n\n{}"
]

def random_constant():
    c = random.randint(1, 5)
    return c, f"$f(x) = {c}$ over $[-\\pi, \\pi]$"

def random_odd_linear():
    c = random.randint(1, 5)
    return c * x, f"$f(x) = {c}x$ (odd) over $[-\\pi, \\pi]$"

def random_even_abs():
    c = random.randint(1, 5)
    return c * Abs(x), f"$f(x) = {c}|x|$ (even) over $[-\\pi, \\pi]$"

def random_step():
    a, b = random.sample([1, 2, 3, -1, -2, -3], 2)
    expr = Piecewise((a, (x >= -pi) & (x < 0)), (b, (x >= 0) & (x <= pi)))
    desc = f"$f(x) = \\begin{{cases}} {a}, & -\\pi \\le x < 0 \\\\ {b}, & 0 \\le x \\le \\pi \\end{{cases}}$"
    return expr, desc

def random_sin():
    k = random.randint(1, 3)
    return sin(k * x), f"$f(x) = \\sin({k}x)$ over $[-\\pi, \\pi]$"

def random_abs_sin():
    k = random.randint(1, 3)
    return Abs(sin(k * x)), f"$f(x) = |\\sin({k}x)|$ over $[-\\pi, \\pi]$"

# Function category map
CATEGORIES = {
    'constant': random_constant,
    'odd_linear': random_odd_linear,
    'even_abs': random_even_abs,
    'step': random_step,
    'sin': random_sin,
    'abs_sin': random_abs_sin,
}

def generate_coefficients_question(level, used_desc):
    category = LEVELS[level]['type']
    if category == 'mixed':
        category = random.choice(list(CATEGORIES.keys()))

    while True:
        f, desc = CATEGORIES[category]()
        if desc not in used_desc:
            used_desc.add(desc)
            break

    # Compute a0, a1, b1 instead of general an, bn
    a0 = simplify((1 / pi) * integrate(f, (x, -pi, pi)))
    a1 = simplify((1 / pi) * integrate(f * cos(1 * x), (x, -pi, pi)))
    b1 = simplify((1 / pi) * integrate(f * sin(1 * x), (x, -pi, pi)))

    # If the expressions are too long, convert to decimals
    def shorten(expr):
        expr_latex = latex(expr)
        return expr.evalf(4) if len(expr_latex) > 60 else expr_latex

    a0_str = shorten(a0)
    a1_str = shorten(a1)
    b1_str = shorten(b1)

    # Prepare question and answer
    template = random.choice(TEMPLATES)
    question = template.format(desc)
    answer = f"**Answer:**\n\n$a_0 = {a0_str}$  \n$a_1 = {a1_str}$  \n$b_1 = {b1_str}$"
    return question, answer


def get_fourier_coefficient_questions(level, num_questions):
    used = set()
    return [
        {'question': q, 'answer': a}
        for _ in range(num_questions)
        for q, a in [generate_coefficients_question(level, used)]
    ]

# Level configuration
LEVELS = {
    1: {'type': 'mixed'},
    2: {'type': 'mixed'},
    3: {'type': 'mixed'},
    4: {'type': 'mixed'},
    5: {'type': 'mixed'},
    6: {'type': 'mixed'},
    7: {'type': 'mixed'}
}
