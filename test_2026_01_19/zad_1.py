from datetime import datetime
from typing import Callable


def fib(n: int, op: Callable[[int, int], int], x1: int, x2: int) -> None:
    for i in range(n):
        temp = x2
        x2 = op(x1, x2)
        x1 = temp

        result = x2

        # print(result)


def lfg(n: int, j: int, k: int, op: Callable[[int, int], int], x: list[int]) -> None:
    assert len(x) >= j > k > 0

    l = len(x)

    for i in range(n):
        x1 = x[(i - j) % l]
        x2 = x[(i - k) % l]

        result = op(x1, x2)

        x[i % l] = result

        # print(result)


def measure_execution_time_seconds(fn: Callable[[], None]) -> float:
    start_time = datetime.now()
    fn()
    end_time = datetime.now()

    return (end_time - start_time).total_seconds()


if __name__ == "__main__":
    sample_size = 100000
    operation = lambda a, b: (a + b) % 10

    fib_s = measure_execution_time_seconds(lambda: fib(sample_size, operation, 0, 1))
    average_fib_s = fib_s / sample_size

    lfg_s = measure_execution_time_seconds(lambda: lfg(sample_size, 7, 2, operation, [1, 2, 3, 4, 5, 6, 7]))
    average_lfg_s = lfg_s / sample_size

    print(f"Średni czas operacji generatora Fibonacciego wynosi {average_fib_s} s")
    print(f"Średni czas operacji generatora LFG wynosi {average_lfg_s} s")

    # Polecenia print zostały zakomentowane, aby czas wypisywania danych nie wpływało na jakość wyników.

    # Średni czas operacji generatora Fibonacciego wynosi 6.065e-08 s
    # Średni czas operacji generatora LFG wynosi 1.176e-07 s

    # Na podstawie otrzymanych wyników można stawierdzić, że wolniejszy jest generator LFG.
