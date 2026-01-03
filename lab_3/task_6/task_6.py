class Node[T]:
    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] = self

    def __str__(self):
        # return f"{self.value}->{self.next.value}"
        return str(self.value)


class CircularLinkedList[T]:
    def __init__(self):
        self._size = 0
        self._back: Node[T] | None = None

    def insert(self, value: T, index: int) -> None:
        if not 0 <= index <= self._size:
            raise IndexError("Index out of bounds.")

        node = Node(value)

        if self._size == 0:
            node.next = node
            self._back = node
        else:
            current = self._back
            for _ in range(index):
                current = current.next

            node.next = current.next
            current.next = node

            if index == self._size:
                self._back = node

        self._size += 1

    def remove(self, index: int) -> T:
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds.")

        if self._size == 1:
            node = self._back
            self._back = None
        else:
            current = self._back
            for _ in range(index):
                current = current.next

            node = current.next
            current.next = node.next

            if index == self._size - 1:
                self._back = current

        self._size -= 1
        return node.value

    def index(self, value: T) -> int:
        current = self._back

        for i in range(self._size):
            if current.value == value:
                return (i - 1) % self._size
            current = current.next

        return -1

    def __len__(self):
        return self._size

    def is_empty(self) -> bool:
        return self._size < 1

    def __str__(self):
        elements = []

        if self._size < 1:
            return "[]"

        current = self._back.next
        for _ in range(self._size):
            elements.append(current)
            current = current.next

        return f"[{", ".join(map(str, elements))}]"


if __name__ == "__main__":
    circular_linked_list = CircularLinkedList[int]()
    print(circular_linked_list)  # []

    circular_linked_list.insert(5, 0)
    circular_linked_list.insert(6, 1)
    circular_linked_list.insert(7, 0)
    print(circular_linked_list)  # [7, 5, 6]

    circular_linked_list.insert(10, 3)
    print(circular_linked_list)  # [7, 5, 6, 10]

    circular_linked_list.remove(0)
    print(circular_linked_list)  # [5, 6, 10]
    circular_linked_list.remove(1)
    print(circular_linked_list)  # [5, 10]
    circular_linked_list.remove(1)
    print(circular_linked_list)  # [5]

    circular_linked_list.insert(6, 1)
    circular_linked_list.insert(7, 2)
    print(circular_linked_list)  # [5, 6, 7]

    print(circular_linked_list.index(6))  # 1
    print(circular_linked_list.index(7))  # 2
    print(circular_linked_list.index(10))  # -1
