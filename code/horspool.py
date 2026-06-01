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


if __name__ == "__main__":
    run_test("abcxabcdabxabcdabcdabcy", "abcdabcy")
