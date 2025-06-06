import random
from sympy import symbols, sin, cos, exp, Abs, simplify, latex, integrate, Piecewise, pi
from sympy.abc import x, n

QUESTION_TEMPLATES = [
    "Find the Fourier series of the periodic function:\n\n{}",
    "Determine the Fourier coefficients $a_0$, $a_n$, and $b_n$ for the function:\n\n{}",
    "Given the periodic function below, compute its Fourier series:\n\n{}",
    "Compute the Fourier series representation for:\n\n{}",
    "Find the expressions for $a_0$, $a_n$, and $b_n$ for this function:\n\n{}"
]

def random_step():
    choice = random.choice([1, -1])
    return Piecewise((choice, (x >= -pi) & (x < 0)), (-choice, (x >= 0) & (x <= pi))), \
        f"$f(x) = \\begin{{cases}} {choice}, & -\\pi \\le x < 0 \\\\ {-choice}, & 0 \\le x \\le \\pi \\end{{cases}}$"

def random_linear():
    coef = random.randint(1, 5)
    return coef * x, f"$f(x) = {coef}x$ over $[-\\pi, \\pi]$"

def random_triangle():
    coef = random.randint(1, 5)
    return coef * Abs(x), f"$f(x) = {coef}|x|$ over $[-\\pi, \\pi]$"

def random_halfwave():
    return Piecewise((sin(x), (x >= 0) & (x <= pi)), (0, (x > -pi) & (x < 0))), \
        "$f(x) = \\begin{cases} \\sin(x), & 0 \\le x \\le \\pi \\\\ 0, & -\\pi < x < 0 \\end{cases}$"

def random_abs_sin():
    return Abs(random.choice([sin(x), cos(x)])), \
        "$f(x) = |\\sin(x)|$ or $|\\cos(x)|$ over $[-\\pi, \\pi]$"

# Category generators
CATEGORY_FUNCTIONS = [random_step, random_linear, random_triangle, random_halfwave, random_abs_sin]

def generate_periodic_fourier_question(level, used_descriptions):
    while True:
        category = random.choice(CATEGORY_FUNCTIONS[:min(len(CATEGORY_FUNCTIONS), level + 1)])
        f, desc = category()
        if desc not in used_descriptions:
            used_descriptions.add(desc)
            break

    # Compute a0 and only first coefficient for an and bn (e.g., n = 1)
    a0_val = simplify((1 / pi) * integrate(f, (x, -pi, pi)))
    an_val = simplify((1 / pi) * integrate(f * cos(1 * x), (x, -pi, pi)))
    bn_val = simplify((1 / pi) * integrate(f * sin(1 * x), (x, -pi, pi)))

    template = random.choice(QUESTION_TEMPLATES)
    question = template.format(desc)

    answer = (
        f"**Answer:**\n\n"
        f"$a_0 = {latex(a0_val)}$  \n"
        f"$a_1 = {latex(an_val)}$  \n"
        f"$b_1 = {latex(bn_val)}$"
    )
    return {"question": question, "answer": answer}


def generate(level, num_questions):
    used = set()
    return [generate_periodic_fourier_question(level, used) for _ in range(num_questions)]
