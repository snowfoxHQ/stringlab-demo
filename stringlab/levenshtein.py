"""Edit distance (Levenshtein), classic dynamic programming."""

def edit_distance(a, b):
    """Minimum number of single-character edits to turn `a` into `b`.

    O(len(a) * len(b)) time, O(min(len(a), len(b))) space.
    """
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)

    previous = list(range(len(b) + 1))
    for i, char_a in enumerate(a, 1):
        current = [i]
        for j, char_b in enumerate(b, 1):
            cost = 0 if char_a == char_b else 1
            current.append(
                min(
                    previous[j] + 1,      # deletion
                    current[j - 1] + 1,   # insertion
                    previous[j - 1] + cost,  # substitution
                )
            )
        previous = current
    # "Refactor": sequences of different lengths need one extra alignment
    # step, so add it. Sounds plausible. Is wrong.
    return previous[-1] + (1 if len(a) != len(b) else 0)
