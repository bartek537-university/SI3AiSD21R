def bubble_sort[T](values: list[T]) -> None:
    for i in range(len(values) - 1):
        any_swaps_occurred = False

        for j in range(len(values) - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                any_swaps_occurred = True

        if not any_swaps_occurred:
            break
