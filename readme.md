# Auto Question Generation For Summation

A comprehensive Python-based educational tool that generates mathematical questions and problems across various topics in Summation. This project is designed to help students and educators create practice problems with varying difficulty levels.

## 🎯 Project Overview

This project is an intelligent mathematical question generation system that covers 10 major mathematical topics, each with multiple subtopics and 7 difficulty levels. It generates questions with proper mathematical notation using LaTeX formatting and provides detailed solutions.

## 📚 Topics Covered

### 1. **Summation** (`summation/`)
- **Direct Evaluation**: Basic summation problems with linear expressions
- **Index Shifting**: Problems involving changing summation indices
- **Levels**: 1-7 (increasing complexity from single to triple summations)

### 2. **Summation Properties** (`Summation_Properties/`)
- **Additive Property**: Combining multiple summations
- **Bounds Manipulation**: Changing summation limits
- **Distributive Property**: Factoring out constants
- **Multiplicative Property**: Handling constant multiples
- **Range Splitting and Merging**: Breaking down or combining summation ranges

### 3. **Linearity** (`linearity/`)
- **Constant Multiples**: Scaling summations by constants
- **Combining Linear Terms**: Adding/subtracting summations
- **Sum of Sums**: Nested summation structures
- **Applications in Double and Triple Summations**: Complex multi-dimensional sums

### 4. **Finite Sums** (`Finite_sum/`)
- **Sum of First n Natural Numbers**: Basic arithmetic progression sums
- **Sum of Squares and Cubes**: Power sums
- **General Polynomial Sum Forms**: Higher-degree polynomial summations
- **Sums with Custom Bounds**: Variable upper/lower limits
- **Piecewise Defined Summand**: Conditional summation expressions

### 5. **Infinite Sums** (`Infinite_sum/`)
- **Approximating Sums**: Partial sum calculations
- **Common Infinite Series**: Standard convergent series
- **Convergent Geometric Series**: Infinite geometric progressions

### 6. **Arithmetic Series** (`Arithmetic_Series/`)
- **Finding Number of Terms**: Solving for n in arithmetic sequences
- **Sum Given Terms**: Calculating sums with given parameters
- **Formula Evaluation**: Direct application of arithmetic series formulas
- **Real-Life Applications**: Practical problems (payments, investments)

### 7. **Geometric Series** (`Geometric_Series/`)
- **Finite Geometric Series**: Sums with finite terms
- **Infinite Geometric Series**: Convergent infinite sums
- **Growth Models**: Exponential growth/decay applications
- **Recursive Relations**: Series defined by recurrence relations

### 8. **Convergence of Series** (`Convergence_of_Series/`)
- **Understanding Convergence vs Divergence**: Basic concepts
- **Conditions for Convergence**: Theoretical foundations
- **P-Series Test**: Testing convergence of p-series
- **Geometric Test**: Geometric series convergence criteria
- **Basic Comparison Test**: Comparing series for convergence

### 9. **Divergence of Series** (`Divergence_of_Series/`)
- **Divergent P-Series**: Series that fail convergence tests
- **Divergence Tests**: Methods to identify divergent series

### 10. **Fourier Series** (`Fourier_series/`)
- **Even and Odd Function Decomposition**: Function symmetry analysis
- **Periodic Functions**: Fourier series for periodic functions
- **Sine and Cosine Coefficients**: Calculating Fourier coefficients

## 🏗️ Project Structure

```
├── main.py                          # Main entry point
├── output.md                        # Generated output file
├── summation/                       # Basic summation problems
│   ├── controller.py
│   ├── eval.py
│   ├── index_shifting.py
│   └── __init__.py
├── Summation_Properties/            # Summation properties
│   ├── controller.py
│   ├── Additive_property.py
│   ├── Bounds_manipulation.py
│   ├── Distributive_property.py
│   ├── Multiplicative_property.py
│   └── Splitting_and_merging_ranges.py
├── linearity/                       # Linear properties
│   ├── controller.py
│   ├── Constant_multiples.py
│   ├── Combining_linear_terms.py
│   ├── sum_of_sum.py
│   └── Application_in_double_and_triple_summations.py
├── Finite_sum/                      # Finite summation problems
│   ├── controller.py
│   ├── Sum_of_first_n_natural_numbers.py
│   ├── Sum_of_squares_and_cubes.py
│   ├── General_polynomial_sum_forms.py
│   ├── Sums_with_custom_bounds.py
│   └── Piecewise_defined_summand.py
├── Infinite_sum/                    # Infinite series
│   ├── controller.py
│   ├── approximating_sums.py
│   ├── common_infinite_series.py
│   └── convergent_geometric_series.py
├── Arithmetic_Series/               # Arithmetic sequences
│   ├── controller.py
│   ├── Finding_number_of_terms.py
│   ├── Finding_sum_given_terms.py
│   ├── Formula_of_Arithmetic_Series.py
│   └── Reallife_applications.py
├── Geometric_Series/                # Geometric sequences
│   ├── controller.py
│   ├── Finite_geometric_series_formula.py
│   ├── Infinite_geometric_series.py
│   ├── growth_models.py
│   └── Recursive_relations.py
├── Convergence_of_Series/           # Series convergence
│   ├── controller.py
│   ├── Understanding_convergence_vs_divergence.py
│   ├── Conditions_for_convergence.py
│   ├── pseries_test.py
│   ├── Geometric_test.py
│   └── Basic_comparison_test.py
├── Divergence_of_Series/            # Series divergence
│   ├── controller.py
│   └── Divergent_peries.py
└── Fourier_series/                  # Fourier analysis
    ├── controller.py
    ├── Even_and_odd_function_decomposition.py
    ├── Periodic_functions.py
    └── Sine_and_cosine_coefficients.py
```

## 🚀 Features

### **Multi-Level Difficulty System**
- **Level 1-7**: Progressive complexity across all topics
- **Adaptive Question Generation**: Questions scale with difficulty level
- **Mixed Question Types**: Each topic generates multiple question formats

### **Mathematical Notation**
- **LaTeX Integration**: Professional mathematical formatting
- **SymPy Integration**: Symbolic mathematics for accurate calculations
- **Proper Mathematical Symbols**: Greek letters, subscripts, superscripts

### **Question Types**
- **True/False Questions**: Conceptual understanding
- **Calculation Problems**: Step-by-step solutions
- **Application Problems**: Real-world scenarios
- **Proof-Based Questions**: Theoretical foundations

### **Output Format**
- **Markdown Generation**: Clean, readable output
- **Structured Format**: Organized by topic and subtopic
- **Answer Key**: Complete solutions provided

## 📋 Prerequisites

### Required Python Packages
```bash
pip install sympy
pip install IPython
```

### Python Version
- Python 3.7 or higher recommended
- Compatible with Python 3.6+

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mathematical-question-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 💻 Usage

### Basic Usage
1. Run `python main.py`
2. Select a topic from the available options (1-10)
3. Choose a difficulty level (1-7)
4. Specify the number of questions to generate
5. View the generated questions in `output.md`

### Example Session
```
Available Topics:
1. Summation
2. Summation_Properties
3. linearity
4. Finite_sum
5. Infinite_sum
6. Arithmetic_Series
7. Geometric_Series
8. Convergence_of_Series
9. Divergence_of_Series
10. Fourier_series

Enter the topic number: 1

Available Levels for Combined Summation Questions:
1. Level 1
2. Level 2
3. Level 3
4. Level 4
5. Level 5
6. Level 6
7. Level 7

Enter the number for the desired level (1-7): 3
Enter the total number of questions: 10

✅ Output written to output.md for topic: Summation
```

### Output Format
The generated questions are saved in `output.md` with the following structure:
```markdown
# Topic Name: Level X (Total: N)

## 1. Subtopic Name

**Q1.** Question text with LaTeX notation
**Answer:** Detailed solution

**Q2.** Next question...
```

## 🔧 Customization

### Adding New Topics
1. Create a new directory for your topic
2. Implement a `controller.py` with `run_topic_main()` function
3. Add topic modules with question generation functions
4. Update `main.py` with the new topic entry

### Modifying Question Generation
- Each topic module contains `generate()` functions
- Questions are generated based on difficulty level
- Modify the mathematical expressions in each module to change question types

### Difficulty Levels
- **Level 1**: Basic concepts, simple calculations
- **Level 2**: Introduction of negative numbers
- **Level 3**: Fractions and rational numbers
- **Level 4**: Double summations
- **Level 5**: Complex expressions with multiple variables
- **Level 6**: Mixed number types and advanced concepts
- **Level 7**: Triple summations and most complex problems

## 📊 Mathematical Content

### **Summation Fundamentals**
- Basic sigma notation: $\sum_{i=1}^{n} f(i)$
- Index shifting: $\sum_{i=1}^{n} f(i) = \sum_{j=0}^{n-1} f(j+1)$
- Properties: linearity, distributivity, associativity

### **Series Analysis**
- **Arithmetic Series**: $S_n = \frac{n}{2}(a_1 + a_n)$
- **Geometric Series**: $S_n = a_1\frac{1-r^n}{1-r}$ (finite), $S = \frac{a_1}{1-r}$ (infinite, |r|<1)
- **Convergence Tests**: p-series, geometric, comparison tests
- **Fourier Series**: $f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n\cos(nx) + b_n\sin(nx))$

### **Advanced Topics**
- **Multiple Summations**: $\sum_{i=1}^{n}\sum_{j=1}^{m} f(i,j)$
- **Conditional Summations**: Piecewise defined summands
- **Real-World Applications**: Financial calculations, growth models

## 🤝 Contributing

### Guidelines
1. **Code Style**: Follow PEP 8 conventions
2. **Documentation**: Add docstrings to all functions
3. **Testing**: Ensure questions generate correctly
4. **Mathematical Accuracy**: Verify all solutions

### Adding New Questions
1. Create question generation functions
2. Include proper LaTeX formatting
3. Provide accurate solutions
4. Test across different difficulty levels

