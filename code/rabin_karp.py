def char_to_int(c):
    return ord(c) - ord('a') + 1

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    base = 10
    
    if m == 0 or n < m:
        return []
        
    pattern_hash = 0
    window_hash = 0
    h_multiplier = base ** (m - 1)
    
    for i in range(m):
        pattern_hash = pattern_hash * base + char_to_int(pattern[i])
        window_hash = window_hash * base + char_to_int(text[i])
        
    matches = []
    
    for i in range(n - m + 1):
        if window_hash == pattern_hash:
            if text[i:i+m] == pattern:
                matches.append(i)
        
        if i < n - m:
            old_char_val = char_to_int(text[i])
            new_char_val = char_to_int(text[i + m])
            window_hash = (window_hash - old_char_val * h_multiplier) * base + new_char_val
            
    return matches



def run_test(text, pattern):
    print("--- Rabin-Karp Search ---")
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    matches = rabin_karp(text, pattern)
    print(f"Matches at positions: {matches}\n")


if __name__ == "__main__":
    run_test("aliceandjoebakedcookies", "joe")
