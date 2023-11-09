import unittest
from math_quiz import generateInteger, generateOperator, mathOperator


class TestMathGame(unittest.TestCase):

    def test_generateInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generateInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
        print("      Test 1 - Passed")

    def test_generateOperator(self):
        for i in range(10):
            self.assertTrue(generateOperator() in ['+', '-', '*'])
        print("     Test 2 - Passed")

    def test_mathOperator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 2, '*', '10 * 2', 20),
                (4, 3, '-', '4 - 3', 1)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                achieved_problem, achieved_answer = mathOperator(num1, num2, operator)
                self.assertTrue(achieved_answer==expected_answer)
                self.assertTrue(achieved_problem==expected_problem)
            print("     Test 3 - Passed")  

if __name__ == "__main__":
    unittest.main()
