#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_all_equal(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -20, -3, -100]), -3)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-1, 0, 1, 2]), 2)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.5, 3.7, 0.9]), 3.7)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.2, 3, 0.5]), 3)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string(self):
        self.assertEqual(max_integer("abcde"), "e")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["abc", "xyz", "def"]), "xyz")

    def test_list_with_none_inside(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 3])

    def test_list_with_bool(self):
        self.assertEqual(max_integer([True, False, 10]), 10)


if __name__ == "__main__":
    unittest.main()
