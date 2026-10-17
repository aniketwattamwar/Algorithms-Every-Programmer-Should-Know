import itertools

try:
    import numpy as np
    from scipy.optimize import linear_sum_assignment
except ImportError:
    np = None
    linear_sum_assignment = None


import itertools

try:
    import numpy as np
    from scipy.optimize import linear_sum_assignment
except ImportError:
    np = None
    linear_sum_assignment = None


def brute_force_assignment(cost_matrix, workers, tasks):
    """
    Solves the assignment problem using brute force by trying all permutations.
    
    This is used as a fallback when scipy is not available. It finds the minimum
    cost assignment by checking every possible worker-task pairing.
    
    Args:
        cost_matrix (list of lists): 2D list where cost_matrix[i][j] is the cost
                                    of assigning worker i to task j.
        workers (list): List of worker names/identifiers.
        tasks (list): List of task names/identifiers.
    
    Returns:
        tuple: (matches, total_cost) where matches is list of (worker_idx, task_idx)
               pairs and total_cost is the minimum total cost.
    
    Raises:
        ValueError: If there are fewer tasks than workers.
    """
    if len(tasks) < len(workers):
        raise ValueError("Need at least as many tasks as workers for a full assignment.")

    best_cost = None
    best_perm = None

    task_indices = range(len(tasks))
    # Try all possible assignments of workers to tasks
    for permutation in itertools.permutations(task_indices, len(workers)):
        cost = sum(cost_matrix[worker_idx][task_idx] for worker_idx, task_idx in enumerate(permutation))
        if best_cost is None or cost < best_cost:
            best_cost = cost
            best_perm = permutation

    return list(enumerate(best_perm)), best_cost


def hungarian(cost_matrix, workers, tasks):
    """
    Solves the assignment problem using the Hungarian algorithm.
    
    Uses scipy's linear_sum_assignment if available (efficient implementation),
    otherwise falls back to brute force method.
    
    Args:
        cost_matrix (list of lists): 2D list where cost_matrix[i][j] is the cost
                                    of assigning worker i to task j.
        workers (list): List of worker names/identifiers.
        tasks (list): List of task names/identifiers.
    
    Returns:
        tuple: (matches, total_cost) where matches is list of (worker_idx, task_idx)
               pairs and total_cost is the minimum total cost.
    """
    if linear_sum_assignment is not None and np is not None:
        # Use efficient scipy implementation
        cost_array = np.array(cost_matrix)
        row_ind, col_ind = linear_sum_assignment(cost_array)
        matches = list(zip(row_ind.tolist(), col_ind.tolist()))
        total_cost = sum(cost_matrix[row][col] for row, col in matches)
        return matches, total_cost

    # Fallback to brute force if scipy not available
    return brute_force_assignment(cost_matrix, workers, tasks)


def print_assignment(title, cost_matrix, workers, tasks):
    """
    Runs the Hungarian algorithm and prints the optimal assignment with costs.
    
    Args:
        title (str): Title to display for the test case.
        cost_matrix (list of lists): Cost matrix for the assignment problem.
        workers (list): List of worker names.
        tasks (list): List of task names.
    """
    print(f"=== {title} ===")
    matches, total_cost = hungarian(cost_matrix, workers, tasks)
    for worker_idx, task_idx in matches:
        print(f"{workers[worker_idx]} -> {tasks[task_idx]} (Cost: {cost_matrix[worker_idx][task_idx]})")
    print(f"Total minimum cost: {total_cost}\n")


if __name__ == "__main__":
    print("Hungarian Assignment Algorithm Demo\n")

    workers = ["Dev 0", "Dev 1", "Dev 2", "Dev 3"]
    tasks = ["Mod 0", "Mod 1", "Mod 2", "Mod 3"]
    cost_matrix = [
        [10, 19, 8, 15],
        [10, 18, 7, 17],
        [13, 16, 9, 14],
        [12, 19, 8, 18],
    ]
    print_assignment("Test 1: 4x4 Cost Matrix from Book", cost_matrix, workers, tasks)

    workers = ["Alice", "Bob", "Carol"]
    tasks = ["Kitchen", "Floors", "Windows"]
    cost_matrix = [
        [15, 10, 9],
        [9, 15, 10],
        [10, 12, 8],
    ]
    print_assignment("Test 2: Balanced 3x3", cost_matrix, workers, tasks)

