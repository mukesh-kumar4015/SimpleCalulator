import unittest
from calculator import Calulator


class TestCalulator(unittest.TestCase):
    def setUp(self):
        self.calulator = Calulator()

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

    def test_add_string_numbers0_returns(self):
        result = self.calulator.add("25", "87.2")
        self.assertEqual(25 + 87.2, result)

        result = self.calulator.add(25, "87.2")
        self.assertEqual(25 + 87.2, result)

        result = self.calulator.add("25", 87.2)
        self.assertEqual(25 + 87.2, result)
