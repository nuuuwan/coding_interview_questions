import unittest

import questions


class TestCase(unittest.TestCase):
    def test_is_palindrome(self):
        test_data_list = [
            ("", True),
            ("a", True),
            ("aa", True),
            ("ab", False),
            ("aba", True),
            ("abc", False),
            ("madam", True),
            ("python", False),
        ]
        for w, expected in test_data_list:
            self.assertEqual(questions.is_palindrome(w), expected)

    def test_fibonacci(self):
        test_data_list = [
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 5),
            (5, 8),
            (6, 13),
            (7, 21),
            (8, 34),
            (9, 55),
        ]
        for input, expected in test_data_list:
            with self.subTest(input=input):
                self.assertEqual(questions.fibonacci(input), expected)

    def test_fuzz(self):
        test_data_list = [
            (1, "1"),
            (3, "Fizz"),
            (5, "Buzz"),
            (15, "FizzBuzz"),
            (16, "16"),
            (18, "Fizz"),
            (20, "Buzz"),
            (30, "FizzBuzz"),
        ]
        for input, expected in test_data_list:
            with self.subTest(input=input):
                self.assertEqual(questions.fuzz(input), expected)

    def test_longest_substring_without_repeats(self):
        test_cases = [
            ('abcabcbb', 3),
            ('bbbbb', 1),
            ('pwwkew', 3),
            ('', 0),
            ('aab', 2),
            ('dvdf', 3),
        ]
        for input, expected in test_cases:
            with self.subTest(input=input):
                self.assertEqual(
                    questions.longest_substring_without_repeats(input),
                    expected,
                )

    def test_array_rotate(self):
        test_cases = [
            (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]),
            (([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5]),
            (([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5]),
            (([1, 2, 3, 4, 5], 1), [5, 1, 2, 3, 4]),
            (([1], 10), [1]),
        ]
        for input, expected in test_cases:
            with self.subTest(input=input):
                self.assertEqual(questions.array_rotate(*input), expected)
