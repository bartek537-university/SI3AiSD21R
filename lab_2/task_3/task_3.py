from typing import Callable


def random_lag_fib(n: int, j: int, k: int, op: Callable[[int, int], int], x: list[int]) -> None:
    assert len(x) >= j > k > 0

    l = len(x)

    for i in range(n):
        x1 = x[(i - j) % l]
        x2 = x[(i - k) % l]

        result = op(x1, x2)

        x[i % l] = result

        print(result)


random_lag_fib(15, 4, 2, lambda a, b: (a + b) % 7, [4, 8, 7, 1])
