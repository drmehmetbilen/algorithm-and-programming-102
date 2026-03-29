def dfs_recursive(graph, start, visited=None, order=None):
    """
    Recursive DFS traversal.
    """
    if start not in graph:
        return []

    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, order)

    return order


def dfs_iterative(graph, start):
    """
    Iterative DFS traversal using a stack.
    """
    if start not in graph:
        return []

    visited = {start}
    stack = [start]
    order = []

    while stack:
        current = stack.pop()
        order.append(current)

        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return order


if __name__ == "__main__":
    traversal_graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "G"],
        "F": ["C", "H"],
        "G": ["E"],
        "H": ["F"],
    }

    print("Recursive DFS from A:", dfs_recursive(traversal_graph, "A"))
    print("Iterative DFS from A:", dfs_iterative(traversal_graph, "A"))

