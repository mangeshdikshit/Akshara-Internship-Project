import random
from sympy import symbols, Sum, Rational, simplify, latex, oo, log, sqrt, Abs, S
from sympy.abc import i

def get_poly_term(var, max_deg=2, coeff_range=(-3,3)):
    deg = random.randint(0, max_deg)
    coeff = random.choice([c for c in range(coeff_range[0], coeff_range[1]+1) if c != 0])
    return coeff * var**deg if deg > 0 else S(coeff)

def get_simple_modifier(var):
    return random.choice([
        S.Zero, S(random.randint(1,3)), S(random.randint(-3,-1)),
        log(var) / random.randint(1,2) if random.random() < 0.3 else S.Zero,
        S.One / var if random.random() < 0.2 else S.Zero
    ])

LEVEL_CONFIG = {
    1: {'types': ['direct_p_le_1'], 'p_range_le_1': (0.1, 1.0), 'complexity': 1},
    2: {'types': ['direct_p_le_1', 'nth_term_obvious_poly'], 'p_range_le_1': (0.5, 1.0), 'complexity': 1},
    3: {'types': ['direct_p_le_1', 'harmonic_variant'], 'p_range_le_1': (0.7, 1.0), 'complexity': 2},
    4: {'types': ['limit_comparison_p_le_1', 'nth_term_rational'], 'p_range_le_1': (0.1, 1.0), 'complexity': 2},
    5: {'types': ['direct_comparison_p_le_1', 'harmonic_variant_complex'], 'p_range_le_1': (0.5, 1.0), 'complexity': 3},
    6: {'types': ['limit_comparison_p_le_1', 'nth_term_dominant_term'], 'p_range_le_1': (0.1, 1.0), 'complexity': 3},
    7: {'types': ['direct_p_le_1', 'limit_comparison_p_le_1', 'nth_term_obvious_poly', 'harmonic_variant_complex'],
        'p_range_le_1': (0.1, 1.0), 'complexity': 4}
}

TF_QUESTION_TEMPLATES = [
    "True or False: The series {sum_latex_part} {stated_behavior_and_reason}.",
    "Evaluate the following statement as True or False: The infinite series with general term $a_i = {expr_latex}$ {stated_behavior_and_reason}. (The series is $\sum a_i$ from $i=1$ to $\infty$).",
    "Is the following assertion correct? The series {sum_latex_part} {stated_behavior_and_reason}.",
    "True or False: For the series with $a_i = {expr_latex}$, it {stated_behavior_and_reason}. (Consider the sum from $i=1$ to $\infty$)."
]

def generate_series_and_correct_reason(level):
    config = LEVEL_CONFIG[level]
    series_type = random.choice(config['types'])
    complexity = config['complexity']
    expr = None
    correct_reason_for_divergence = "The series diverges " 

    if series_type == 'direct_p_le_1':
        p_min, p_max = config['p_range_le_1']
        p_val_float = random.uniform(p_min, p_max)
        p_val = round(p_val_float, 3) 
        if p_val == 0: p_val = 0.001 # ensure not exactly zero after rounding, use a small value
        
        if complexity <= 2: 
            expr = S.One / (i**S(str(p_val))) # Use string representation for exact Rational
        else:
            numerator = random.randint(1,3)
            # Round the p-value in the modifier to 3 decimal places
            modifier_p_val_float = random.uniform(0.1,0.3)
            modifier_p_val = round(modifier_p_val_float, 3)
            denominator_modifier = random.choice([S.Zero, S.One/i**S(str(modifier_p_val)), log(i)/random.randint(2,4)])
            expr = S(numerator) / (i**S(str(p_val)) + denominator_modifier)
            expr = simplify(expr)
            
        if S(str(p_val)) == S.One and simplify(expr - S.One/i) == S.Zero : # Compare with SymPy One
            correct_reason_for_divergence += "because it is the harmonic series (p=1)."
        else:
            correct_reason_for_divergence += f"by the p-series test, as p = {p_val} ≤ 1." # Display rounded p_val

    elif series_type == 'nth_term_obvious_poly':
        if complexity == 1:
            expr = get_poly_term(i, max_deg=0) 
            if expr == S.Zero: expr = S(random.randint(1,3)) 
        else:
            expr = get_poly_term(i, max_deg=complexity-1)
        correct_reason_for_divergence += "by the nth-term test for divergence, as the terms $a_i = " + latex(expr) + "$ do not approach 0."

    elif series_type == 'harmonic_variant':
        scale = random.randint(1, 3) if complexity < 3 else random.randint(1,5)
        shift = random.randint(0, 2) if complexity < 3 else random.randint(0,4)
        if scale == 1 and shift == 0: 
            if random.choice([True,False]): scale = random.randint(2,3)
            else: shift = random.randint(1,2)
        expr = S(scale) / (i + S(shift))
        correct_reason_for_divergence += f"as it is a variant of the harmonic series (behaves like $\sum {latex(S(scale)/i)}$)."

    elif series_type == 'limit_comparison_p_le_1':
        p_min, p_max = config['p_range_le_1']
        # Round p_comp to 3 decimal places
        p_comp_float = random.uniform(p_min, p_max)
        p_comp = round(p_comp_float, 3)
        if p_comp == 0: p_comp = 0.001
        
        numerator_poly_deg = random.randint(0, complexity -1)
        denominator_poly_power = S(str(numerator_poly_deg + p_comp)) 
        
        num = get_poly_term(i, max_deg=numerator_poly_deg, coeff_range=(1,3)) 
        den_lead_coeff = random.randint(1,3)
        den_main_term = den_lead_coeff * i**denominator_poly_power
        den_rest_max_deg = 0
        if float(denominator_poly_power) > 0 : 
            den_rest_max_deg = int(float(denominator_poly_power) -1) if float(denominator_poly_power) >=1 else 0

        den = den_main_term + get_poly_term(i, max_deg=den_rest_max_deg)
        if den == S.Zero: den = S.One 
        
        expr = simplify(num / den)
        correct_reason_for_divergence += f"by the Limit Comparison Test with the divergent p-series $\sum 1/i^{{{p_comp}}}$, as $\lim_{{i \\to \infty}} \\frac{{{latex(expr)}}}{{1/i^{{{p_comp}}}}} = L$, where $0 < L < \infty$."

    elif series_type == 'direct_comparison_p_le_1':
        p_comp_float = random.uniform(0.1, 1.0)
        p_comp = round(p_comp_float, 3)
        if p_comp == 0: p_comp = 0.001
        
        c = random.randint(1,2)
        b_n = S(c) / (i**S(str(p_comp))) # Use string for exact Rational
        if complexity <= 2 :
            expr = S(c+random.randint(0,1)) / (i**S(str(p_comp)) - get_simple_modifier(i)/S(10)) 
        else:
            expr = (S(c) * i + random.randint(1,3)) / (i**(S(str(p_comp))+S.One) - i/S(2) + S.One) 
        expr = simplify(expr)
        correct_reason_for_divergence += f"by the Direct Comparison Test. The terms $a_i = {latex(expr)}$ are greater than or equal to terms of a known divergent p-series like $\sum {latex(b_n)}$ (for large enough i)."

    elif series_type == 'nth_term_rational':
        deg_num = random.randint(1, complexity)
        deg_den = random.randint(0, deg_num) 
        num = get_poly_term(i, max_deg=deg_num, coeff_range=(1,3))
        den = get_poly_term(i, max_deg=deg_den, coeff_range=(1,3))
        if den == S.Zero: den = S.One 
        expr = simplify(num / den)
        correct_reason_for_divergence += "by the nth-term test for divergence, as the terms $a_i = " + latex(expr) + "$ do not approach 0."

    elif series_type == 'nth_term_dominant_term':
        if complexity <=2 :
            expr = S(random.randint(2,5)) - S.One/i
        else:
            base_float = random.choice([2.0, 1.5, 1.1]) # Start with float for easy random choice
            base = S(str(base_float)) # Convert to SymPy Rational/Float from string for precision
            expr = base**i / (base**i - S.One) if random.choice([True,False]) else (i**complexity + i)/(i**complexity - S.One) 
        expr = simplify(expr)
        correct_reason_for_divergence += "by the nth-term test for divergence, as the terms $a_i = " + latex(expr) + "$ do not approach 0."
    
    if expr is None:
        expr = S.One / i
        correct_reason_for_divergence = "The series diverges because it is the harmonic series (p=1)."
    
    summation = Sum(expr, (i, 1, oo))
    return summation, correct_reason_for_divergence, expr

# --- get_false_reason (remains the same) ---
def get_false_reason(correct_reason_str, expr_obj):
    if "diverges" in correct_reason_str.lower():
        return random.choice([
            "converges by the p-series test as p > 1.",
            "converges because it is a geometric series with |r| < 1.",
            "converges by the alternating series test as terms decrease to zero.",
            "converges because its terms approach 0 rapidly."
        ])
    else: 
        return "converges for a plausible but incorrect reason."

def generate_tf_question(level):
    summation_obj, correct_reason, expr_obj = generate_series_and_correct_reason(level)
    is_statement_true = random.choice([True, False])
    stated_behavior_and_reason = ""
    actual_answer = ""

    if is_statement_true:
        stated_behavior_and_reason = correct_reason.replace("The series ", "", 1).strip()
        actual_answer = "True"
    else:
        if random.random() < 0.7: 
            stated_behavior_and_reason = get_false_reason(correct_reason, expr_obj)
        else: 
            stated_behavior_and_reason = "diverges " + random.choice([
                "because it is a p-series with p > 1.", 
                "because it is an alternating series with terms approaching 0.",
                "by the geometric series test with |r| > 1, but the terms are positive."
            ])
        actual_answer = "False"
        
    template = random.choice(TF_QUESTION_TEMPLATES)
    sum_latex_str = f"$$\sum_{{i=1}}^{{\infty}} {latex(summation_obj.function)}$$" # Corrected to \infty
    expr_latex_str = latex(summation_obj.function)

    if "{sum_latex_part}" in template:
        question_latex = template.replace("{sum_latex_part}", sum_latex_str).replace("{stated_behavior_and_reason}", stated_behavior_and_reason)
    elif "{expr_latex}" in template:
         question_latex = template.replace("{expr_latex}", expr_latex_str).replace("{stated_behavior_and_reason}", stated_behavior_and_reason)
    else:
        question_latex = f"True or False: The series {sum_latex_str} {stated_behavior_and_reason}."

    answer_explanation = ""
    if not is_statement_true:
        answer_explanation = f" The correct statement is: {correct_reason}"

    answer_latex = f"**Answer:** {actual_answer}.{answer_explanation}"
    
    return question_latex, answer_latex, str(simplify(expr_obj))

# --- Main `generate` function (remains the same) ---
def generate(level, num_questions):
    questions = []
    seen_expressions_strs = set()
    attempts = 0
    max_attempts_total = num_questions * 15

    while len(questions) < num_questions and attempts < max_attempts_total:
        attempts += 1
        try:
            question_text, answer_text, expr_str_for_uniqueness = generate_tf_question(level)
            
            if expr_str_for_uniqueness in seen_expressions_strs:
                if random.random() < 0.5 : 
                    continue

            seen_expressions_strs.add(expr_str_for_uniqueness)
            questions.append({"question": question_text, "answer": answer_text})
        except Exception as e:
            print(f"Error during question generation for level {level}: {e}")

    if len(questions) < num_questions:
        print(f"Warning: Could only generate {len(questions)} True/False questions for level {level}.")
        
    return questions
