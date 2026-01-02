class Stack[T]:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("Capacity must be a positive integer.")

        self._size = 0
        self._capacity = capacity
        self._values: list[int | None] = [None] * capacity

    def push(self, value: T) -> None:
        if self._size >= self._capacity:
            raise OverflowError("Stack is full.")

        self._values[self._size] = value
        self._size += 1

    def pop(self) -> T:
        if self._size < 1:
            raise OverflowError("Stack is empty.")

        popped_value = self._values[self._size - 1]
        self._size -= 1

        return popped_value

    def peek(self) -> T:
        if self._size < 1:
            raise OverflowError("Stack is empty.")
        return self._values[self._size - 1]

    def __len__(self):
        return self._size

    def is_empty(self) -> bool:
        return self._size < 1

    def is_full(self) -> bool:
        return self._size >= self._capacity

    def __str__(self):
        elements = map(str, self._values[:self._size])
        return f"[{", ".join(elements)}]"


def print_stack_buffer(stack: Stack) -> None:
    # noinspection PyProtectedMember
    print(f"Buffer: {stack._values}\tStack: {stack}")


if __name__ == "__main__":
    stack = Stack(5)
    print_stack_buffer(stack)  # Buffer: [None, None, None, None, None]	Stack: []

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print_stack_buffer(stack)  # Buffer: [1, 2, 3, None, None]	Stack: [1, 2, 3]

    print(stack.peek())  # 3
    print(stack.peek())  # 3

    stack.pop()
    print_stack_buffer(stack)  # Buffer: [1, 2, 3, None, None]	Stack: [1, 2]
    stack.pop()
    print_stack_buffer(stack)  # Buffer: [1, 2, 3, None, None]	Stack: [1]

    stack.push(4)
    print_stack_buffer(stack)  # Buffer: [1, 4, 3, None, None]	Stack: [1, 4]

    stack.pop()
    print_stack_buffer(stack)  # Buffer: [1, 4, 3, None, None]	Stack: [1]

    stack.pop()
    stack.push(7)
    print_stack_buffer(stack)  # Buffer: [7, 4, 3, None, None]	Stack: [7]
