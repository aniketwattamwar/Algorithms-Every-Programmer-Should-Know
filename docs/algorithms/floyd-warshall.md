# Chapter 9: Floyd-Warshall Algorithm

The Floyd-Warshall algorithm is an algorithm for finding shortest paths in a directed weighted graph with positive or negative edge weights (but with no negative cycles). A single execution of the algorithm will find the lengths (summed weights) of shortest paths between all pairs of vertices.

## Pseudocode

```text
Define infinity as a value larger than any possible path distance.
Initialize a 2D array distance_matrix matching the dimensions of the input graph.

For each row i and column j in the graph:
    If there is a direct edge from i to j, distance_matrix[i][j] = edge_weight
    If i equals j, distance_matrix[i][j] = 0
    Else, distance_matrix[i][j] = infinity

For every vertex k (acting as the intermediate bridge):
    For every vertex i (acting as the start node):
        For every vertex j (acting as the destination node):
            If distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
                Update distance_matrix[i][j] to the new cheaper sum

Return distance_matrix
```
