import math


def dijkstra(graph: list[list[float]], source: int, destination: int) -> tuple[float, list[int]]:
    weights: list[float] = []
    history: list[int] = []

    for i in range(len(graph)):
        weights.append(math.inf)
        history.append(-1)

    pending_vertices: list[int] = []

    for i in range(len(graph)):
        pending_vertices.append(i)

    weights[source] = 0

    while pending_vertices:
        vertex = min(pending_vertices, key=lambda pending_vertex: weights[pending_vertex])
        pending_vertices.remove(vertex)

        for neighbor, distance in enumerate(graph[vertex]):
            if distance <= 0:
                continue

            calculated_weight = weights[vertex] + distance

            if calculated_weight < weights[neighbor]:
                weights[neighbor] = calculated_weight
                history[neighbor] = vertex

    path = [destination]
    vertex = destination

    while vertex != source:
        vertex = history[vertex]
        path.insert(0, vertex)

    return weights[destination], path


if __name__ == "__main__":
    graph = [
        # A B  C  D  E  F
        [0, 3, 0, 0, 3, 0],  # A
        [0, 0, 1, 0, 0, 0],  # B
        [0, 3, 0, 0, 0, 1],  # C
        [0, 3, 0, 0, 0, 0],  # D
        [0, 0, 0, 0, 0, 2],  # E
        [6, 0, 0, 1, 0, 0],  # F
    ]

    print(dijkstra(graph, 0, 5))
