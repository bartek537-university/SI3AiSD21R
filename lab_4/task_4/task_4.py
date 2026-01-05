import math

Edge = tuple[int, int, float]


def floyd_warshall(edges: list[Edge]) -> list[list[float]]:
    size = max(max(edge[0], edge[1]) for edge in edges) + 1
    distances = [[math.inf] * size for _ in range(size)]

    for source, destination, distance in edges:
        distances[source][destination] = distance

    for y in range(size):
        distances[y][y] = 0

    for k in range(size):
        for y in range(size):
            for x in range(size):
                calculated_distance = distances[y][k] + distances[k][x]

                if calculated_distance < distances[y][x]:
                    distances[y][x] = calculated_distance

    return distances


if __name__ == "__main__":
    edges = [
        (0, 2, -2),
        (2, 3, 2),
        (3, 1, -1),
        (1, 0, 4),
        (1, 2, 3),
    ]

    print(floyd_warshall(edges))
