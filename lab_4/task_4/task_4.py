import math

Edge = tuple[int, int, float]


def floyd_warshall(edges: list[Edge], size: int) -> list[list[float]]:
    distances = [[math.inf] * size for _ in range(size)]

    for source, destination, distance in edges:
        distances[source][destination] = distance

    for i in range(size):
        distances[i][i] = 0

    for k in range(size):
        for i in range(size):
            for j in range(size):
                calculated_distance = distances[i][k] + distances[k][j]

                if calculated_distance < distances[i][j]:
                    distances[i][j] = calculated_distance

    return distances


if __name__ == "__main__":
    edges = [
        (0, 2, -2),
        (2, 3, 2),
        (3, 1, -1),
        (1, 0, 4),
        (1, 2, 3),
    ]

    print(floyd_warshall(edges, 4))
