def knapsack(W, wt, val, n):
    """
    Solves the 0/1 Knapsack problem using Dynamic Programming.
    W: Maximum weight capacity
    wt: List of weights
    val: List of values
    n: Number of items
    """
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
    # Problem data based on the provided example
    weights = [2, 4, 1, 5]
    values = [3, 5, 2, 6]
    W = 8
    n = 4

    # Generate table
    dp_table = knapsack(W, weights, values, n)

    # Print table in formatted layout
    print("Table of Options:")
    print("T[i, j] | " + " | ".join([f"j={j}" if j == 0 else f"{j}" for j in range(W + 1)]))
    print("-" * 55)
    for i in range(n + 1):
        print(f"  i={i}   | " + " | ".join([f"{dp_table[i][j]}" for j in range(W + 1)]))
