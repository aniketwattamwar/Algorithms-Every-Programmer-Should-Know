import argparse
import time


def compute_lps(pattern):
    """
    Computes the Longest Prefix Suffix (LPS) array for the KMP algorithm.
    
    The LPS array stores the length of the longest proper prefix that is also
    a suffix for each substring of the pattern. This helps skip unnecessary
    comparisons during pattern matching.
    
    Args:
        pattern (str): The pattern string to analyze.
    
    Returns:
        list: LPS array where lps[i] is the longest proper prefix-suffix length
              for pattern[0..i].
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Fall back to previous prefix
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    """
    Searches for all occurrences of a pattern in text using KMP algorithm.
    
    Uses the LPS array to efficiently skip characters that can't match,
    avoiding backtracking in the text.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: List of starting indices where the pattern is found.
    """
    n = len(text)
    m = len(pattern)

    if m == 0 or n < m:
        return []

    lps = compute_lps(pattern)

    matches = []
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            # Found a match
            matches.append(i - j)
            j = lps[j - 1]  # Continue searching for next occurrence
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                # Use LPS to skip characters
                j = lps[j - 1]
            else:
                i += 1  # Move to next character in text

    return matches


def run_test(text, pattern):
    """
    Runs a test of the KMP search algorithm with given text and pattern.
    
    Prints the text and positions where matches are found.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    """
    print("--- KMP Search ---")
    print(f"Text:    {text}")
    print(f"Pattern: '{pattern}'")
    print(f"Calculated LPS array: {compute_lps(pattern)}")
    matches = kmp_search(text, pattern)
    print(f"Matches at positions: {matches}\n")


def naive_search(text, pattern):
    """Search for all pattern occurrences by checking every possible position."""
    n = len(text)
    m = len(pattern)
    matches = []
    for i in range(n - m + 1):
        k = 0
        while k < m and text[i + k] == pattern[k]:
            k += 1
        if k == m:
            matches.append(i)
    return matches


def run_benchmark():
    """Compare naive search and KMP on inputs that trigger repeated comparisons."""
    for size in [2000, 4000, 8000, 16000]:
        text = "a" * size + "b"
        pattern = "a" * (size // 4) + "b"

        start = time.perf_counter()
        naive_matches = naive_search(text, pattern)
        naive_time = time.perf_counter() - start

        start = time.perf_counter()
        kmp_matches = kmp_search(text, pattern)
        kmp_time = time.perf_counter() - start

        if naive_matches != kmp_matches:
            raise AssertionError(f"Search results differ for text size {size}")

        print(
            f"text={size:6}: naive {naive_time * 1000:8.2f} ms | "
            f"KMP {kmp_time * 1000:7.2f} ms"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the KMP search examples.")
    parser.add_argument(
        "--benchmark",
        action="store_true",
        help="compare naive search with KMP",
    )
    args = parser.parse_args()

    if args.benchmark:
        run_benchmark()
    else:
        run_test("abcxabcdabxabcdabcdabcy", "abcdabcy")
        run_test("aabadeaabadcaab", "aabadc")
