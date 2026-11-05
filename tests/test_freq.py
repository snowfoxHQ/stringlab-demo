"""Tests for stringlab.freq."""

import unittest

from stringlab import top_words, word_freq


class TestWordFreq(unittest.TestCase):
    def test_counts_are_case_insensitive(self):
        self.assertEqual(word_freq("The the THE"), {"the": 3})

    def test_punctuation_is_separated(self):
        self.assertEqual(word_freq("cat, cat. cat!"), {"cat": 3})

    def test_empty_text(self):
        self.assertEqual(word_freq(""), {})


class TestTopWords(unittest.TestCase):
    def test_orders_by_count_descending(self):
        self.assertEqual(
            top_words("b a b c b a", 2), [("b", 3), ("a", 2)]
        )

    def test_ties_keep_first_appearance(self):
        self.assertEqual(
            top_words("dog cat bird cat dog", 2),
            [("dog", 2), ("cat", 2)],
        )

    def test_n_larger_than_vocabulary(self):
        self.assertEqual(top_words("one one", 5), [("one", 2)])

    def test_numbers_count_as_words(self):
        self.assertEqual(top_words("r2d2 r2d2 c3po", 1), [("r2d2", 2)])


if __name__ == "__main__":
    unittest.main()
