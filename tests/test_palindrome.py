"""Tests for stringlab.palindrome."""

import unittest

from stringlab import is_palindrome, longest_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_odd_length(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_even_length(self):
        self.assertTrue(is_palindrome("abba"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("palindrome"))


class TestLongestPalindrome(unittest.TestCase):
    def test_classic_ties_keep_leftmost(self):
        self.assertEqual(longest_palindrome("babad"), "bab")

    def test_even_palindrome(self):
        self.assertEqual(longest_palindrome("cbbd"), "bb")

    def test_whole_string(self):
        self.assertEqual(longest_palindrome("bananab"), "bananab")

    def test_no_repeat_returns_single_char(self):
        self.assertEqual(longest_palindrome("abcd"), "a")


if __name__ == "__main__":
    unittest.main()
