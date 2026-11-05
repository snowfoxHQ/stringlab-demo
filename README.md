# stringlab

A tiny, stdlib-only string algorithms library - and the official demo
target for the [ai-arsenal](../../README.md) test pipeline.

## Features

- `edit_distance(a, b)` - Levenshtein distance, classic DP
- `is_palindrome(text)` / `longest_palindrome(text)` - expand-around-center
- `word_freq(text)` / `top_words(text, n)` - case-insensitive word counts

## Usage

```python
from stringlab import edit_distance, top_words

edit_distance("kitten", "sitting")  # 3
top_words("b a b c b a", 2)         # [("b", 3), ("a", 2)]
```

## Tests

Two suites, same library:

```bash
python -m unittest discover -s tests -t . -v   # 19 tests, stdlib only
python -m pytest tests/ -q                     # 40 tests, needs pytest
```

The unittest suite is the zero-dependency baseline; the pytest suite is
pytest-native (plain functions + parametrize) and covers the same modules.

If your harness writes suite logs, name each one `test-<framework>.log`
(for example `test-unittest.log`, `test-pytest.log`) - the host-side gate
only reads files matching `test*.log`.

## Benchmarks

Measured with `python bench.py` (1 second per case):

| case | claim |
| --- | --- |
| levenshtein 32x32 | >= 500 ops/s |
| longest_palindrome, 400 chars | >= 100 ops/s |

## Branches

| branch | what it demonstrates |
| --- | --- |
| `main` | a clean project: pipeline ends PASS(0) |
| `demo/regression` | a subtle off-by-one bug - the pipeline must catch it: FAIL(1) |

The bug on the demo branch is invisible to the eye but obvious to
`edit_distance("", "abc")`: exactly what a test suite is for.
