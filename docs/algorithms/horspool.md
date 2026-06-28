# Chapter 6: Horspool's Algorithm

Horspool's algorithm is a simplified version of the Boyer-Moore string search algorithm.
It uses a bad-character shift table to skip over sections of the text quickly when a
mismatch occurs.

## How it works

- Precompute a bad character table for the pattern.
- Compare the pattern against the text from right to left.
- When a mismatch occurs, shift the pattern by the bad-character rule using the
  text character aligned with the pattern's final position.
- If the character does not appear in the pattern, shift the full pattern length.

## Implementation details

- The bad character table stores shift distances for all pattern characters except
  the final character.
- On a mismatch, Horspool always consults the character under the end of the current
  text window.
- A complete match returns the starting index, and then the algorithm continues by
  advancing the search window.

## Pseudocode

```text
First, create a shift table for the pattern:
    For each character in the pattern (except the last one),
    record how many positions to shift the pattern if that character causes a mismatch.

Then search the text:
    Starting from the beginning of the text:
        Compare the pattern against the text window from right to left.
        
        If all characters match:
            Record this position as a match.
            Shift the pattern forward by one position.
        
        If a mismatch occurs:
            Look at the character in the text where the mismatch happened.
            Shift the pattern by the amount stored in the table for that character.
            If the character is not in the table, shift by the full pattern length.
    
    Continue until you can no longer fit the pattern in the remaining text.

Return all positions where matches were found.
```

## Example usage

```python
from code.horspool import horspool_search

text = "abcxabcdabxabcdabcdabcy"
pattern = "abcdabcy"
matches = horspool_search(text, pattern)
print(matches)  # [15]
```
