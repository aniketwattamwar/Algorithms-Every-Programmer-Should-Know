# Chapter 4: Rabin-Karp Algorithm

Rabin-Karp uses a rolling hash to locate occurrences of a pattern within text. It compares hash values first, and only verifies character equality when the hashes match.

## Pseudocode

```text
Turn each character into a number based on its position in the alphabet.

Compute a hash value for the pattern.
Compute a hash value for the first window of the text (same length as pattern).

Slide a window through the text:
    For each position, check if the window hash matches the pattern hash.
        If they match, verify that the actual characters are the same (to avoid false matches).
        If the characters match, record this position.
    
    Move to the next window position by:
        Removing the contribution of the leftmost character,
        Multiplying by the base value,
        Adding the contribution of the new rightmost character.

Continue until every window has been checked.
Return all positions where the pattern was found.
```
