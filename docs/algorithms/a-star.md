# Chapter 12: A* algorithm

## Overview

A* is an informed graph-search algorithm for finding a least-cost path from a
start node to a goal. It prioritizes nodes by the estimated total route cost
$$f(n) = g(n) + h(n),$$
where $g(n)$ is the cost already paid to reach node $n$ and $h(n)$ estimates
the remaining cost to the goal. An admissible heuristic never overestimates
that remaining cost; with non-negative edge costs, standard A* then finds an
optimal path.

## Pseudocode

```text
function A_STAR(start, goal):
	open_set = priority queue ordered by f, initially containing start
	g[start] = 0
	f[start] = h(start)
	came_from = empty map

	while open_set is not empty:
		current = node in open_set with the smallest f

		if current == goal:
			return reconstruct_path(came_from, current)

		remove current from open_set

		for each neighbor of current:
			tentative_g = g[current] + cost(current, neighbor)

			if neighbor has no g value, or tentative_g < g[neighbor]:
				came_from[neighbor] = current
				g[neighbor] = tentative_g
				f[neighbor] = tentative_g + h(neighbor)
				add neighbor to open_set (or update its priority)

	return "no path exists"
```

The implementation uses a heap-backed priority queue. When a better route to
a node is found, it pushes a new queue entry rather than modifying an entry in
place. It returns both the reconstructed path and its total cost; an unreachable
goal returns `(None, infinity)`.

## Python implementation

The complete implementation, including the six-intersection example, is in
[code/a_star.py](../../code/a_star.py). It provides standard A* and a weighted
A* variant. Weighted A* scales the heuristic by a factor `epsilon`; values
greater than 1 can guide the search more aggressively but give up the standard
optimality guarantee.

Run the file directly to see the example. Standard A* finds the path
`S → B → D → G` with cost 10.

