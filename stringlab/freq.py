"""Word frequency counting."""

import re

_WORD = re.compile(r"[a-z0-9']+")


def word_freq(text):
    """Case-insensitive word frequency as a dict {word: count}."""
    freq = {}
    for word in _WORD.findall(text.lower()):
        freq[word] = freq.get(word, 0) + 1
    return freq


def top_words(text, n):
    """The `n` most frequent words, most frequent first.

    Ties keep first-appearance order (stable sort on descending count).
    """
    freq = word_freq(text)
    first_seen = {}
    for word in _WORD.findall(text.lower()):
        first_seen.setdefault(word, len(first_seen))
    ranked = sorted(freq.items(), key=lambda item: (-item[1], first_seen[item[0]]))
    return ranked[:n]
