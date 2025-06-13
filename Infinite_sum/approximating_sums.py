import random
from sympy import symbols, S, Sum, oo, latex, Rational


n = symbols('n', integer=True) # This 'n' will be used for the expression inside the sum for display


def partial_sum_geometric(a, r, k_upper_index): # k_upper_index is the upper limit of n (0 to k)
    if r == S.One:
        return a * (k_upper_index + 1)
    else:
        idx = symbols('idx_geom', integer=True)
        return Sum(a * r**idx, (idx, 0, k_upper_index)).doit()

def partial_sum_harmonic_calc(k_upper_index):
    idx = symbols('idx_harm', integer=True)
    return Sum(S.One/idx, (idx, 1, k_upper_index)).doit()

def partial_sum_power_series_calc(x_val, k_upper_index):
    idx = symbols('idx_power', integer=True)
    return Sum(idx * x_val**idx, (idx, 1, k_upper_index)).doit()


def partial_sum_geom_question():
    a_val = random.randint(1, 5)
    r_val = random.choice([S(1)/2, S(1)/3, S(2)/3])
    k_upper_index = random.randint(3, 6)
    
    expr_for_display = a_val * r_val**n 
    
    actual_partial_sum = partial_sum_geometric(S(a_val), S(r_val), k_upper_index) 
    
    q = (f"Find the partial sum of the geometric series \n\n $\\sum_{{n=0}}^\\infty {latex(expr_for_display)}$ \n\n "
         f"up to and including the term for $n={k_upper_index}$ (this is often denoted $S_{{{k_upper_index}}}$).")
    a_str = f"**Answer:** $S_{{{k_upper_index}}} = {latex(actual_partial_sum)}$"
    return q, a_str

def partial_sum_harmonic_question():
    k_num_terms = random.randint(4, 7)
    actual_partial_sum = partial_sum_harmonic_calc(k_num_terms)
    
    q = (f"Find the partial sum of the harmonic series \n\n $\\sum_{{n=1}}^\\infty \\frac{{1}}{{n}}$ \n\n "
         f"up to {k_num_terms} terms (i.e., $S_{{{k_num_terms}}}$).")
    a_str = f"**Answer:** $S_{{{k_num_terms}}} = {latex(actual_partial_sum)}$"
    return q, a_str

def partial_sum_alternating_geom_question():
    a_val = random.randint(1, 3)
    r_val = random.choice([-S(1)/2, -S(1)/3, -S(2)/3]) 
    k_upper_index = random.randint(3, 6)
    
    expr_for_display = a_val * r_val**n 
    
    actual_partial_sum = partial_sum_geometric(S(a_val), S(r_val), k_upper_index)
        
    q = (f"Find the partial sum of the alternating geometric series \n\n $\\sum_{{n=0}}^\\infty {latex(expr_for_display)}$ \n\n "
         f"up to and including the term for $n={k_upper_index}$ (this is often denoted $S_{{{k_upper_index}}}$).")
    a_str = f"**Answer:** $S_{{{k_upper_index}}} = {latex(actual_partial_sum)}$"
    return q, a_str

def partial_sum_power_series_question():
    x_val_coeff = random.choice([S(1)/2, S(1)/3, S(1)/4])
    k_num_terms = random.randint(3, 5)
    
    expr_for_display = n * x_val_coeff**n 
    
    actual_partial_sum = partial_sum_power_series_calc(S(x_val_coeff), k_num_terms)
        
    q = (f"Find the partial sum of the series \n\n $\\sum_{{n=1}}^\\infty {latex(expr_for_display)}$ \n\n "
         f"up to {k_num_terms} terms (i.e., $S_{{{k_num_terms}}}$).")
    a_str = f"**Answer:** $S_{{{k_num_terms}}} = {latex(actual_partial_sum)}$"
    return q, a_str

# === Return Q&A Based on Level and Question Count ===
def get_partial_sums_questions(level: int, num_questions: int):
    generators_by_level = {
        1: [partial_sum_geom_question],
        2: [partial_sum_harmonic_question],
        3: [partial_sum_alternating_geom_question],
        4: [partial_sum_power_series_question],
        5: [partial_sum_geom_question, partial_sum_harmonic_question],
        6: [partial_sum_alternating_geom_question, partial_sum_power_series_question],
        7: [partial_sum_geom_question, partial_sum_harmonic_question, 
            partial_sum_alternating_geom_question, partial_sum_power_series_question],
    }

    if level not in generators_by_level:
         raise ValueError(f"Invalid level: {level}. Level must be between 1 and {len(generators_by_level)}.")

    available_generators = generators_by_level[level]
    results = []
    for _ in range(num_questions):
        func_to_call = random.choice(available_generators)
        q, a = func_to_call()
        results.append({"question": q, "answer": a})
    
    return results

if __name__ == '__main__':
    # Test cases
    for lvl_test in range(1, 8):
        print(f"\n--- Testing Level {lvl_test} ---")
        try:
            questions = get_partial_sums_questions(lvl_test, 1)
            for i_q, qa_pair in enumerate(questions):
                print(f"Q{i_q+1}: {qa_pair['question']}")
                print(f"   {qa_pair['answer']}\n")
        except ValueError as e:
            print(f"Error for level {lvl_test}: {e}")

    print("\n--- Direct function tests ---")
    q_geom, a_geom = partial_sum_geom_question()
    print(f"Geom Q: {q_geom}\n   A: {a_geom}\n")
    q_harm, a_harm = partial_sum_harmonic_question()
    print(f"Harmonic Q: {q_harm}\n   A: {a_harm}\n")
    q_alt, a_alt = partial_sum_alternating_geom_question()
    print(f"Alt Geom Q: {q_alt}\n   A: {a_alt}\n")
    q_pow, a_pow = partial_sum_power_series_question()
    print(f"Power Series Q: {q_pow}\n   A: {a_pow}\n")