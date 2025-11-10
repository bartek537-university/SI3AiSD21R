from typing import Callable


def random_fib(n: int, op: Callable[[int, int], int], x1: int, x2: int) -> None:
    for i in range(n):
        temp = x2
        x2 = op(x1, x2)
        x1 = temp

        print(x2)


random_fib(20, lambda a, b: (a + b) % 4, 0, 1)
