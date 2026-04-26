import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian(cost_matrix, workers, tasks):
    
    cost_array = np.array(cost_matrix)
    row_ind, col_ind = linear_sum_assignment(cost_array)
    
    total_cost = 0
    print("--- O(n^3) Solution ---")
    
    for worker_idx, task_idx in zip(row_ind, col_ind):
        cost = cost_matrix[worker_idx][task_idx]
        total_cost += cost
        print(f"{workers[worker_idx]} is assigned to {tasks[task_idx]} (Cost: {cost})")
        
    print(f"Total Minimum Cost: {total_cost}")

# Your Matrix Data
workers = ["Alice", "Bob", "Carol"]
tasks = ["Kitchen", "Floors", "Windows"]
cost_matrix = [
    [15, 10, 9],  # Alice
    [9,  15, 10], # Bob
    [10, 12, 8]   # Carol
]

hungarian(cost_matrix, workers, tasks)