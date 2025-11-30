def insertion_sort[T](values: list[T]) -> None:
    for i in range(1, len(values)):
        current = values[i]
        j = i

        while j > 0 and values[j - 1] > current:
            values[j] = values[j - 1]
            j -= 1

        values[j] = current
