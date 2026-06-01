# Horspool's Algorithm

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

## Example usage

```python
from code.horspool import horspool_search

text = "abcxabcdabxabcdabcdabcy"
pattern = "abcdabcy"
matches = horspool_search(text, pattern)
print(matches)  # [15]
```
