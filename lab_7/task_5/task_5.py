def merge_sort[T](values: list[T]) -> None:
    temp_values = [None] * len(values)
    _merge_sort(values, temp_values, 0, len(values))


def _merge_sort[T](values: list[T], temp: list[T], start: int, end: int) -> None:
    if end - start < 2:
        return

    middle = (start + end) // 2

    _merge_sort(values, temp, start, middle)
    _merge_sort(values, temp, middle, end)

    head = start
    l, r = start, middle

    while l < middle and r < end:
        if values[l] < values[r]:
            temp[head] = values[l]
            l += 1
        else:
            temp[head] = values[r]
            r += 1
        head += 1

    for i in range(l, middle):
        temp[head] = values[i]
        head += 1

    for i in range(r, end):
        temp[head] = values[i]
        head += 1

    for i in range(start, end):
        values[i] = temp[i]
