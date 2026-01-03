class Node[T]:
    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] = self
        self.previous: Node[T] = self

    def __str__(self):
        return str(self.value)


class SentinelDoublyLinkedList[T]:
    def __init__(self):
        self._size = 0

        sentinel = Node(value=None)
        sentinel.previous = sentinel
        sentinel.next = sentinel

        self._sentinel = Node[T](None)

    def insert(self, value: T, index: int) -> None:
        if not 0 <= index <= self._size:
            raise IndexError("Index out of bounds.")

        node = Node(value)

        current = self._sentinel
        for _ in range(index):
            current = current.next

        node.previous = current
        node.next = current.next
        current.next.previous = node
        current.next = node

        self._size += 1

    def remove(self, index: int) -> T:
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds.")

        current = self._sentinel
        for _ in range(index):
            current = current.next

        node = current.next
        node.next.previous = current
        current.next = node.next

        self._size -= 1
        return node.value

    def index(self, value: T) -> int:
        current = self._sentinel.next
        index = 0

        while current is not self._sentinel:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return -1

    def __len__(self):
        return self._size

    def is_empty(self) -> bool:
        return self._size < 1

    def __str__(self):
        elements = []

        current = self._sentinel.next
        while current != self._sentinel:
            elements.append(current)
            current = current.next

        return f"[{", ".join(map(str, elements))}]"


if __name__ == "__main__":
    sentinel_doubly_linked_list = SentinelDoublyLinkedList[int]()
    print(sentinel_doubly_linked_list)

    sentinel_doubly_linked_list.insert(5, 0)
    sentinel_doubly_linked_list.insert(6, 1)
    sentinel_doubly_linked_list.insert(7, 0)
    print(sentinel_doubly_linked_list)  # [7, 5, 6]

    sentinel_doubly_linked_list.insert(8, 3)
    sentinel_doubly_linked_list.insert(9, 4)
    print(sentinel_doubly_linked_list)  # [7, 5, 6, 8, 9]

    print(sentinel_doubly_linked_list.remove(0))  # 7
    print(sentinel_doubly_linked_list)  # [5, 6, 8, 9]
    print(sentinel_doubly_linked_list.remove(3))  # 9
    print(sentinel_doubly_linked_list)  # [5, 6, 8]

    print(sentinel_doubly_linked_list.index(5))  # 0
    print(sentinel_doubly_linked_list.index(6))  # 1
    print(sentinel_doubly_linked_list.index(8))  # 2
