# Chapter 5: Knuth-Morris-Pratt Algorithm

Knuth-Morris-Pratt efficiently searches for a pattern in text by precomputing a longest-prefix-suffix array that lets it skip unnecessary comparisons.

## Pseudocode

```text
First, analyze the pattern to build a lookup table:
    For each position in the pattern, find the longest portion that is both:
        - A prefix (starts at the beginning)
        - A suffix (ends at this position)
    Store these lengths in a table.

Then search through the text:
    Starting from the beginning of both the text and pattern:
        Compare characters one by one.
        
        When characters match:
            Advance both pointers.
        
        When you've matched the entire pattern:
            Record this match position.
            Use the lookup table to decide where to resume searching.
        
        When characters don't match:
            If you had partial matches before this mismatch,
                use the lookup table to skip ahead instead of going back in the text.
            If no partial matches, just move forward in the text.

Return all positions where the pattern was found.
```
