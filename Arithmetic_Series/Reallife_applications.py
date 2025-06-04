import random
from sympy import symbols, Rational, latex, simplify
from sympy.abc import n

# Levels configuration
LEVELS = {
    1: {'dims': 1, 'pos': True, 'neg': False, 'frac': False},
    2: {'dims': 1, 'pos': True, 'neg': True, 'frac': False},
    3: {'dims': 1, 'pos': True, 'neg': True, 'frac': True},
    4: {'dims': 2, 'pos': True, 'neg': False, 'frac': False},
    5: {'dims': 2, 'pos': True, 'neg': True, 'frac': False},
    6: {'dims': 2, 'pos': True, 'neg': True, 'frac': True},
    7: {'dims': 3, 'pos': True, 'neg': True, 'frac': True}
}

def get_random_number(pos=True, neg=False, frac=False):
    nums = list(range(100, 1000, 50))  # payment amounts
    if neg:
        nums += [-x for x in nums]
    num = random.choice(nums)
    if frac and random.choice([True, False]):
        denom = random.randint(2, 5)
        num = Rational(num, denom)
    return num

def generate_real_life_payment_question(level):
    config = LEVELS[level]
    a = get_random_number(config['pos'], config['neg'], config['frac'])  # first payment
    d = random.choice([50, 100, 150]) if not config['frac'] else get_random_number(config['pos'], config['neg'], config['frac'])
    n_val = random.randint(6, 12)  # number of months

    total_payment = simplify(n_val / 2 * (2 * a + (n_val - 1) * d))

    templates = [
        f"A person agrees to pay ₹${latex(a)}$ as the first installment of a loan, "
        f"increasing each subsequent monthly payment by ₹${latex(d)}$ for {n_val} months.\n\n"
        f"Calculate the total amount paid after {n_val} months using the arithmetic series formula:\n\n"
        r"$S_n = \frac{n}{2} \left[2a + (n - 1)d\right]$",

        f"Ravi decides to save ₹${latex(a)}$ in the first month and increase his savings by ₹${latex(d)}$ every month. "
        f"How much will he have saved in total after {n_val} months?\n\n"
        r"Use: $S_n = \frac{n}{2} \left[2a + (n - 1)d\right]$",

        f"A builder receives ₹${latex(a)}$ for the first stage of construction and the payment increases by ₹${latex(d)}$ for each following stage. "
        f"If there are {n_val} stages, find the total earnings.\n\n"
        r"$S_n = \frac{n}{2} \left[2a + (n - 1)d\right]$",

        f"A company offers a starting salary of ₹${latex(a)}$ with an increment of ₹${latex(d)}$ every month. "
        f"What will be the total salary received in {n_val} months?\n\n"
        r"$S_n = \frac{n}{2} \left[2a + (n - 1)d\right]$"
    ]

    question = random.choice(templates)
    answer = f"**Answer:** ₹${latex(total_payment)}$"

    return question, answer

def generate(level, num_questions):
    questions = []
    for _ in range(num_questions):
        q, a = generate_real_life_payment_question(level)
        questions.append({"question": q, "answer": a})
    return questions
