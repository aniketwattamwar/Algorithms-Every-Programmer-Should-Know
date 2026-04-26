def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0 or n < m:
        return []

    lps = compute_lps(pattern)
    print(f"Pattern: '{pattern}'")
    print(f"Calculated LPS array: {lps}")

    matches = []
    i = 0
    j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


def run_test(text, pattern):
    print("--- KMP Search ---")
    print(f"Text:    {text}")
    matches = kmp_search(text, pattern)
    print(f"Matches at positions: {matches}\n")


if __name__ == "__main__":
    run_test("abcxabcdabxabcdabcdabcy", "abcdabcy")
    run_test("aabadeaabadcaab", "aabadc")
