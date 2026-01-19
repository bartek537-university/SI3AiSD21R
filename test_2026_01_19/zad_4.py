import random


def quick_sort[T](values: list[T]) -> None:
    _quick_sort(values, 0, len(values))


def _quick_sort[T](values: list[T], start, end) -> None:
    if end - start < 2:
        return

    random_swap_pivot = random.randint(start, end - 1)

    pivot_value = values[random_swap_pivot]
    values[random_swap_pivot], values[end - 1] = values[end - 1], values[random_swap_pivot]

    pivot_index = start

    for i in range(start, end - 1):
        if values[i] < pivot_value:
            values[i], values[pivot_index] = values[pivot_index], values[i]
            pivot_index += 1

    values[end - 1], values[pivot_index] = values[pivot_index], values[end - 1]

    _quick_sort(values, start, pivot_index)
    _quick_sort(values, pivot_index + 1, end)


if __name__ == "__main__":
    # Normalny przykład
    a = [5, 10, 7, -6, 12, 10]
    print(a)  # [5, 10, 7, -6, 12, 10]
    quick_sort(a)
    print(a)  # [-6, 5, 7, 10, 10, 12]

    # Przykład niemożliwy do posortowania
    b = [1] * int(1_000)
    # print(b)
    # quick_sort(b)  # "RecursionError: maximum recursion depth exceeded"
    # print(b)

    # "RecursionError: maximum recursion depth exceeded" występuje już przy 1000 elementów.
    # Sortowanie szybkie działa na zasadzie wyboru elementu "pivota", przeniesieniu elementów od niego mniejszych na lewą stronę tablicy
    # i elementów większych na drugą. Każda z części (niekoniecznie równych!) jest następnie rekurencyjnie sortowana.
    # Niemożliwość posortowania tego przykładu polega na tym, że niezależnie od doboru pivota, żaden z elementów nie zmieni swojego położenia,
    # co oznacza, że w przypadku 1000 elementów, rekurencyjnie zostanie wywołane sortowanie szybkie dla 0 elementów i dla 999 elementów,
    # następnie dla 0 i 998, 0 i 997 i tak dalej. W języku Python spowoduje to przekroczenie maksymalnej głębokości rekursji,
    # a więc błąd programu. Dla takich przypadków algorytm osiąga złożoność czasową O(n^2).
