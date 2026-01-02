class Queue[T]:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("Capacity must be a positive integer.")

        self._start_index = 0
        self._size = 0
        self._capacity = capacity
        self._buffer = [None] * capacity

    def enqueue(self, value: T) -> None:
        if self._size >= self._capacity:
            raise OverflowError("Queue is full.")

        insert_index = (self._start_index + self._size) % self._capacity
        self._buffer[insert_index] = value

        self._size += 1

    def dequeue(self) -> T:
        if self._size < 1:
            raise OverflowError("Queue is empty.")

        dequeued_value = self._buffer[self._start_index]

        self._start_index = (self._start_index + 1) % self._capacity
        self._size -= 1

        return dequeued_value

    def peek(self) -> T:
        if self._size < 1:
            raise OverflowError("Queue is empty.")
        return self._buffer[self._start_index]

    def __len__(self):
        return self._size

    def is_empty(self) -> bool:
        return self._size < 1

    def is_full(self) -> bool:
        return self._size >= self._capacity

    def __str__(self):
        elements = [str(self._buffer[(self._start_index + i) % self._capacity]) for i in range(self._size)]
        return f"[{", ".join(elements)}]"


def print_queue_buffer(queue: Queue) -> None:
    # noinspection PyProtectedMember
    print(f"Buffer: {queue._buffer}\tQueue: {queue}")


if __name__ == "__main__":
    queue = Queue[int](5)
    print_queue_buffer(queue)  # Buffer: [None, None, None, None, None]	Stack: []

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print_queue_buffer(queue)  # Buffer: [1, 2, 3, None, None]	Stack: [1, 2, 3]

    print(queue.dequeue())  # 1
    print_queue_buffer(queue)  # Buffer: [1, 2, 3, None, None]	Stack: [2, 3]

    print(queue.dequeue())  # 2
    print(queue.dequeue())  # 3

    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)

    print_queue_buffer(queue)  # Buffer: [8, 9, 10, 6, 7]	Stack: [6, 7, 8, 9, 10]
