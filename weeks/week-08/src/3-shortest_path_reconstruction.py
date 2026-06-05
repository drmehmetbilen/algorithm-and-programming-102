import heapq


def dijkstra_with_parents(graph, start):
    """
    Return shortest distances and parent pointers from start.
    """
    if start not in graph:
        return {}, {}

    distances = {node: float("inf") for node in graph}
    parents = {start: None}
    distances[start] = 0

    heap = [(0, start)]
    settled = set()

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node in settled:
            continue

        settled.add(current_node)

        for neighbor, weight in graph.get(current_node, {}).items():
            candidate = current_distance + weight

            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                parents[neighbor] = current_node
                heapq.heappush(heap, (candidate, neighbor))

    return distances, parents


def shortest_path(graph, start, target):
    """
    Return one shortest path and its cost from start to target, else None.
    """
    if start not in graph or target not in graph:
        return None

    distances, parents = dijkstra_with_parents(graph, start)

    if distances[target] == float("inf"):
        return None

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parents.get(current)

    path.reverse()
    return path, distances[target]


if __name__ == "__main__":
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "F": 6},
        "E": {"C": 10, "D": 2, "F": 3},
        "F": {"D": 6, "E": 3},
    }

    print("Shortest path A -> F:", shortest_path(graph, "A", "F"))
    print("Shortest path A -> E:", shortest_path(graph, "A", "E"))
    print("Shortest path B -> Z:", shortest_path(graph, "B", "Z"))
