class Node[T]:
    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] | None = None

    def __str__(self):
        return str(self.value)


class SinglyLinkedList[T]:
    def __init__(self):
        self._size = 0
        self._root: Node[T] | None = None

    def insert(self, value: T, index: int) -> None:
        if not 0 <= index <= self._size:
            raise IndexError("Index out of bounds.")

        node = Node(value)

        if index == 0:
            node.next = self._root
            self._root = node
        else:
            current = self._root
            for _ in range(index - 1):
                current = current.next

            node.next = current.next
            current.next = node

        self._size += 1

    def remove(self, index: int) -> T:
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds.")

        if index == 0:
            node = self._root
            self._root = node.next
        else:
            current = self._root
            for _ in range(index - 1):
                current = current.next

            node = current.next
            current.next = node.next

        self._size -= 1
        return node.value

    def index(self, value: T) -> int:
        current = self._root

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

        current = self._root
        while current:
            elements.append(current)
            current = current.next

        return f"[{", ".join(map(str, elements))}]"


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList[int]()
    print(singly_linked_list)  # []

    singly_linked_list.insert(5, 0)
    singly_linked_list.insert(6, 1)
    singly_linked_list.insert(7, 0)
    print(singly_linked_list)  # [7, 5, 6]

    singly_linked_list.insert(10, 3)
    print(singly_linked_list)  # [7, 5, 6, 10]

    singly_linked_list.remove(0)
    print(singly_linked_list)  # [5, 6, 10]
    singly_linked_list.remove(1)
    print(singly_linked_list)  # [5, 10]
    singly_linked_list.remove(1)
    print(singly_linked_list)  # [5]

    singly_linked_list.insert(6, 1)
    singly_linked_list.insert(7, 2)
    print(singly_linked_list)  # [5, 6, 7]

    print(singly_linked_list.index(6))  # 1
    print(singly_linked_list.index(7))  # 2
    print(singly_linked_list.index(10))  # -1
