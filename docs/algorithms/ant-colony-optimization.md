# Chapter 8: Ant colony optimization

Ant Colony Optimization (ACO) is a probabilistic technique for solving computational problems which can be reduced to finding good paths through graphs. It is inspired by the behavior of ants in finding paths from the colony to food.

## Pseudocode

```text
Initialize the graph with physical distances between all nodes (the Nest and the Crumbs).
Initialize the pheromone level on all paths to a baseline value of 1.0.
Set algorithm parameters: number of iterations, number of ants, evaporation rate, and deposit reward.

For each iteration:
    For each ant in the swarm:
        Place the ant at the Nest (starting node).
        While there are still unvisited Crumbs:
            Calculate the probability of moving to each unvisited Crumb based on:
                1. The Pheromone level on the path (historical success)
                2. The Heuristic (1 / distance)
            Roll a weighted digital die to choose the next Crumb.
            Move the ant and mark the Crumb as visited.
        
        Return the ant to the Nest to complete the full loop.
        Calculate the total distance of the ant's tour.

    Evaporate pheromones:
        Reduce the pheromone level on ALL paths in the entire graph by the evaporation rate (e.g., 50%).

    Deposit pheromones:
        For each ant:
            Calculate the deposit amount (Reward Amount / Total Tour Distance).
            Add this deposit strictly to the paths that specific ant traversed.

    Track the absolute shortest tour found in this generation.

Return the global shortest tour and its total distance.
```
