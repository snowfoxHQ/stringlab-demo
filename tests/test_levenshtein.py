"""Tests for stringlab.levenshtein."""

import unittest

from stringlab import edit_distance


class TestEditDistance(unittest.TestCase):
    def test_equal_strings(self):
        self.assertEqual(edit_distance("same", "same"), 0)

    def test_empty_versus_word(self):
        self.assertEqual(edit_distance("", "abc"), 3)
        self.assertEqual(edit_distance("abc", ""), 3)

    def test_classic_pair(self):
        self.assertEqual(edit_distance("kitten", "sitten"), 1)
        self.assertEqual(edit_distance("kitten", "sitting"), 3)

    def test_transposition_costs_two(self):
        # ab -> ba needs one substitution... actually two: a->b and b->a.
        self.assertEqual(edit_distance("ab", "ba"), 2)

    def test_symmetry(self):
        for a, b in (("flaw", "lawn"), ("abcdef", "azced"), ("x", "yyyy")):
            self.assertEqual(edit_distance(a, b), edit_distance(b, a))


if __name__ == "__main__":
    unittest.main()
