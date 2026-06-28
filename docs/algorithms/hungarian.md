# Chapter 3: Hungarian Algorithm

The Hungarian algorithm solves the assignment problem by finding the minimum-cost matching between workers and tasks. In this repository, it uses `scipy.optimize.linear_sum_assignment` when available, with a fallback to brute-force assignment.

## Pseudocode

```text
Option 1: Use an efficient solver if available
    Convert the cost matrix into the solver format.
    Ask the solver to find the minimum-cost pairing of workers to tasks.
    The solver returns one worker-task match per worker.
    Aggregate the chosen pairs and compute the total cost.
    Return the optimal assignment and total cost.

Option 2: Solve without a solver
    Start with no assignment and the best cost unknown.
    Generate every possible way to assign workers to distinct tasks.
    For each candidate assignment:
        Add the cost of each worker-task pair in the assignment.
        Compare the calculated cost with the best known cost.
        If this assignment is cheaper, remember it as the new best.
    After testing all possibilities, return the lowest-cost assignment and its cost.
```
