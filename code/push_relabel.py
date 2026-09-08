from collections import deque


class PushRelabel:
    """Compute a maximum flow in a directed capacitated graph."""

    def __init__(self, num_vertices):
        if num_vertices <= 0:
            raise ValueError("num_vertices must be positive")

        self.V = num_vertices
        self.capacity = [[0] * num_vertices for _ in range(num_vertices)]
        self.flow = [[0] * num_vertices for _ in range(num_vertices)]
        self.height = [0] * num_vertices
        self.excess = [0] * num_vertices

    def add_edge(self, u, v, cap):
        """Add capacity from vertex ``u`` to vertex ``v``."""
        self._validate_vertex(u)
        self._validate_vertex(v)
        if cap < 0:
            raise ValueError("cap must be non-negative")

        self.capacity[u][v] += cap

    def _validate_vertex(self, vertex):
        if not 0 <= vertex < self.V:
            raise IndexError("vertex is outside the graph")

    def _push(self, u, v):
        residual = self.capacity[u][v] - self.flow[u][v]
        amount = min(self.excess[u], residual)

        self.flow[u][v] += amount
        self.flow[v][u] -= amount
        self.excess[u] -= amount
        self.excess[v] += amount
        return amount

    def _relabel(self, u):
        neighbor_heights = [
            self.height[v]
            for v in range(self.V)
            if self.capacity[u][v] - self.flow[u][v] > 0
        ]
        if not neighbor_heights:
            return False

        self.height[u] = min(neighbor_heights) + 1
        return True

    def max_flow(self, source, sink):
        """Return the maximum flow from ``source`` to ``sink``."""
        self._validate_vertex(source)
        self._validate_vertex(sink)
        if source == sink:
            raise ValueError("source and sink must be different vertices")

        self.flow = [[0] * self.V for _ in range(self.V)]
        self.height = [0] * self.V
        self.excess = [0] * self.V
        self.height[source] = self.V

        for vertex in range(self.V):
            if vertex != source and self.capacity[source][vertex] > 0:
                self.excess[source] = self.capacity[source][vertex]
                self._push(source, vertex)

        active_queue = deque(
            vertex
            for vertex in range(self.V)
            if vertex not in (source, sink) and self.excess[vertex] > 0
        )

        while active_queue:
            u = active_queue.popleft()

            while self.excess[u] > 0:
                pushed = False
                for v in range(self.V):
                    residual = self.capacity[u][v] - self.flow[u][v]
                    if residual > 0 and self.height[u] == self.height[v] + 1:
                        was_inactive = self.excess[v] == 0
                        self._push(u, v)
                        pushed = True

                        if (
                            v not in (source, sink)
                            and was_inactive
                            and self.excess[v] > 0
                        ):
                            active_queue.append(v)

                        if self.excess[u] == 0:
                            break

                if not pushed and not self._relabel(u):
                    break

        return self.excess[sink]


def build_book_graph():
    """Return the graph shown in the book's push-relabel example."""
    graph = PushRelabel(4)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 5)
    graph.add_edge(1, 2, 15)
    graph.add_edge(1, 3, 10)
    graph.add_edge(2, 3, 10)
    return graph


def print_edges(graph):
    """Print the directed edges with positive capacities."""
    for u in range(graph.V):
        for v in range(graph.V):
            if graph.capacity[u][v] > 0:
                print(f"  {u} -> {v}: capacity = {graph.capacity[u][v]}")


if __name__ == "__main__":
    print("Example 1: book graph")
    book_graph = build_book_graph()
    print_edges(book_graph)
    print("Maximum flow from 0 to 3:", book_graph.max_flow(0, 3))
    print()

    print("Example 2: a network that can reroute flow")
    rerouting_graph = PushRelabel(6)
    for edge in ((0, 1, 10), (0, 2, 10), (1, 2, 2), (1, 3, 4),
                 (1, 4, 8), (2, 4, 9), (3, 5, 10), (4, 3, 6),
                 (4, 5, 10)):
        rerouting_graph.add_edge(*edge)
    print_edges(rerouting_graph)
    print("Maximum flow from 0 to 5:", rerouting_graph.max_flow(0, 5))
    print()

    print("Example 3: disconnected sink")
    disconnected_graph = PushRelabel(4)
    disconnected_graph.add_edge(0, 1, 8)
    disconnected_graph.add_edge(1, 2, 4)
    print_edges(disconnected_graph)
    print("Maximum flow from 0 to 3:", disconnected_graph.max_flow(0, 3))