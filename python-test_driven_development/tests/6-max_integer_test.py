import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_all_equal(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.8]), 2.7)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "z", "d"]), "z")

    def test_string_list(self):
        self.assertEqual(max_integer(["abc", "abcd", "a"]), "abcd")

    def test_not_list_input(self):
        with self.assertRaises(TypeError):
            max_integer(42)

    def test_list_with_non_int(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])