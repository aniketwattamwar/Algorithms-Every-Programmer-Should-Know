import random

def choose_next_node(current_node, unvisited_crumbs, distances, pheromones, alpha=1.0, beta=1.0):
    """
    Calculates probabilities and selects the next node using the State Transition Rule.
    
    Args:
        current_node (int): The node the ant is currently standing on.
        unvisited_crumbs (list): Nodes the ant hasn't visited yet.
        distances (list of lists): 2D matrix of physical distances between nodes.
        pheromones (list of lists): 2D matrix of current pheromone weights.
        alpha (float): Tuning parameter for pheromone importance.
        beta (float): Tuning parameter for heuristic importance.
        
    Returns:
        int: The selected next node.
    """
    probabilities = []
    total_score = 0.0

    # Calculate the raw score (Pheromone * Heuristic) for each available path
    for crumb in unvisited_crumbs:
        pheromone_level = pheromones[current_node][crumb] ** alpha
        # Note: distances[current_node][crumb] should be > 0
        heuristic = (1.0 / distances[current_node][crumb]) ** beta
        
        score = pheromone_level * heuristic
        probabilities.append((crumb, score))
        total_score += score

    # Normalize to percentages and roll the weighted digital die
    random_roll = random.uniform(0, total_score)
    cumulative = 0.0

    for crumb, score in probabilities:
        cumulative += score
        if cumulative >= random_roll:
            return crumb

    # Fallback in case of floating-point rounding errors
    return unvisited_crumbs[-1]


def ant_colony_optimization(distances, num_ants, iterations, decay_rate=0.5, reward=100.0):
    """
    Executes the Ant Colony Optimization algorithm to find the shortest tour.

    Args:
        distances (list of lists): 2D matrix of distances between nodes.
        num_ants (int): Size of the swarm per iteration.
        iterations (int): Number of generations to run.
        decay_rate (float): Percentage of pheromones to evaporate (0.0 to 1.0).
        reward (float): Constant used to calculate pheromone deposit.

    Returns:
        tuple: (best_tour_list, best_distance_float)
    """
    num_nodes = len(distances)
    
    # Initialize baseline pheromones to 1.0 for all paths
    pheromones = [[1.0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    global_best_tour = None
    global_best_distance = float('inf')

    # Index 0 is strictly defined as the Nest, just like Node A on the whiteboard
    nest_node = 0 

    for _ in range(iterations):
        all_tours = []

        # Step 1: Simulate the swarm building their paths
        for _ in range(num_ants):
            # All remaining indices (1 through n) are the Crumbs
            unvisited_crumbs = list(range(1, num_nodes)) 
            current_node = nest_node
            
            tour = [current_node]
            tour_distance = 0.0

            # Ant travels until all crumbs are collected
            while unvisited_crumbs:
                next_node = choose_next_node(current_node, unvisited_crumbs, distances, pheromones)
                tour_distance += distances[current_node][next_node]
                tour.append(next_node)
                unvisited_crumbs.remove(next_node)
                current_node = next_node

            # Ant returns home to the Nest to complete the loop
            tour_distance += distances[current_node][nest_node]
            tour.append(nest_node)
            all_tours.append((tour, tour_distance))

            # Track the absolute best path found
            if tour_distance < global_best_distance:
                global_best_distance = tour_distance
                global_best_tour = tour

        # Step 2: Evaporation (Negative Feedback)
        for i in range(num_nodes):
            for j in range(num_nodes):
                pheromones[i][j] *= (1.0 - decay_rate)

        # Step 3: Deposit (Positive Feedback)
        for tour, tour_distance in all_tours:
            deposit_amount = reward / tour_distance
            
            # Apply deposit strictly to the edges the ant traversed
            for i in range(len(tour) - 1):
                from_node = tour[i]
                to_node = tour[i + 1]
                
                # Update both directions for an undirected graph
                pheromones[from_node][to_node] += deposit_amount
                pheromones[to_node][from_node] += deposit_amount

    return global_best_tour, global_best_distance

if __name__ == "__main__":
    # Example distance matrix for testing (symmetric graph)
    # The nodes could be A, B, C, D where A is node 0 (nest).
    test_distances = [
        [0.0, 10.0, 15.0, 20.0],
        [10.0, 0.0, 35.0, 25.0],
        [15.0, 35.0, 0.0, 30.0],
        [20.0, 25.0, 30.0, 0.0]
    ]
    
    best_tour, best_distance = ant_colony_optimization(
        distances=test_distances, 
        num_ants=10, 
        iterations=100, 
        decay_rate=0.5, 
        reward=100.0
    )
    
    print("Best Tour:", best_tour)
    print("Best Distance:", best_distance)
