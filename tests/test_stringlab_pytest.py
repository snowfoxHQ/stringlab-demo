"""Pytest-native suite for stringlab.

Same library, a different runner. The platform's log forensics understand
unittest and pytest output; this file exists so the pytest branch is
exercised on a real machine, not only in the self-test's fake logs.

Run: python -m pytest tests/ -q
"""

import pytest

from stringlab import (
    edit_distance,
    is_palindrome,
    longest_palindrome,
    top_words,
    word_freq,
)


@pytest.mark.parametrize(
    ("a", "b", "want"),
    [
        ("kitten", "sitting", 3),
        ("", "abc", 3),
        ("abc", "abc", 0),
        ("flaw", "lawn", 2),
        ("intention", "execution", 5),
        ("a", "", 1),
    ],
)
def test_edit_distance(a, b, want):
    assert edit_distance(a, b) == want


@pytest.mark.parametrize(
    ("text", "want"),
    [
        ("abba", True),
        ("abc", False),
        ("a", True),
        ("", True),
        ("abca", False),
        ("racecar", True),
    ],
)
def test_is_palindrome(text, want):
    assert is_palindrome(text) is want


@pytest.mark.parametrize(
    ("text", "want"),
    [
        ("", ""),
        ("abba", "abba"),
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("abc", "a"),  # tie: leftmost wins
    ],
)
def test_longest_palindrome(text, want):
    assert longest_palindrome(text) == want


def test_word_freq_case_insensitive():
    assert word_freq("Hello hello WORLD world world") == {
        "hello": 2,
        "world": 3,
    }


def test_word_freq_ignores_punctuation():
    assert word_freq("it's it's fine") == {"it's": 2, "fine": 1}


def test_top_words_order_and_ties():
    assert top_words("b a b c b a", 2) == [("b", 3), ("a", 2)]


def test_top_words_more_than_distinct():
    assert top_words("x y", 5) == [("x", 1), ("y", 1)]
