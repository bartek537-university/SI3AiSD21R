def heap_sort[T](values: list[T]) -> None:
    for i in range(1, len(values)):
        value = values[i]
        child_index = i

        while child_index > 0:
            parent_index = (child_index - 1) // 2

            if values[parent_index] >= value:
                break

            values[child_index] = values[parent_index]
            child_index = parent_index

        values[child_index] = value

    for i in range(len(values)):
        leaf_index = len(values) - i - 1
        values[0], values[leaf_index] = values[leaf_index], values[0]

        parent_index = 0

        while parent_index * 2 + 1 < leaf_index:
            left_index = parent_index * 2 + 1
            right_index = parent_index * 2 + 2

            if right_index < leaf_index and values[left_index] < values[right_index]:
                max_index = right_index
            else:
                max_index = left_index

            if values[parent_index] >= values[max_index]:
                break

            values[parent_index], values[max_index] = values[max_index], values[parent_index]
            parent_index = max_index
