"""Palindrome checks and longest-palindromic-substring."""


def is_palindrome(text):
    """True if `text` reads the same forwards and backwards."""
    return text == text[::-1]


def longest_palindrome(text):
    """The longest palindromic substring of `text`.

    On ties, the leftmost occurrence wins. Empty string returns "".
    Expand-around-center, O(n^2) time, O(1) extra space.
    """
    if not text:
        return ""
    best_start, best_len = 0, 1

    def expand(left, right):
        while left >= 0 and right < len(text) and text[left] == text[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1

    for center in range(len(text)):
        for start, length in (
            expand(center, center),      # odd length
            expand(center, center + 1),  # even length
        ):
            if length > best_len:
                best_start, best_len = start, length
    return text[best_start : best_start + best_len]
