import random
from sympy import symbols, simplify, latex, sin, cos, exp, Abs, Rational
from sympy.abc import x

QUESTION_TEMPLATES = [
    "Given the function:\n\n$f(x) = {}$\n\nDecompose it into its even and odd parts.",
    "Find the even and odd components of the function:\n\n$f(x) = {}$",
    "Break the function $f(x) = {}$ into its even and odd parts.",
    "Decompose the following function into even and odd parts:\n\n$f(x) = {}$",
    "Split the function $f(x) = {}$ into its even and odd parts."
]

# Function generators per type
def generate_polynomial(level):
    degree = level + 1
    terms = []
    used_degrees = set()
    for _ in range(random.randint(2, level + 2)):
        while True:
            d = random.randint(0, degree)
            if d not in used_degrees:
                used_degrees.add(d)
                break
        coeff = random.randint(-5, 5)
        if coeff != 0:
            terms.append(coeff * x**d)
    return sum(terms)

def generate_trig(level):
    terms = []
    for _ in range(random.randint(1, level)):
        n = random.randint(1, level + 1)
        func = random.choice([sin, cos])
        coeff = random.choice([-1, 1]) * random.randint(1, 3)
        terms.append(coeff * func(n * x))
    return sum(terms)

def generate_exponential(level):
    terms = []
    for _ in range(random.randint(1, level)):
        base = random.choice([exp(x), exp(-x)])
        coeff = random.randint(1, 4) * random.choice([-1, 1])
        terms.append(coeff * base)
    return sum(terms)

def generate_absolute(level):
    inner = generate_polynomial(level)
    return Abs(inner) + random.randint(-3, 3) * x

EXPR_GENERATORS = [generate_polynomial, generate_trig, generate_exponential, generate_absolute]

def generate_random_function(level, existing_expressions):
    while True:
        expr_gen = random.choice(EXPR_GENERATORS)
        f = simplify(expr_gen(level))
        if f not in existing_expressions:
            existing_expressions.add(f)
            return f

def generate_even_odd_question(level, existing_expressions):
    f = generate_random_function(level, existing_expressions)
    f_neg = f.subs(x, -x)

    even_part = simplify((f + f_neg) / 2)
    odd_part = simplify((f - f_neg) / 2)

    template = random.choice(QUESTION_TEMPLATES)
    question = template.format(latex(f))

    # Helper to shorten or represent as simplified form
    def format_expr(expr):
        expr_latex = latex(expr)
        # if len(expr_latex) > 60:
            # return "\\text{(simplified expression)}"
        return expr_latex

    even_latex = format_expr(even_part)
    odd_latex = format_expr(odd_part)

    answer = (
        "**Answer:**\n\n"
        "$\n"
        f"f_e(x) = \\frac{{f(x) + f(-x)}}{{2}} = {even_latex} \\\\\n"
        f"f_o(x) = \\frac{{f(x) - f(-x)}}{{2}} = {odd_latex}\n"
        "$"
    )

    return {"question": question, "answer": answer}



def generate(level, num_questions):
    existing_expressions = set()
    return [generate_even_odd_question(level, existing_expressions) for _ in range(num_questions)]
