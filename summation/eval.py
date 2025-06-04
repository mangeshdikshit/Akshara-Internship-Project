from IPython.display import Markdown
import random
import fractions
from sympy import symbols, Sum, latex, Rational, simplify

i, j, k = symbols('i j k')

def generate_fraction():
    """Generates a random fraction as sympy Rational."""
    numerator = random.randint(-3, 3)
    denominator = random.randint(1, 5)
    return Rational(numerator, denominator)

def generate_question_template(n, a, b, level, is_double=False, is_triple=False, m=None, c=None, d=None, p=None, q=None, r=None):
    """Chooses a question template at random for single, double or triple summations with sympy latex."""
    # convert all coefficients to sympy Rationals for consistency in latex
    a_sym = Rational(a) if not isinstance(a, Rational) else a
    b_sym = Rational(b) if not isinstance(b, Rational) else b
    if is_double or is_triple:
        c_sym = Rational(c) if not isinstance(c, Rational) else c
        d_sym = Rational(d) if not isinstance(d, Rational) else d
    if is_triple:
        q_sym = Rational(q) if not isinstance(q, Rational) else q
        r_sym = Rational(r) if not isinstance(r, Rational) else r

    if not is_double and not is_triple:
        expr = a_sym*i + b_sym
        templates = [
            f"Compute:\n\n $ \\sum_{{i=1}}^{{{n}}} {latex(expr)} $",
            f"Evaluate the sum:\n\n $ \\sum_{{i=1}}^{{{n}}} {latex(expr)} $",
            f"Calculate:\n\n $ \\sum_{{i=1}}^{{{n}}} {latex(expr)} $",
            f"Find:\n\n $ \\sum_{{i=1}}^{{{n}}} {latex(expr)} $",
            f"Solve:\n\n $ \\sum_{{i=1}}^{{{n}}} {latex(expr)} $"
        ]
    elif is_double:
        expr = a_sym*i + b_sym*j + c_sym*i*j + d_sym
        templates = [
            f"Compute the double summation:\n\n $ \\sum_{{i=1}}^{{{n}}} \\sum_{{j=1}}^{{{m}}} {latex(expr)} $",
            f"Evaluate:\n\n $ \\sum_{{i=1}}^{{{n}}} \\sum_{{j=1}}^{{{m}}} {latex(expr)} $",
            f"Find the result:\n\n $ \\sum_{{i=1}}^{{{n}}} \\sum_{{j=1}}^{{{m}}} {latex(expr)} $",
            f"Calculate the value:\n\n $ \\sum_{{i=1}}^{{{n}}} \\sum_{{j=1}}^{{{m}}} {latex(expr)} $"
        ]
    elif is_triple:
        expr = a_sym*i + b_sym*j + c_sym*k + d_sym*i*j + q_sym*i*k + r_sym*j*k
        templates = [
            f"Evaluate the triple summation:\n\n $ \\sum_{{i=1}}^{{{n}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{k=1}}^{{{p}}} {latex(expr)} $",
            f"Find the total value:\n\n $ \\sum_{{i=1}}^{{{n}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{k=1}}^{{{p}}} {latex(expr)} $",
            f"Compute:\n\n $ \\sum_{{i=1}}^{{{n}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{k=1}}^{{{p}}} {latex(expr)} $",
            f"Solve the summation:\n\n $ \\sum_{{i=1}}^{{{n}}} \\sum_{{j=1}}^{{{m}}} \\sum_{{k=1}}^{{{p}}} {latex(expr)} $"
        ]
    return random.choice(templates)

def generate_summation_question(level):
    """Generates a summation question for Levels 1–7 using sympy expressions."""
    if level == "Level 1":
        n = random.randint(2, 6)
        a = random.randint(1, 3)
        b = random.randint(1, 4)
        template = generate_question_template(n, a, b, level)
        # symbolic summation using sympy
        expr = a*i + b
        summation = Sum(expr, (i, 1, n)).doit()
        return f"\n{template}\n", lambda: summation

    elif level == "Level 2":
        n = random.randint(2, 6)
        a = random.randint(-3, 3)
        b = random.randint(-3, 3)
        template = generate_question_template(n, a, b, level)
        expr = a*i + b
        summation = Sum(expr, (i, 1, n)).doit()
        return f"\n{template}\n", lambda: summation

    elif level == "Level 3":
        n = random.randint(2, 5)
        a = random.choice([random.randint(-3, 3), generate_fraction()])
        b = random.choice([random.randint(-3, 3), generate_fraction()])
        template = generate_question_template(n, a, b, level)
        expr = a*i + b
        summation = Sum(expr, (i, 1, n)).doit()
        return f"\n{template}\n", lambda: summation

    elif level == "Level 4":
        n = random.randint(2, 4)
        m = random.randint(2, 4)
        a, b, c, d = [random.randint(1, 3) for _ in range(4)]
        template = generate_question_template(n, a, b, level, is_double=True, m=m, c=c, d=d)
        expr = a*i + b*j + c*i*j + d
        summation = Sum(Sum(expr, (i, 1, n)), (j, 1, m)).doit()
        return f"\n{template}\n", lambda: summation

    elif level == "Level 5":
        n = random.randint(2, 4)
        m = random.randint(2, 4)
        a, b, c, d = [random.randint(-2, 2) for _ in range(4)]
        template = generate_question_template(n, a, b, level, is_double=True, m=m, c=c, d=d)
        expr = a*i + b*j + c*i*j + d
        summation = Sum(Sum(expr, (i, 1, n)), (j, 1, m)).doit()
        return f"\n{template}\n", lambda: summation

    elif level == "Level 6":
        n = random.randint(2, 3)
        m = random.randint(2, 3)
        def random_val(): return random.choice([random.randint(-2, 2), generate_fraction()])
        a, b, c, d = [random_val() for _ in range(4)]
        template = generate_question_template(n, a, b, level, is_double=True, m=m, c=c, d=d)
        expr = a*i + b*j + c*i*j + d
        summation = Sum(Sum(expr, (i, 1, n)), (j, 1, m)).doit()
        return f"\n{template}\n", lambda: summation

    elif level == "Level 7":
        n = m = p = random.randint(2, 3)
        def random_val(): return random.choice([random.randint(-2, 2), generate_fraction()])
        a, b, c, d, q, r = [random_val() for _ in range(6)]
        template = generate_question_template(n, a, b, level, is_triple=True, m=m, p=p, c=c, d=d, q=q, r=r)
        expr = a*i + b*j + c*k + d*i*j + q*i*k + r*j*k
        summation = Sum(Sum(Sum(expr, (i, 1, n)), (j, 1, m)), (k, 1, p)).doit()
        return f"\n{template}\n", lambda: summation



def evaluate_summation(summation_fn):
    """Evaluates the summation and returns answer as plain fraction string like '2/5' or integer."""
    result = summation_fn()
    simplified = simplify(result)

    if isinstance(simplified, Rational):
        num, den = simplified.p, simplified.q
        if den == 1:
            return str(num)
        else:
            return f"{num}/{den}"
    else:
        # If expression is integer or other sympy expression, convert to string
        return str(simplified)



def generate_questions(level, count):
    results = []
    for _ in range(count):
        question_text, summation_fn = generate_summation_question(level)
        solution_text = evaluate_summation(summation_fn)
        formatted_output = f"{question_text.strip()}\n\n**Answer:** $$$${solution_text}$$$$\n---\n"
        results.append(formatted_output)
    return results
