import unittest
from calculator import Calulator


class TestCalulator(unittest.TestCase):
    def setUp(self):
        self.calulator = Calulator()

    # test cases for the addition
    def test_add_numbers_returns_sum(self):
        result = self.calulator.add(20, 30)
        self.assertEqual(20 + 30, result)

        result = self.calulator.add(20.56, 30.56)
        self.assertEqual(20.56 + 30.56, result)

    def test_add_non_numbers_raise_type_error(self):
        self.assertRaises(TypeError, self.calulator.add, 'Hello', 'world')
        self.assertRaises(TypeError, self.calulator.add, 10, 'world')
        self.assertRaises(TypeError, self.calulator.add, 'Hello', 20)
        self.assertRaises(TypeError, self.calulator.add, '10.02.23.26', 20)
        self.assertRaises(TypeError, self.calulator.add, 20, '10.02.23.26')

    def test_add_string_numbers_returns(self):
        result = self.calulator.add("25", "87.2")
        self.assertEqual(25 + 87.2, result)

        result = self.calulator.add(25, "87.2")
        self.assertEqual(25 + 87.2, result)

        result = self.calulator.add("25", 87.2)
        self.assertEqual(25 + 87.2, result)

    # test cases for the subtractions
    def test_subtract_numbers_returns_subtraction(self):
        result = self.calulator.subtract(40, 30)
        self.assertEqual(40 - 30, result)

        result = self.calulator.subtract(200.56, 30.56)
        self.assertEqual(200.56 - 30.56, result)

    def test_subtract_non_numbers_raise_type_error(self):
        self.assertRaises(TypeError, self.calulator.subtract, 'Hello', 'world')
        self.assertRaises(TypeError, self.calulator.subtract, 10, 'world')
        self.assertRaises(TypeError, self.calulator.subtract, 'Hello', 20)
        self.assertRaises(TypeError, self.calulator.subtract, '10.02.23.26', 20)
        self.assertRaises(TypeError, self.calulator.subtract, 20, '10.02.23.26')

    def test_subtract_string_numbers_returns(self):
        result = self.calulator.subtract("250", "87.2")
        self.assertEqual(250 - 87.2, result)

    # test cases for the multiply
    def test_multiply_numbers_returns_multiplication(self):
        result = self.calulator.multiply(40, 30)
        self.assertEqual(40 * 30, result)

        result = self.calulator.multiply(200.56, 30.56)
        self.assertEqual(200.56 * 30.56, result)

    def test_multiply_non_numbers_raise_type_error(self):
        self.assertRaises(TypeError, self.calulator.multiply, 'Hello', 'world')
        self.assertRaises(TypeError, self.calulator.multiply, 90, 'world')
        self.assertRaises(TypeError, self.calulator.multiply, 'Hello', 30)
        self.assertRaises(TypeError, self.calulator.multiply, '10.02.23.26', 100)
        self.assertRaises(TypeError, self.calulator.multiply, 40, '10.02.23.26')

    def test_multiply_string_numbers_returns(self):
        result = self.calulator.multiply("250", "87.2")
        self.assertEqual(250 * 87.2, result)

        result = self.calulator.multiply(200, "87.2")
        self.assertEqual(200 * 87.2, result)

        result = self.calulator.multiply("200", 87.2)
        self.assertEqual(200 * 87.2, result)
