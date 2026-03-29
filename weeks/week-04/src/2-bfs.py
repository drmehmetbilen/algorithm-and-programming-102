from collections import deque


def bfs_traversal(graph, start):
    """
    Return the BFS visit order starting from start.
    """
    if start not in graph:
        return []

    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def bfs_distances(graph, start):
    """
    Return shortest distances from start in an unweighted graph.
    """
    if start not in graph:
        return {}

    distances = {start: 0}
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for neighbor in graph.get(current, []):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances


def shortest_path_unweighted(graph, start, target):
    """
    Return one shortest path from start to target, else None.
    """
    if start not in graph or target not in graph:
        return None

    parents = {start: None}
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current == target:
            break

        for neighbor in graph.get(current, []):
            if neighbor not in parents:
                parents[neighbor] = current
                queue.append(neighbor)

    if target not in parents:
        return None

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()
    return path


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "G"],
        "F": ["C", "H"],
        "G": ["E"],
        "H": ["F"],
    }

    print("BFS order from A:", bfs_traversal(graph, "A"))
    print("Distances from A:", bfs_distances(graph, "A"))
    print("Shortest path A -> G:", shortest_path_unweighted(graph, "A", "G"))
    print("Shortest path A -> Z:", shortest_path_unweighted(graph, "A", "Z"))
