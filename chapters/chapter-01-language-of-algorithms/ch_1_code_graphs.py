from collections import deque
from typing import Any


def graph_dfs(graph: dict[Any, list[Any]], start_node: Any) -> list[Any]:
    """Return an iterative depth-first traversal of a graph."""
    if start_node not in graph:
        return []

    stack = [start_node]
    visited = set()
    traversal_output = []

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            traversal_output.append(current_node)

            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_output


def graph_bfs(graph: dict[Any, list[Any]], start_node: Any) -> list[Any]:
    """Return an iterative breadth-first traversal of a graph."""
    if start_node not in graph:
        return []

    queue = deque([start_node])
    visited = {start_node}
    traversal_output = []

    while queue:
        current_node = queue.popleft()
        traversal_output.append(current_node)

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_output


def main() -> None:
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("Depth-first traversal:", graph_dfs(graph, "A"))
    print("Breadth-first traversal:", graph_bfs(graph, "A"))


if __name__ == "__main__":
    main()
