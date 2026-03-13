def build_adjacency_list(edges, directed=False):
    """
    Build an adjacency-list graph from a list of edge tuples.
    """
    graph = {}

    for start, end in edges:
        graph.setdefault(start, [])
        graph.setdefault(end, [])
        graph[start].append(end)

        if not directed:
            graph[end].append(start)

    return graph


def list_edges(graph, directed=False):
    """
    Return graph edges as a list of tuples.
    """
    edges = []
    seen = set()

    for start, neighbors in graph.items():
        for end in neighbors:
            if directed:
                edges.append((start, end))
            else:
                edge = tuple(sorted((start, end)))
                if edge not in seen:
                    seen.add(edge)
                    edges.append(edge)

    return edges


def degree(graph, node):
    """
    Return degree of a node in an undirected graph.
    """
    return len(graph.get(node, []))


def in_degree(graph, node):
    """
    Return in-degree of a node in a directed graph.
    """
    count = 0
    for neighbors in graph.values():
        count += neighbors.count(node)
    return count


def out_degree(graph, node):
    """
    Return out-degree of a node in a directed graph.
    """
    return len(graph.get(node, []))


def describe_graph(graph, directed=False):
    """
    Print a readable graph summary.
    """
    graph_type = "Directed" if directed else "Undirected"
    print(f"{graph_type} graph")
    print("Nodes:", sorted(graph.keys()))
    print("Edges:", list_edges(graph, directed=directed))
    print()

    for node in sorted(graph.keys()):
        print(f"{node} -> {graph[node]}")

    print()

    for node in sorted(graph.keys()):
        if directed:
            print(
                f"{node}: out-degree={out_degree(graph, node)}, "
                f"in-degree={in_degree(graph, node)}"
            )
        else:
            print(f"{node}: degree={degree(graph, node)}")


if __name__ == "__main__":
    undirected_edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
    ]
    directed_edges = [
        ("A", "B"),
        ("B", "C"),
        ("C", "A"),
        ("C", "D"),
        ("D", "E"),
    ]

    undirected_graph = build_adjacency_list(undirected_edges, directed=False)
    directed_graph = build_adjacency_list(directed_edges, directed=True)

    describe_graph(undirected_graph, directed=False)
    print("-" * 32)
    describe_graph(directed_graph, directed=True)
