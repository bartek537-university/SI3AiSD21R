class PriorityQueue[T]:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("Capacity must be a positive integer.")

        self._size = 0
        self._capacity = capacity
        self._elements: list[tuple[int, float] | None] = [None] * capacity

    def enqueue(self, value: T, priority: float) -> None:
        if self._size >= self._capacity:
            raise OverflowError("Queue is full.")

        i = self._size

        while i > 0:
            if self._elements[i - 1][1] > priority:
                self._elements[i] = self._elements[i - 1]
                i -= 1
            else:
                break

        self._elements[i] = (value, priority)
        self._size += 1

    def dequeue(self) -> T:
        if self._size < 1:
            raise OverflowError("Queue is empty.")

        dequeued_value = self._elements[self._size - 1][0]
        self._size -= 1

        return dequeued_value

    def peek(self) -> T:
        if self._size < 1:
            raise OverflowError("Queue is empty.")
        return self._elements[self._size - 1][0]

    def __len__(self):
        return self._size

    def is_empty(self) -> bool:
        return self._size < 1

    def is_full(self) -> bool:
        return self._size >= self._capacity

    def __str__(self):
        elements = map(str, self._elements[:self._size])
        return f"[{", ".join(elements)}]"


def print_queue_buffer(queue: PriorityQueue) -> None:
    # noinspection PyProtectedMember
    print(f"Buffer: {queue._elements}\tQueue: {queue}")


if __name__ == "__main__":
    queue = PriorityQueue[int](5)
    print_queue_buffer(queue)  # Buffer: [None, None, None, None, None]	Stack: []

    queue.enqueue(6, 1)
    queue.enqueue(8, 5)
    queue.enqueue(4, 3)

    print_queue_buffer(queue)  # Buffer: [(6, 1), (4, 3), (4, 4), (8, 5), None]	Stack: [(6, 1), (4, 3), (4, 4), (8, 5)]

    print(queue.peek())  # 8

    queue.enqueue(3, 2)

    print(queue.peek())  # 8

    print_queue_buffer(queue)
    print(queue)  # Buffer: [(6, 1), (3, 2), (4, 3), (4, 4), (8, 5)]	Stack: [(6, 1), (3, 2), (4, 3), (4, 4), (8, 5)]

    print(queue.dequeue())  # 8
    print(queue.dequeue())  # 4
    print(queue.dequeue())  # 4

    print_queue_buffer(queue)  # Buffer: [(6, 1), (3, 2), (4, 3), (4, 4), (8, 5)]	Stack: [(6, 1), (3, 2)]

    queue.enqueue(5, 1.5)

    print_queue_buffer(queue)  # Buffer: [(6, 1), (5, 1.5), (3, 2), (4, 4), (8, 5)]	Stack: [(6, 1), (5, 1.5), (3, 2)]
