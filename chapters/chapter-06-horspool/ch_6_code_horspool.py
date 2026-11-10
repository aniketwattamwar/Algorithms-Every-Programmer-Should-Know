import argparse
import time
import random


def build_bad_char_table(pattern):
    """
    Constructs the bad character shift table for Horspool's algorithm.

    Rule: Shift = Length - 1 - index
    Rule: Ignore the final character. Overwrite with rightmost occurrences.
    """
    m = len(pattern)
    bad_char_table = {}

    for i in range(m - 1):
        bad_char_table[pattern[i]] = m - 1 - i

    return bad_char_table


def horspool_search(text, pattern):
    """
    Executes the Boyer-Moore-Horspool search utilizing right-to-left scanning.

    Args:
        text (str): The text to search within.
        pattern (str): The pattern to find.

    Returns:
        list: Starting indices of each match in the text.
    """
    n = len(text)
    m = len(pattern)

    if m == 0 or n < m:
        return []

    bad_char_table = build_bad_char_table(pattern)
    matches = []
    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            matches.append(i)
            shift = bad_char_table.get(text[i + m - 1], m)
        else:
            bad_char = text[i + m - 1]
            shift = bad_char_table.get(bad_char, m)

        i += shift

    return matches


def run_test(text, pattern):
    """
    Runs a test of Horspool search with given text and pattern.
    """
    print("--- Horspool Search ---")
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    matches = horspool_search(text, pattern)
    print(f"Matches at positions: {matches}\n")


def generate_text(alphabet, size, seed=42):
    rng = random.Random(seed)
    return "".join(rng.choices(alphabet, k=size))


def median_ms(text, pattern, runs=11):
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        horspool_search(text, pattern)
        elapsed = (time.perf_counter() - start) * 1000
        times.append(elapsed)
    times.sort()
    return times[len(times) // 2]


def run_benchmark():
    """Compare Horspool performance across different alphabet sizes."""
    text_size = 200_000

    inputs = [
        ("English (26 chars)", "abcdefghijklmnopqrstuvwxyz"),
        ("DNA     ( 4 chars)", "acgt"),
        ("Binary  ( 2 chars)", "ab"),
    ]

    for label, alphabet in inputs:
        text = generate_text(alphabet, text_size)
        print(label)
        for m in [8, 32, 128]:
            pattern = text[text_size // 2 : text_size // 2 + m]
            ms = median_ms(text, pattern)
            print(f"  pattern length {m:>3}: {ms:6.2f} ms")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Horspool search examples.")
    parser.add_argument(
        "--benchmark",
        action="store_true",
        help="compare Horspool on English, DNA, and binary text",
    )
    args = parser.parse_args()

    if args.benchmark:
        run_benchmark()
    else:
        run_test("abcxabcdabxabcdabcdabcy", "abcdabcy")
