from collections import defaultdict


class BronKerbosch:
    """Find all maximal cliques in an undirected graph."""

    def __init__(self):
        self.graph = defaultdict(set)
        self.maximal_cliques = []

    def add_vertex(self, vertex):
        """Add an isolated vertex to the graph."""
        self.graph[vertex]

    def add_edge(self, u, v):
        """Add an undirected edge between vertices ``u`` and ``v``."""
        if u == v:
            raise ValueError("self-loops are not valid in a simple graph")

        self.graph[u].add(v)
        self.graph[v].add(u)

    def _bron_kerbosch(self, current, candidates, excluded):
        if not candidates and not excluded:
            self.maximal_cliques.append(frozenset(current))
            return

        for vertex in list(candidates):
            neighbors = self.graph[vertex]
            self._bron_kerbosch(
                current | {vertex},
                candidates & neighbors,
                excluded & neighbors,
            )
            candidates.remove(vertex)
            excluded.add(vertex)

    def _bron_kerbosch_with_pivot(self, current, candidates, excluded):
        if not candidates and not excluded:
            self.maximal_cliques.append(frozenset(current))
            return

        pivot_candidates = candidates | excluded
        pivot = max(
            pivot_candidates,
            key=lambda vertex: len(candidates & self.graph[vertex]),
            default=None,
        )
        pivot_neighbors = self.graph[pivot] if pivot is not None else set()

        for vertex in list(candidates - pivot_neighbors):
            neighbors = self.graph[vertex]
            self._bron_kerbosch_with_pivot(
                current | {vertex},
                candidates & neighbors,
                excluded & neighbors,
            )
            candidates.remove(vertex)
            excluded.add(vertex)

    def find_maximal_cliques(self, use_pivot=True):
        """Return all maximal cliques, optionally using pivot optimization."""
        self.maximal_cliques = []
        vertices = set(self.graph)

        if use_pivot:
            self._bron_kerbosch_with_pivot(set(), vertices, set())
        else:
            self._bron_kerbosch(set(), vertices, set())

        return sorted(
            (sorted(clique) for clique in self.maximal_cliques),
            key=lambda clique: (len(clique), clique),
        )


def build_book_graph():
    """Build a graph with three overlapping maximal cliques."""
    graph = BronKerbosch()
    for edge in (
        (1, 2), (1, 3), (2, 3),
        (2, 4), (2, 5), (4, 5),
        (3, 4),
    ):
        graph.add_edge(*edge)
    return graph


def print_cliques(cliques):
    """Print maximal cliques in a readable format."""
    for number, clique in enumerate(cliques, start=1):
        print(f"  Clique {number}: {clique}")


if __name__ == "__main__":
    print("Example 1: overlapping cliques")
    book_graph = build_book_graph()
    print_cliques(book_graph.find_maximal_cliques())
    print()

    print("Example 2: standard algorithm without pivoting")
    standard_graph = BronKerbosch()
    for edge in ((0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4)):
        standard_graph.add_edge(*edge)
    print_cliques(standard_graph.find_maximal_cliques(use_pivot=False))
    print()

    print("Example 3: complete graph and isolated vertex")
    complete_graph = BronKerbosch()
    for edge in (("A", "B"), ("A", "C"), ("B", "C")):
        complete_graph.add_edge(*edge)
    complete_graph.add_vertex("D")
    print_cliques(complete_graph.find_maximal_cliques())