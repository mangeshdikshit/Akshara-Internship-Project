import random
from sympy import symbols, factorial, latex, Rational
from sympy.abc import x

# Define functions and their Maclaurin series coefficients pattern for levels
LEVELS = {
    1: [("e^x", lambda n: 1 / factorial(n), r"a_n = \frac{1}{n!}")],
    2: [("sin(x)", lambda n: 0 if n % 2 == 0 else ((-1)**((n-1)//2)) / factorial(n),
         r"a_n = \begin{cases} \frac{(-1)^{\frac{n-1}{2}}}{n!}, & \text{if } n \text{ odd} \\ 0, & \text{if } n \text{ even} \end{cases}")],
    3: [("cos(x)", lambda n: 0 if n % 2 == 1 else ((-1)**(n//2)) / factorial(n),
         r"a_n = \begin{cases} \frac{(-1)^{\frac{n}{2}}}{n!}, & \text{if } n \text{ even} \\ 0, & \text{if } n \text{ odd} \end{cases}")],
    4: [("ln(1+x)", lambda n: (-1)**(n-1) / n if n > 0 else 0,
         r"a_n = \begin{cases} \frac{(-1)^{n-1}}{n}, & n \ge 1 \\ 0, & n = 0 \end{cases}")],
    5: [("1/(1+x)", lambda n: (-1)**n,
         r"a_n = (-1)^n")],
    6: [("arctan(x)", lambda n: 0 if n % 2 == 0 else ((-1)**((n-1)//2)) / n,
         r"a_n = \begin{cases} \frac{(-1)^{\frac{n-1}{2}}}{n}, & \text{if } n \text{ odd} \\ 0, & \text{if } n \text{ even} \end{cases}")],
    7: [("sqrt(1+x)", lambda n: 0 if n % 2 == 1 else
         ((-1)**(n//2) * factorial(2*(n//2))) / ((1 - 2*(n//2)) * (factorial(n//2))**2 * 4**(n//2)),
         r"a_{2k} = \frac{(-1)^k \cdot (2k)!}{(1 - 2k) \cdot (k!)^2 \cdot 4^k},\quad a_{2k+1} = 0")
    ]
}

QUESTION_TEMPLATES = [
    "Examine the first few terms of the Maclaurin series for ${}$. Can you deduce a general rule for its coefficients?",
    "For the function ${}$, analyze the Maclaurin series and identify the pattern in the coefficients.",
    "What is the general formula for the coefficients in the Maclaurin series expansion of ${}$?",
    "The Maclaurin series of ${}$ has a recognizable coefficient pattern. Derive this pattern.",
    "Determine the rule for the $n$th coefficient $a_n$ in the Maclaurin series for ${}$."
]

def generate_maclaurin_pattern_question(level):
    func_name, coeff_func, coeff_rule_latex = random.choice(LEVELS[level])
    terms = random.randint(4, 7)

    # Generate series expression string (but not included in the question)
    series_terms = []
    for n in range(terms):
        c = coeff_func(n)
        if c == 0:
            continue
        c_latex = latex(c)
        term = f"{c_latex} x^{n}" if n > 0 else f"{c_latex}"
        series_terms.append(term)
    series_str = " + ".join(series_terms).replace("+ -", "- ")

    # Form question
    template = random.choice(QUESTION_TEMPLATES)
    question = template.format(func_name)

    # Answer with actual coefficient rule
    answer = f"**Answer:**\n\nThe general coefficient pattern in the Maclaurin series of ${func_name}$ is:\n\n"
    answer += "$$\n" + coeff_rule_latex + "\n$$"

    return {"question": question, "answer": answer}

def generate(level, num_questions):
    return [generate_maclaurin_pattern_question(level) for _ in range(num_questions)]
