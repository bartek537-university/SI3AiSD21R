import math


def prim(graph: list[list[float]]) -> list[list[float]]:
    weights: list[float] = []  # cheapest_cost
    history: list[int] = []  # cheapest_edge

    for i in range(len(graph)):
        weights.append(math.inf)
        history.append(-1)

    pending_vertices = set[int]()

    for i in range(len(graph)):
        pending_vertices.add(i)

    weights[0] = 0

    while pending_vertices:
        vertex = min(pending_vertices, key=lambda pending_vertex: weights[pending_vertex])
        pending_vertices.remove(vertex)

        for neighbor, distance in enumerate(graph[vertex]):
            if distance <= 0 or neighbor not in pending_vertices:
                continue

            if distance < weights[neighbor]:
                weights[neighbor] = distance
                history[neighbor] = vertex

    edges = [[0.] * len(graph) for _ in range(len(graph))]

    for vertex, weight in enumerate(weights):
        if weight == math.inf:
            continue

        neighbor = history[vertex]

        edges[vertex][neighbor] = weight
        edges[neighbor][vertex] = weight

    return edges


if __name__ == "__main__":
    graph = [
        # A B  C  D  E  F  G
        [0, 8, 0, 0, 0, 0, 0],  # A
        [8, 0, 4, 0, 7, 0, 0],  # B
        [0, 4, 0, 3, 6, 9, 0],  # C
        [0, 0, 3, 0, 0, 12, 0],  # D
        [0, 7, 6, 0, 0, 10, 0],  # E
        [0, 0, 9, 12, 10, 0, 4],  # F
        [0, 0, 0, 0, 0, 4, 0],  # G
    ]

    print(prim(graph))
