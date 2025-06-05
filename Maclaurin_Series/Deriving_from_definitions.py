import random
from sympy import symbols, diff, factorial, simplify, latex
from sympy.abc import x

# Define function levels for increasing difficulty
LEVELS = {
    1: [("e^x", lambda n: 1)],
    2: [("sin(x)", lambda n: 0 if n % 4 == 0 or n % 4 == 2 else ((-1)**((n-1)//2))),
        ("cos(x)", lambda n: 0 if n % 4 == 1 or n % 4 == 3 else ((-1)**(n//2)))],
    3: [("ln(1+x)", lambda n: (-1)**(n-1) * factorial(n-1))],
    4: [("1/(1+x)", lambda n: (-1)**n * factorial(n))],
    5: [("sqrt(1+x)", lambda n: ((-1)**(n-1)) * factorial(2*n-3) / (2**(2*n-2) * factorial(n-1)))],
    6: [("tan(x)", None)],
    7: [("arctan(x)", None)],
}

# Fresh question templates to vary tone and phrasing
QUESTION_TEMPLATES = [
    "Using the definition of Maclaurin series, derive the expansion of ${}$ up to {} terms.",
    "From the series definition, find the Maclaurin expansion for ${}$ including {} terms.",
    "Compute the Maclaurin series of ${}$ from first principles up to {} terms.",
    "By differentiating term-by-term, write the Maclaurin series for ${}$ using {} terms.",
    "Manually derive the Maclaurin series of ${}$ based on its definition, taking {} terms."
]

def derivative_at_0(func_lambda, n):
    try:
        return func_lambda(n)
    except:
        return None

def generate_maclaurin_from_definition(level):
    func_name, func_lambda = random.choice(LEVELS[level])
    a = 0  # Maclaurin center
    terms = random.randint(3 + level // 2, 5 + level)

    x = symbols('x')
    maclaurin_terms = []

    if func_lambda:
        for n in range(terms):
            deriv_n = derivative_at_0(func_lambda, n)
            if deriv_n is None:
                break
            term = (deriv_n / factorial(n)) * x**n
            maclaurin_terms.append(term)
        series_expr = simplify(sum(maclaurin_terms))
    else:
        from sympy import sin, cos, exp, log, tan, atan, sqrt
        func_dict = {
            "tan(x)": tan(x),
            "arctan(x)": atan(x)
        }
        series_expr = func_dict[func_name].series(x, 0, terms).removeO()

    template = random.choice(QUESTION_TEMPLATES)
    question = template.format(func_name, terms)

    answer = f"**Answer:**\n\nThe Maclaurin series derived from the definition is:\n\n"
    answer += "$$\n" + f"{func_name} \\approx " + latex(series_expr) + "\n$$"

    return {"question": question, "answer": answer}

def generate(level, num_questions):
    return [generate_maclaurin_from_definition(level) for _ in range(num_questions)]
