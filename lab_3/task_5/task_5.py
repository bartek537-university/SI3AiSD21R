class Node[T]:
    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] | None = None
        self.previous: Node[T] | None = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList[T]:
    def __init__(self):
        self._size = 0
        self._front: Node[T] | None = None
        self._back: Node[T] | None = None

    def insert(self, value: T, index: int) -> None:
        if not 0 <= index <= self._size:
            raise IndexError("Index out of bounds.")

        node = Node(value)

        if self._size == 0:
            self._front = node
            self._back = node
        elif index == 0:
            node.next = self._front
            self._front.previous = node
            self._front = node
        elif index == self._size:
            node.previous = self._back
            self._back.next = node
            self._back = node
        else:
            current = self._front
            for _ in range(index - 1):
                current = current.next

            node.previous = current
            node.next = current.next
            current.next.previous = node
            current.next = node

        self._size += 1

    def remove(self, index: int) -> T:
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds.")

        if self._size == 1:
            node = self._front
            self._front = None
            self._back = None
        elif index == 0:
            node = self._front
            node.next.previous = None
            self._front = node.next
        elif index == self._size - 1:
            node = self._back
            node.previous.next = None
            self._back = node.previous
        else:
            current: Node[T] = self._front
            for _ in range(index - 1):
                current = current.next

            node = current.next
            node.next.previous = current
            current.next = node.next

        self._size -= 1
        return node.value

    def index(self, value: T) -> int:
        current = self._front

        for i in range(self._size):
            if current.value == value:
                return i
            current = current.next

        return -1

    def __len__(self):
        return self._size

    def is_empty(self) -> bool:
        return self._size < 1

    def __str__(self):
        elements = []

        current = self._front
        while current:
            elements.append(current)
            current = current.next

        return f"[{", ".join(map(str, elements))}]"


if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList[int]()
    print(doubly_linked_list)

    doubly_linked_list.insert(5, 0)
    doubly_linked_list.insert(6, 1)
    doubly_linked_list.insert(7, 0)
    print(doubly_linked_list)  # [7, 5, 6]

    doubly_linked_list.insert(8, 3)
    doubly_linked_list.insert(9, 4)
    print(doubly_linked_list)  # [7, 5, 6, 8, 9]

    print(doubly_linked_list.remove(0))  # 7
    print(doubly_linked_list)  # [5, 6, 8, 9]
    print(doubly_linked_list.remove(3))  # 9
    print(doubly_linked_list)  # [5, 6, 8]

    print(doubly_linked_list.index(5))  # 0
    print(doubly_linked_list.index(6))  # 1
    print(doubly_linked_list.index(8))  # 2
