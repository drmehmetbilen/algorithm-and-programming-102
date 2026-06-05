import heapq


def dijkstra_distances(graph, start):
    """
    Return shortest distances from start using Dijkstra's algorithm.
    """
    if start not in graph:
        return {}

    distances = {node: float("inf") for node in graph}
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
                heapq.heappush(heap, (candidate, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "F": 6},
        "E": {"C": 10, "D": 2, "F": 3},
        "F": {"D": 6, "E": 3},
    }

    print("Distances from A:", dijkstra_distances(graph, "A"))
    print("Distances from C:", dijkstra_distances(graph, "C"))
