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
