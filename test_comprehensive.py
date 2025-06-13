import unittest
import sys
import os
import random
from unittest.mock import patch, MagicMock
import importlib
from sympy import symbols, Sum, Rational, simplify, latex, sin, cos, pi, integrate, Piecewise, Abs, Eq, solve
from sympy.abc import i, j, k, x, n

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class ComprehensiveMathQuestionGeneratorTest(unittest.TestCase):
    """Comprehensive test suite for the entire mathematical question generator project."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.topics = {
            "1": ("Summation", "summation.controller"),
            "2": ("Summation_Properties", "Summation_Properties.controller"),
            "3": ("linearity", "linearity.controller"),
            "4": ("Finite_sum", "Finite_sum.controller"),
            "5": ("Infinite_sum", "Infinite_sum.controller"),
            "6": ("Arithmetic_Series", "Arithmetic_Series.controller"),
            "7": ("Geometric_Series", "Geometric_Series.controller"),
            "8": ("Convergence_of_Series", "Convergence_of_Series.controller"),
            "9": ("Divergence_of_Series", "Divergence_of_Series.controller"),
            "10": ("Fourier_series", "Fourier_series.controller"),
        }
        
        # Set random seed for reproducible tests
        random.seed(42)
    
    def test_01_project_structure(self):
        """Test that all required directories and files exist."""
        required_dirs = [
            "summation", "Summation_Properties", "linearity", "Finite_sum",
            "Infinite_sum", "Arithmetic_Series", "Geometric_Series",
            "Convergence_of_Series", "Divergence_of_Series", "Fourier_series"
        ]
        
        for dir_name in required_dirs:
            self.assertTrue(os.path.exists(dir_name), f"Directory {dir_name} does not exist")
            self.assertTrue(os.path.exists(os.path.join(dir_name, "controller.py")), 
                          f"controller.py missing in {dir_name}")
    
    def test_02_main_module_imports(self):
        """Test that all topic modules can be imported."""
        for key, (name, module_path) in self.topics.items():
            try:
                module = importlib.import_module(module_path)
                self.assertIsNotNone(module, f"Module {module_path} is None")
                
                # Test that run_topic_main function exists
                self.assertTrue(hasattr(module, 'run_topic_main'), 
                              f"run_topic_main function missing in {module_path}")
                self.assertTrue(callable(module.run_topic_main), 
                              f"run_topic_main is not callable in {module_path}")
            except ImportError as e:
                self.fail(f"Module {module_path} cannot be imported: {e}")
    
    def test_03_summation_module(self):
        """Test summation module functionality."""
        try:
            from summation.eval import generate_summation_question, evaluate_summation, generate_fraction
            from summation.index_shifting import generate_index_shifting_question
            from summation.controller import generate_questions_controller, run_topic_main
            
            # Test generate_fraction
            fraction = generate_fraction()
            self.assertIsInstance(fraction, Rational)
            
            # Test generate_summation_question for each level
            for level in ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7"]:
                question, answer_fn = generate_summation_question(level)
                self.assertIsInstance(question, str)
                self.assertTrue(len(question) > 0)
                self.assertTrue(callable(answer_fn))
                
                # Test answer function
                answer = evaluate_summation(answer_fn)
                self.assertIsInstance(answer, str)
                self.assertTrue(len(answer) > 0)
            
            # Test index shifting
            for level in ["Level 1", "Level 2", "Level 3"]:
                question, answer = generate_index_shifting_question(level)
                self.assertIsInstance(question, str)
                self.assertIsInstance(answer, str)
                self.assertTrue(len(question) > 0)
                self.assertTrue(len(answer) > 0)
            
            # Test controller
            output = generate_questions_controller("Level 1", 5)
            self.assertIsInstance(output, list)
            self.assertTrue(len(output) > 0)
            
        except ImportError as e:
            self.fail(f"Summation module import failed: {e}")
    
    def test_04_summation_properties_module(self):
        """Test summation properties module functionality."""
        try:
            from Summation_Properties.Additive_property import generate as generate_additive
            from Summation_Properties.Bounds_manipulation import generate as generate_bounds
            from Summation_Properties.Distributive_property import generate as generate_distributive
            from Summation_Properties.Multiplicative_property import generate as generate_multiplicative
            from Summation_Properties.Splitting_and_merging_ranges import generate as generate_splitting
            from Summation_Properties.controller import generate_all_summation_properties_questions_controller
            
            # Test each property generator
            for level in range(1, 8):
                # Test additive property
                additive_questions = generate_additive(level, 2)
                self.assertIsInstance(additive_questions, list)
                self.assertEqual(len(additive_questions), 2)
                
                # Test bounds manipulation
                bounds_questions = generate_bounds(level, 2)
                self.assertIsInstance(bounds_questions, list)
                self.assertEqual(len(bounds_questions), 2)
                
                # Test distributive property
                distributive_questions = generate_distributive(level, 2)
                self.assertIsInstance(distributive_questions, list)
                self.assertEqual(len(distributive_questions), 2)
                
                # Test multiplicative property
                multiplicative_questions = generate_multiplicative(level, 2)
                self.assertIsInstance(multiplicative_questions, list)
                self.assertEqual(len(multiplicative_questions), 2)
                
                # Test splitting and merging
                splitting_questions = generate_splitting(level, 2)
                self.assertIsInstance(splitting_questions, list)
                self.assertEqual(len(splitting_questions), 2)
            
            # Test controller
            output = generate_all_summation_properties_questions_controller("Level 1", 10)
            self.assertIsInstance(output, list)
            self.assertTrue(len(output) > 0)
            
        except ImportError as e:
            self.fail(f"Summation properties module import failed: {e}")
    
    def test_05_linearity_module(self):
        """Test linearity module functionality."""
        try:
            from linearity.Constant_multiples import generate_questions as generate_constant_multiple
            from linearity.Combining_linear_terms import generate_questions as generate_combining_terms
            from linearity.sum_of_sum import generate_questions as generate_sum_of_sum
            from linearity.Application_in_double_and_triple_summations import generate_questions as generate_application
            from linearity.controller import generate_all_linearity_questions_controller
            
            # Test each linearity generator
            for level in range(1, 8):
                # Test constant multiples
                constant_questions = generate_constant_multiple(level, 2)
                self.assertIsInstance(constant_questions, list)
                self.assertEqual(len(constant_questions), 2)
                
                # Test combining terms
                combining_questions = generate_combining_terms(level, 2)
                self.assertIsInstance(combining_questions, list)
                self.assertEqual(len(combining_questions), 2)
                
                # Test sum of sum
                sum_of_sum_questions = generate_sum_of_sum(level, 2)
                self.assertIsInstance(sum_of_sum_questions, list)
                self.assertEqual(len(sum_of_sum_questions), 2)
                
                # Test application
                application_questions = generate_application(level, 2)
                self.assertIsInstance(application_questions, list)
                self.assertEqual(len(application_questions), 2)
            
            # Test controller
            output = generate_all_linearity_questions_controller("Level 1", 10)
            self.assertIsInstance(output, list)
            self.assertTrue(len(output) > 0)
            
        except ImportError as e:
            self.fail(f"Linearity module import failed: {e}")
    
    def test_06_finite_sum_module(self):
        """Test finite sum module functionality."""
        try:
            from Finite_sum.Sum_of_first_n_natural_numbers import generate_question_answer_string as generate_natural
            from Finite_sum.Sum_of_squares_and_cubes import generate_questions as generate_powers
            from Finite_sum.General_polynomial_sum_forms import generate_general_poly_sums
            from Finite_sum.Sums_with_custom_bounds import generate_questions as generate_custom_bounds
            from Finite_sum.Piecewise_defined_summand import generate_questions as generate_piecewise
            from Finite_sum.controller import generate_all_finite_sum_questions_controller
            
            # Test each finite sum generator
            for level in range(1, 8):
                # Test natural numbers
                natural_output = generate_natural(level, 2)
                self.assertIsInstance(natural_output, str)
                self.assertTrue(len(natural_output) > 0)
                
                # Test powers (returns string, not list)
                power_output = generate_powers(level, 2)
                self.assertIsInstance(power_output, str)
                self.assertTrue(len(power_output) > 0)
                
                # Test custom bounds (returns list)
                custom_questions = generate_custom_bounds(level, 2)
                self.assertIsInstance(custom_questions, list)
                self.assertEqual(len(custom_questions), 2)
                
                # Test piecewise (returns list)
                piecewise_questions = generate_piecewise(level, 2)
                self.assertIsInstance(piecewise_questions, list)
                self.assertEqual(len(piecewise_questions), 2)
            
            # Test general polynomial sums
            poly_output = generate_general_poly_sums(1, 2)
            self.assertIsInstance(poly_output, str)
            self.assertTrue(len(poly_output) > 0)
            
            # Test controller
            output = generate_all_finite_sum_questions_controller("Level 1", 10)
            self.assertIsInstance(output, list)
            self.assertTrue(len(output) > 0)
            
        except ImportError as e:
            self.fail(f"Finite sum module import failed: {e}")
    
    def test_07_infinite_sum_module(self):
        """Test infinite sum module functionality."""
        try:
            from Infinite_sum.approximating_sums import get_partial_sums_questions
            from Infinite_sum.common_infinite_series import get_convergent_series_questions
            from Infinite_sum.convergent_geometric_series import generate_geometric_series
            from Infinite_sum.controller import generate_all_mixed_questions
            
            # Test each infinite sum generator
            for level in range(1, 8):
                # Test partial sums
                partial_questions = get_partial_sums_questions(level, 2)
                self.assertIsInstance(partial_questions, list)
                self.assertEqual(len(partial_questions), 2)
                
                # Test convergent series
                convergent_questions = get_convergent_series_questions(level, 2)
                self.assertIsInstance(convergent_questions, list)
                self.assertEqual(len(convergent_questions), 2)
                
                # Test geometric series
                geometric_questions = generate_geometric_series(level, 2)
                self.assertIsInstance(geometric_questions, list)
                self.assertEqual(len(geometric_questions), 2)
            
            # Test controller
            output = generate_all_mixed_questions("Level 1", 10)
            self.assertIsInstance(output, list)
            self.assertTrue(len(output) > 0)
            
        except ImportError as e:
            self.fail(f"Infinite sum module import failed: {e}")
    
    def test_08_arithmetic_series_module(self):
        """Test arithmetic series module functionality."""
        try:
            from Arithmetic_Series.Finding_number_of_terms import generate as generate_find_n
            from Arithmetic_Series.Finding_sum_given_terms import generate as generate_sum_given_terms
            from Arithmetic_Series.Formula_of_Arithmetic_Series import generate as generate_evaluate_sigma
            from Arithmetic_Series.Reallife_applications import generate as generate_real_life
            from Arithmetic_Series.controller import generate_all_arithmetic_questions
            
            # Test each arithmetic series generator
            for level in range(1, 8):
                # Test finding number of terms
                find_n_questions = generate_find_n(level, 2)
                self.assertIsInstance(find_n_questions, list)
                self.assertEqual(len(find_n_questions), 2)
                
                # Test sum given terms
                sum_questions = generate_sum_given_terms(level, 2)
                self.assertIsInstance(sum_questions, list)
                self.assertEqual(len(sum_questions), 2)
                
                # Test formula evaluation
                formula_questions = generate_evaluate_sigma(level, 2)
                self.assertIsInstance(formula_questions, list)
                self.assertEqual(len(formula_questions), 2)
                
                # Test real life applications
                real_life_questions = generate_real_life(level, 2)
                self.assertIsInstance(real_life_questions, list)
                self.assertEqual(len(real_life_questions), 2)
            
            # Test controller
            output = generate_all_arithmetic_questions("Level 1", 10)
            self.assertIsInstance(output, list)
            self.assertTrue(len(output) > 0)
            
        except ImportError as e:
            self.fail(f"Arithmetic series module import failed: {e}")
    
    def test_09_geometric_series_module(self):
        """Test geometric series module functionality."""
        try:
            from Geometric_Series.Finite_geometric_series_formula import generate as generate_finite_geometric
            from Geometric_Series.Infinite_geometric_series import generate as generate_infinite_geometric
            from Geometric_Series.growth_models import generate as generate_growth
            from Geometric_Series.Recursive_relations import generate as generate_recursive
            from Geometric_Series.controller import generate_all_geometric_questions_controller
            
            # Test each geometric series generator
            for level in range(1, 8):
                # Test finite geometric series
                finite_questions = generate_finite_geometric(level, 2)
                self.assertIsInstance(finite_questions, list)
                self.assertEqual(len(finite_questions), 2)
                
                # Test infinite geometric series
                infinite_questions = generate_infinite_geometric(level, 2)
                self.assertIsInstance(infinite_questions, list)
                self.assertEqual(len(infinite_questions), 2)
                
                # Test growth models
                growth_questions = generate_growth(level, 2)
                self.assertIsInstance(growth_questions, list)
                self.assertEqual(len(growth_questions), 2)
                
                # Test recursive relations
                recursive_questions = generate_recursive(level, 2)
                self.assertIsInstance(recursive_questions, list)
                self.assertEqual(len(recursive_questions), 2)
            
            # Test controller
            output = generate_all_geometric_questions_controller("Level 1", 10)
            self.assertIsInstance(output, list)
            self.assertTrue(len(output) > 0)
            
        except ImportError as e:
            self.fail(f"Geometric series module import failed: {e}")
    
    def test_10_convergence_module(self):
        """Test convergence of series module functionality."""
        try:
            from Convergence_of_Series.Understanding_convergence_vs_divergence import generate as generate_convergence_divergence
            from Convergence_of_Series.Conditions_for_convergence import generate as generate_conditions
            from Convergence_of_Series.pseries_test import generate as generate_pseries
            from Convergence_of_Series.Geometric_test import generate as generate_geometric_test
            from Convergence_of_Series.Basic_comparison_test import generate as generate_comparison
            from Convergence_of_Series.controller import generate_all_convergence_questions_controller
            
            # Test each convergence generator
            for level in range(1, 8):
                # Test convergence vs divergence
                conv_div_questions = generate_convergence_divergence(level, 2)
                self.assertIsInstance(conv_div_questions, list)
                self.assertEqual(len(conv_div_questions), 2)
                
                # Test conditions for convergence
                conditions_questions = generate_conditions(level, 2)
                self.assertIsInstance(conditions_questions, list)
                self.assertEqual(len(conditions_questions), 2)
                
                # Test p-series test
                pseries_questions = generate_pseries(level, 2)
                self.assertIsInstance(pseries_questions, list)
                self.assertEqual(len(pseries_questions), 2)
                
                # Test geometric test
                geometric_test_questions = generate_geometric_test(level, 2)
                self.assertIsInstance(geometric_test_questions, list)
                self.assertEqual(len(geometric_test_questions), 2)
                
                # Test comparison test
                comparison_questions = generate_comparison(level, 2)
                self.assertIsInstance(comparison_questions, list)
                self.assertEqual(len(comparison_questions), 2)
            
            # Test controller
            output = generate_all_convergence_questions_controller("Level 1", 10)
            self.assertIsInstance(output, list)
            self.assertTrue(len(output) > 0)
            
        except ImportError as e:
            self.fail(f"Convergence module import failed: {e}")
    
    def test_11_divergence_module(self):
        """Test divergence of series module functionality."""
        try:
            from Divergence_of_Series.Divergent_peries import generate as generate_divergent_questions
            from Divergence_of_Series.controller import generate_all_divergence_questions_controller
            
            # Test divergent series generator
            for level in range(1, 8):
                divergent_questions = generate_divergent_questions(level, 2)
                self.assertIsInstance(divergent_questions, list)
                self.assertEqual(len(divergent_questions), 2)
            
            # Test controller
            output = generate_all_divergence_questions_controller("Level 1", 10)
            self.assertIsInstance(output, list)
            self.assertTrue(len(output) > 0)
            
        except ImportError as e:
            self.fail(f"Divergence module import failed: {e}")
    
    def test_12_fourier_series_module(self):
        """Test Fourier series module functionality."""
        try:
            from Fourier_series.Even_and_odd_function_decomposition import generate as generate_even_odd
            from Fourier_series.Periodic_functions import generate as generate_periodic
            from Fourier_series.Sine_and_cosine_coefficients import get_fourier_coefficient_questions
            from Fourier_series.controller import generate_all_fourier_function_questions_controller
            
            # Test each Fourier series generator
            for level in range(1, 8):
                # Test even/odd decomposition
                even_odd_questions = generate_even_odd(level, 2)
                self.assertIsInstance(even_odd_questions, list)
                self.assertEqual(len(even_odd_questions), 2)
                
                # Test periodic functions
                periodic_questions = generate_periodic(level, 2)
                self.assertIsInstance(periodic_questions, list)
                self.assertEqual(len(periodic_questions), 2)
                
                # Test Fourier coefficients
                coefficient_questions = get_fourier_coefficient_questions(level, 2)
                self.assertIsInstance(coefficient_questions, list)
                self.assertEqual(len(coefficient_questions), 2)
            
            # Test controller
            output = generate_all_fourier_function_questions_controller("Level 1", 10)
            self.assertIsInstance(output, list)
            self.assertTrue(len(output) > 0)
            
        except ImportError as e:
            self.fail(f"Fourier series module import failed: {e}")
    
    def test_13_question_format_consistency(self):
        """Test that all generated questions follow consistent format."""
        try:
            from summation.eval import generate_summation_question
            from Arithmetic_Series.Finding_number_of_terms import generate as generate_find_n
            from Convergence_of_Series.pseries_test import generate as generate_pseries
            
            # Test summation questions
            question, answer_fn = generate_summation_question("Level 1")
            self.assertIn("$", question)  # Should contain LaTeX
            self.assertIn("\\sum", question)  # Should contain summation symbol
            
            # Test arithmetic series questions
            arithmetic_questions = generate_find_n(1, 1)
            self.assertIsInstance(arithmetic_questions, list)
            self.assertEqual(len(arithmetic_questions), 1)
            question_data = arithmetic_questions[0]
            self.assertIn("question", question_data)
            self.assertIn("answer", question_data)
            self.assertIn("$", question_data["question"])  # Should contain LaTeX
            
            # Test convergence questions
            convergence_questions = generate_pseries(1, 1)
            self.assertIsInstance(convergence_questions, list)
            self.assertEqual(len(convergence_questions), 1)
            question_data = convergence_questions[0]
            self.assertIn("question", question_data)
            self.assertIn("answer", question_data)
            
        except ImportError as e:
            self.fail(f"Question format test failed: {e}")
    
    def test_14_mathematical_correctness(self):
        """Test mathematical correctness of generated questions."""
        try:
            from summation.eval import generate_summation_question, evaluate_summation
            
            # Test summation evaluation
            question, answer_fn = generate_summation_question("Level 1")
            answer = evaluate_summation(answer_fn)
            
            # Answer should be a valid string representation
            self.assertIsInstance(answer, str)
            self.assertTrue(len(answer) > 0)
            
            # Test that answer can be parsed as a number or fraction
            if "/" in answer:
                # Fraction format
                parts = answer.split("/")
                self.assertEqual(len(parts), 2)
                self.assertTrue(parts[0].replace("-", "").isdigit())
                self.assertTrue(parts[1].isdigit())
            else:
                # Integer format
                self.assertTrue(answer.replace("-", "").isdigit())
            
        except ImportError as e:
            self.fail(f"Mathematical correctness test failed: {e}")
    
    def test_15_level_progression(self):
        """Test that question complexity increases with level."""
        try:
            from summation.eval import generate_summation_question
            
            # Test that higher levels generate more complex questions
            level1_question, _ = generate_summation_question("Level 1")
            level7_question, _ = generate_summation_question("Level 7")
            
            # Level 7 should have more complex LaTeX (triple summation)
            self.assertIn("\\sum", level1_question)
            self.assertIn("\\sum", level7_question)
            
            # Level 7 should have more summation symbols (triple vs single)
            level1_sums = level1_question.count("\\sum")
            level7_sums = level7_question.count("\\sum")
            self.assertGreaterEqual(level7_sums, level1_sums)
            
        except ImportError as e:
            self.fail(f"Level progression test failed: {e}")
    
    def test_16_error_handling(self):
        """Test error handling in question generation."""
        try:
            from summation.controller import generate_questions_controller
            
            # Test invalid level
            output = generate_questions_controller("Invalid Level", 5)
            self.assertIsInstance(output, list)
            self.assertTrue(any("Error" in line for line in output))
            
            # Test invalid question count
            output = generate_questions_controller("Level 1", -5)
            self.assertIsInstance(output, list)
            self.assertTrue(any("Error" in line for line in output))
            
        except ImportError as e:
            self.fail(f"Error handling test failed: {e}")
    
    def test_17_output_format(self):
        """Test that controller outputs are properly formatted."""
        try:
            from summation.controller import generate_questions_controller
            
            output = generate_questions_controller("Level 1", 3)
            
            # Should be a list of strings
            self.assertIsInstance(output, list)
            self.assertTrue(len(output) > 0)
            
            # Should contain markdown formatting
            output_text = "\n".join(output)
            self.assertIn("#", output_text)  # Should have headers
            self.assertIn("**Q", output_text)  # Should have question markers
            self.assertIn("**Answer:", output_text)  # Should have answer markers
            
        except ImportError as e:
            self.fail(f"Output format test failed: {e}")
    
    def test_18_random_seed_consistency(self):
        """Test that setting random seed produces consistent results."""
        try:
            from summation.eval import generate_summation_question
            
            # Set seed and generate questions
            random.seed(42)
            question1, answer_fn1 = generate_summation_question("Level 1")
            
            random.seed(42)
            question2, answer_fn2 = generate_summation_question("Level 1")
            
            # Should be identical with same seed
            self.assertEqual(question1, question2)
            
        except ImportError as e:
            self.fail(f"Random seed consistency test failed: {e}")
    
    def test_19_sympy_integration(self):
        """Test that SymPy integration works correctly."""
        try:
            from sympy import symbols, Sum, Rational, simplify
            
            # Test basic SymPy operations
            i = symbols('i')
            expr = 2*i + 3
            summation = Sum(expr, (i, 1, 5)).doit()
            self.assertIsNotNone(summation)
            
            # Test rational arithmetic
            r1 = Rational(1, 2)
            r2 = Rational(1, 3)
            result = r1 + r2
            self.assertEqual(result, Rational(5, 6))
            
        except ImportError as e:
            self.fail(f"SymPy integration test failed: {e}")
    
    def test_20_complete_workflow(self):
        """Test complete workflow from main to output generation."""
        try:
            # Mock the input and file operations
            with patch('builtins.input', side_effect=['1', '1', '5']):
                with patch('builtins.open', create=True) as mock_open:
                    mock_file = MagicMock()
                    mock_open.return_value.__enter__.return_value = mock_file
                    
                    # Import and run main
                    import main
                    main.main()
                    
                    # Verify file operations
                    mock_open.assert_called()
                    mock_file.write.assert_called()
                    
        except ImportError as e:
            self.fail(f"Complete workflow test failed: {e}")

def run_comprehensive_tests():
    """Run all comprehensive tests and return results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(ComprehensiveMathQuestionGeneratorTest)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"COMPREHENSIVE TEST RESULTS")
    print(f"{'='*60}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print(f"\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_comprehensive_tests()
    sys.exit(0 if success else 1) 