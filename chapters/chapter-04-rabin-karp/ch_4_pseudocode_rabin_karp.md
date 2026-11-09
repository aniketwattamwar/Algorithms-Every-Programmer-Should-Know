# Chapter 4: Rabin-Karp Algorithm

Rabin-Karp uses a rolling hash to locate occurrences of a pattern within text. It compares hash values first, and only verifies character equality when the hashes match.

## Python implementation

The implementation is in [ch_4_code_rabin_karp.py](ch_4_code_rabin_karp.py).

## Pseudocode

```text
Turn each character into a number based on its position in the alphabet.
Choose a base and a modulus for the hash calculations.

Compute the pattern hash, reducing modulo the modulus after each character.
Compute the first text-window hash the same way (same length as pattern).
Precompute base raised to pattern length minus one, modulo the modulus.

Slide a window through the text:
    For each position, check if the window hash matches the pattern hash.
        If they match, verify that the actual characters are the same (to avoid false matches).
        If the characters match, record this position.
    
    Move to the next window position by:
        Removing the contribution of the leftmost character,
        Multiplying by the base value,
        Adding the contribution of the new rightmost character,
        Reducing the result modulo the modulus.

Continue until every window has been checked.
Return all positions where the pattern was found.
```
