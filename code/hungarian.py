import itertools

try:
    import numpy as np
    from scipy.optimize import linear_sum_assignment
except ImportError:
    np = None
    linear_sum_assignment = None


def brute_force_assignment(cost_matrix, workers, tasks):
    if len(tasks) < len(workers):
        raise ValueError("Need at least as many tasks as workers for a full assignment.")

    best_cost = None
    best_perm = None

    task_indices = range(len(tasks))
    for permutation in itertools.permutations(task_indices, len(workers)):
        cost = sum(cost_matrix[worker_idx][task_idx] for worker_idx, task_idx in enumerate(permutation))
        if best_cost is None or cost < best_cost:
            best_cost = cost
            best_perm = permutation

    return list(enumerate(best_perm)), best_cost


def hungarian(cost_matrix, workers, tasks):
    if linear_sum_assignment is not None and np is not None:
        cost_array = np.array(cost_matrix)
        row_ind, col_ind = linear_sum_assignment(cost_array)
        matches = list(zip(row_ind.tolist(), col_ind.tolist()))
        total_cost = sum(cost_matrix[row][col] for row, col in matches)
        return matches, total_cost

    return brute_force_assignment(cost_matrix, workers, tasks)


def print_assignment(title, cost_matrix, workers, tasks):
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

