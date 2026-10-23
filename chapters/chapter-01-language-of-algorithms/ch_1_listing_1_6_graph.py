from collections import deque


def graph_dfs(graph, start_node):
    """Return an iterative depth-first traversal of an adjacency-list graph."""
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


def graph_bfs(graph, start_node):
    """Return an iterative breadth-first traversal of an adjacency-list graph."""
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


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("Depth-first:", graph_dfs(graph, "A"))
    print("Breadth-first:", graph_bfs(graph, "A"))


if __name__ == "__main__":
    main()
