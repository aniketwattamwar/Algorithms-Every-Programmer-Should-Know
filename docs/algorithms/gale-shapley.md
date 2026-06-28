# Chapter 2: Gale-Shapley Algorithm

Gale-Shapley is a stable matching algorithm that finds an assignment between two groups—such as students and universities—so that no pair would rather be matched with each other than with their assigned partner.

## Pseudocode

```text
Start with all students marked as free.
Keep an empty matching of universities to students.

Repeat while any students remain free:
    Take a free student and go through their universities in order of preference.
    
    For the next university the student hasn't proposed to:
        If the university has no match:
            Match the student with this university and mark them as matched.
        
        If the university already has a match:
            Check if the university prefers this new student over their current match.
            If yes, replace the current match with this student and mark the old match as free.
            If no, keep the current match and leave this student free.

When all students have been matched or exhausted their options, return the final matching.
```
