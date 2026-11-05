#!/usr/bin/env python3
"""Benchmark whose numbers the README claims. Report section 7 compares."""

import random
import string
import time

from stringlab import edit_distance, longest_palindrome


def measure(fn, seconds=1.0):
    random.seed(2026)
    ops = 0
    deadline = time.perf_counter() + seconds
    while time.perf_counter() < deadline:
        fn()
        ops += 1
    return ops / seconds


def bench_levenshtein():
    a = "".join(random.choice(string.ascii_lowercase) for _ in range(32))
    b = "".join(random.choice(string.ascii_lowercase) for _ in range(32))
    return measure(lambda: edit_distance(a, b))


def bench_palindrome():
    text = "".join(random.choice("ab") for _ in range(400))
    return measure(lambda: longest_palindrome(text))


def main():
    lev = bench_levenshtein()
    pal = bench_palindrome()
    print("levenshtein(32x32): %.0f ops/s (README claims >= 500)" % lev)
    print("longest_palindrome(400 chars): %.0f ops/s (README claims >= 100)" % pal)
    if lev < 500 or pal < 100:
        raise SystemExit("benchmark below README claims")


if __name__ == "__main__":
    main()
