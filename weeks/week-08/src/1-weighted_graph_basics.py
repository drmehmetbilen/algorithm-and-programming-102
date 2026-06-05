def build_weighted_graph(edges, directed=False):
    """
    Build a weighted adjacency-list graph from (start, end, weight) tuples.
    """
    graph = {}

    for start, end, weight in edges:
        graph.setdefault(start, {})
        graph.setdefault(end, {})
        graph[start][end] = weight

        if not directed:
            graph[end][start] = weight

    return graph


def path_cost(graph, path):
    """
    Return total cost of a path, or None if the path is invalid.
    """
    if len(path) < 2:
        return 0

    total = 0

    for index in range(len(path) - 1):
        start = path[index]
        end = path[index + 1]

        if end not in graph.get(start, {}):
            return None

        total += graph[start][end]

    return total


def describe_weighted_graph(graph, directed=False):
    """
    Print a readable summary of a weighted graph.
    """
    graph_type = "Directed" if directed else "Undirected"
    print(f"{graph_type} weighted graph")
    print("Nodes:", sorted(graph.keys()))
    print()

    for node in sorted(graph.keys()):
        print(f"{node} -> {graph[node]}")


if __name__ == "__main__":
    weighted_edges = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 1),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 10),
        ("D", "E", 2),
        ("D", "F", 6),
        ("E", "F", 3),
    ]

    graph = build_weighted_graph(weighted_edges, directed=False)
    describe_weighted_graph(graph, directed=False)
    print()
    print("Path cost A -> B -> D -> F:", path_cost(graph, ["A", "B", "D", "F"]))
    print(
        "Path cost A -> C -> B -> D -> E -> F:",
        path_cost(graph, ["A", "C", "B", "D", "E", "F"]),
    )
