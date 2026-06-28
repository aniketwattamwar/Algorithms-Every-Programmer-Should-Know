# Chapter 7: Knapsack Algorithm

The Knapsack Algorithm, specifically the 0/1 Knapsack Problem, is a classic optimization problem solved using Dynamic Programming. The goal is to maximize the total value of items placed in a knapsack without exceeding its weight capacity.

## Pseudocode

```text
Function Knapsack(W, wt, val, n):
    Create a 2D array K of size (n + 1) x (W + 1)
    
    For i from 0 to n:
        For w from 0 to W:
            If i == 0 or w == 0:
                K[i][w] = 0
            Else if wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w - wt[i-1]], K[i-1][w])
            Else:
                K[i][w] = K[i-1][w]
                
    Return K
```

## Python Code

```python
def knapsack(W, wt, val, n):
    # Initialize DP table
    # Rows: 0 to n (number of items)
    # Cols: 0 to W (weight capacity)
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
                
    return K

if __name__ == '__main__':
    weights = [2, 4, 1, 5]
    values = [3, 5, 2, 6]
    W = 8
    n = 4

    dp_table = knapsack(W, weights, values, n)

    print("Table of Options:")
    print("T[i, j] | " + " | ".join([f"j={j}" if j == 0 else f"{j}" for j in range(W + 1)]))
    print("-" * 55)
    for i in range(n + 1):
        print(f"  i={i}   | " + " | ".join([f"{dp_table[i][j]}" for j in range(W + 1)]))
```

## Example: Finding the Table of Options

Given the Knapsack problem:
- Weights = `{2, 4, 1, 5}`
- Values = `{3, 5, 2, 6}`
- `n = 4`
- `W = 8`

Here is the completed DP Table (Table of Options) `T[i, j]`:

| `T[i, j]` | `j=0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **i=0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 0 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| **2** | 0 | 0 | 3 | 3 | 5 | 5 | 8 | 8 | 8 |
| **3** | 0 | 2 | 3 | 5 | 5 | 7 | 8 | 10 | 10 |
| **4** | 0 | 2 | 3 | 5 | 5 | 7 | 8 | 10 | 11 |

## Real-world applications
- Cloud resource allocation
- Portfolio optimization

## Alternatives and Key Insights
Dynamic programming avoids overlapping subproblems by storing previously computed answers. 
