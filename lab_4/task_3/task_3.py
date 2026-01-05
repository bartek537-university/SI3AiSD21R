import math
from typing import Callable


def a_star(graph: list[list[float]], source: int, destination: int, approximate_distance: Callable[[int], float]) \
        -> tuple[float, list[int]] | None:
    weights: list[tuple[float, float]] = []  # g_score, f_score
    history: list[int] = []

    for i in range(len(graph)):
        weights.append((math.inf, math.inf))
        history.append(-1)

    pending_vertices = set[int]([source])

    weights[source] = (0, approximate_distance(source))

    while pending_vertices:
        vertex = min(pending_vertices, key=lambda pending_vertex: weights[pending_vertex][1])

        if vertex == destination:
            break

        pending_vertices.remove(vertex)

        for neighbor, distance in enumerate(graph[vertex]):
            if distance <= 0:
                continue

            calculated_weight = weights[vertex][0] + distance

            if calculated_weight < weights[neighbor][0]:
                weights[neighbor] = (calculated_weight, calculated_weight + approximate_distance(neighbor))
                history[neighbor] = vertex
                pending_vertices.add(neighbor)

    if not pending_vertices:
        return None

    path = []
    vertex = destination

    while vertex != -1:
        path.insert(0, vertex)
        vertex = history[vertex]

    return weights[destination][0], path


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

    print(a_star(graph, 0, 5, lambda vertex: vertex / 5))
