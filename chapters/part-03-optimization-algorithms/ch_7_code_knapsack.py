import argparse
import itertools
import random
import time


def knapsack(W, wt, val, n):
    """
    Solves the 0/1 Knapsack problem using Dynamic Programming.
    
    Args:
        W (int): Maximum weight capacity of the knapsack.
        wt (list): List of weights of the items.
        val (list): List of values of the items.
        n (int): Number of items available.
        
    Returns:
        list: A 2D array representing the DP table, where K[i][w] contains 
              the maximum value for the first i items with weight limit w.
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


def brute_force(W, wt, val, n):
    """Return the best value by checking every possible item combination."""
    best = 0
    for r in range(n + 1):
        for combo in itertools.combinations(range(n), r):
            total_weight = sum(wt[k] for k in combo)
            if total_weight <= W:
                total_value = sum(val[k] for k in combo)
                best = max(best, total_value)
    return best


def run_benchmark():
    """Compare dynamic programming with brute force for increasing item counts."""
    random.seed(0)
    for n in [10, 15, 20, 24]:
        weights = [random.randint(1, 20) for _ in range(n)]
        values = [random.randint(1, 50) for _ in range(n)]

        start = time.perf_counter()
        dp_table = knapsack(50, weights, values, n)
        dp_time = time.perf_counter() - start

        start = time.perf_counter()
        brute_force_value = brute_force(50, weights, values, n)
        brute_force_time = time.perf_counter() - start

        if dp_table[n][50] != brute_force_value:
            raise AssertionError(f"Knapsack results differ for n={n}")

        print(
            f"n={n:2}: DP {dp_time * 1000:6.2f} ms | "
            f"brute force {brute_force_time * 1000:9.2f} ms"
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the knapsack examples.")
    parser.add_argument(
        "--benchmark",
        action="store_true",
        help="compare dynamic programming with brute force",
    )
    args = parser.parse_args()

    if args.benchmark:
        run_benchmark()
    else:
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
