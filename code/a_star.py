"""A* search for weighted graphs.

The example at the bottom uses the six-intersection map from Chapter 12.
"""

import heapq
from collections import defaultdict


class AStar:
    """Find paths in an undirected, weighted graph using A* search."""

    def __init__(self):
        self.graph = defaultdict(list)
        self.heuristics = {}

    def add_edge(self, u, v, weight):
        """Add an undirected, weighted edge between ``u`` and ``v``."""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def set_heuristic(self, node, h_value):
        """Set the estimated remaining cost from ``node`` to the goal."""
        self.heuristics[node] = h_value

    def find_shortest_path(self, start, goal):
        """Return the optimal path and its cost using standard A*.

        For the optimality guarantee, edge weights must be non-negative and
        the heuristic must be admissible (never overestimate the remaining
        cost).
        """
        open_set = [(self.heuristics[start], start)]
        g_score = {start: 0}
        came_from = {}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self._reconstruct_path(came_from, current), g_score[current]

            for neighbor, weight in self.graph[current]:
                tentative_g = g_score[current] + weight

                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristics[neighbor]
                    heapq.heappush(open_set, (f_score, neighbor))

        return None, float("inf")

    def find_shortest_path_weighted(self, start, goal, epsilon=1.0):
        """Return a path using weighted A*.

        Multiplying the heuristic by ``epsilon`` (typically greater than 1)
        may reduce node expansions, but does not preserve the shortest-path
        guarantee.
        """
        open_set = [(epsilon * self.heuristics[start], start)]
        g_score = {start: 0}
        came_from = {}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self._reconstruct_path(came_from, current), g_score[current]

            for neighbor, weight in self.graph[current]:
                tentative_g = g_score[current] + weight

                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + epsilon * self.heuristics[neighbor]
                    heapq.heappush(open_set, (f_score, neighbor))

        return None, float("inf")

    def _reconstruct_path(self, came_from, current):
        """Rebuild a path by following parent pointers from the goal."""
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]


if __name__ == "__main__":
    # Six-intersection map from Chapter 12.
    astar = AStar()
    edges = [
        ("S", "A", 3), ("S", "B", 4), ("A", "B", 2), ("A", "C", 3),
        ("B", "D", 4), ("C", "D", 2), ("C", "G", 5), ("D", "G", 2),
    ]
    for u, v, weight in edges:
        astar.add_edge(u, v, weight)

    heuristics = {"S": 6, "A": 4, "B": 4, "C": 2, "D": 2, "G": 0}
    for node, h_value in heuristics.items():
        astar.set_heuristic(node, h_value)

    path, cost = astar.find_shortest_path("S", "G")
    print("Standard A*:", path, "cost =", cost)
    # Expected: ['S', 'B', 'D', 'G'] with cost 10.

    path, cost = astar.find_shortest_path_weighted("S", "G", epsilon=2.0)
    print("Weighted A* (epsilon=2.0):", path, "cost =", cost)
