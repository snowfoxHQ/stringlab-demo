"""stringlab - a tiny stdlib-only string algorithms library.

This project exists to demonstrate the ai-arsenal test pipeline. It is
deliberately boring: no third-party dependencies, standard unittest, a
benchmark whose claims live in the README - so a full pipeline run ends
in a clean, honest PASS(0) on any machine, even with sandbox network
access blocked.
"""

__version__ = "1.0.0"

from .levenshtein import edit_distance
from .palindrome import is_palindrome, longest_palindrome
from .freq import word_freq, top_words

__all__ = [
    "edit_distance",
    "is_palindrome",
    "longest_palindrome",
    "word_freq",
    "top_words",
]
