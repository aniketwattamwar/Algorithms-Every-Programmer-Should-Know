def char_to_int(c):
    """
    Converts a character to an integer value for hashing.
    
    Maps 'a' to 1, 'b' to 2, ..., 'z' to 26.
    
    Args:
        c (str): A single character.
    
    Returns:
        int: The integer value of the character.
    """
    return ord(c) - ord('a') + 1

def rabin_karp(text, pattern):
    """
    Implements the Rabin-Karp string searching algorithm.
    
    Uses rolling hash to efficiently find all occurrences of a pattern
    in a text by comparing hash values instead of characters directly.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: List of starting indices where the pattern is found.
    """
    n = len(text)
    m = len(pattern)
    base = 10  # Base for hashing (can be any number, 10 is simple)
    
    if m == 0 or n < m:
        return []
        
    pattern_hash = 0
    window_hash = 0
    h_multiplier = base ** (m - 1)  # Precompute multiplier for rolling hash
    
    # Calculate initial hash values for pattern and first window
    for i in range(m):
        pattern_hash = pattern_hash * base + char_to_int(pattern[i])
        window_hash = window_hash * base + char_to_int(text[i])
        
    matches = []
    
    # Slide the window through the text
    for i in range(n - m + 1):
        # Check if hashes match, then verify characters to avoid collisions
        if window_hash == pattern_hash:
            if text[i:i+m] == pattern:
                matches.append(i)
        
        # Update rolling hash for next window (if not at end)
        if i < n - m:
            old_char_val = char_to_int(text[i])
            new_char_val = char_to_int(text[i + m])
            window_hash = (window_hash - old_char_val * h_multiplier) * base + new_char_val
            
    return matches



def run_test(text, pattern):
    """
    Runs a test of the Rabin-Karp algorithm with given text and pattern.
    
    Prints the text, pattern, and positions where matches are found.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    """
    print("--- Rabin-Karp Search ---")
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    matches = rabin_karp(text, pattern)
    print(f"Matches at positions: {matches}\n")


if __name__ == "__main__":
    run_test("aliceandjoebakedcookies", "joe")
