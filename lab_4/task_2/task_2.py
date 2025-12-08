class Queue[T]:
    def __init__(self, capacity: int):
        assert capacity > 0
        self._start_index = 0
        self._size = 0
        self._capacity = capacity
        self._buffer = [None] * capacity

    def enqueue(self, value: T) -> None:
        if self._size >= self._capacity:
            raise OverflowError("The queue is full.")

        insert_index = (self._start_index + self._size) % self._capacity
        self._buffer[insert_index] = value
        self._size += 1

    def dequeue(self) -> T:
        if self._size < 1:
            raise OverflowError("The queue is empty.")

        dequeued_value = self._buffer[self._start_index]
        self._start_index = (self._start_index + 1) % self._capacity
        self._size -= 1

        return dequeued_value

    def __len__(self):
        return self._size


class PriorityQueue[T]:
    def __init__(self, capacity: int):
        assert capacity > 0
        self._size = 0
        self._capacity = capacity
        self._elements: list[tuple[int, float] | None] = [None] * capacity

    def enqueue(self, value: T, weight: float) -> None:
        if self._size >= self._capacity:
            raise OverflowError("The queue is full.")

        j = self._size
        while j > 0 and self._elements[j - 1][1] > weight:
            self._elements[j] = self._elements[j - 1]
            j -= 1
        self._elements[j] = (value, weight)

        self._size += 1

    def dequeue(self) -> tuple[T, float]:
        if self._size < 1:
            raise OverflowError("The queue is empty.")

        dequeued_element = self._elements[self._size - 1]
        self._size -= 1

        return dequeued_element

    def __len__(self):
        return self._size


class Node[T]:
    def __init__(self, value: T | None = None):
        self.value = value
        self.left: Node[T] | None = None
        self.right: Node[T] | None = None


def huffman_encode(message: str) -> tuple[str, dict[str, str]]:
    assert len(message) > 0

    occurrences: dict[str, int] = {}

    for letter in message:
        if letter not in occurrences:
            occurrences[letter] = 0
        occurrences[letter] += 1

    assert len(occurrences) > 1

    symbols = PriorityQueue[Node](capacity=len(occurrences))

    for letter, count in occurrences.items():
        symbols.enqueue(Node(letter), -count)

    while len(symbols) > 1:
        right_node, right_weight = symbols.dequeue()
        left_node, left_weight = symbols.dequeue()

        compound_node = Node()
        compound_node.left = left_node
        compound_node.right = right_node

        symbols.enqueue(compound_node, left_weight + right_weight)

    root = symbols.dequeue()[0]

    bfs_queue = Queue[tuple[Node, str]](capacity=len(occurrences) * 2)
    bfs_queue.enqueue((root, ""))

    coding_table: dict[str, str] = {}

    while len(bfs_queue) > 0:
        element, code = bfs_queue.dequeue()

        if element.left:
            bfs_queue.enqueue((element.left, f"{code}0"))
        if element.right:
            bfs_queue.enqueue((element.right, f"{code}1"))

        if not element.left and not element.right:
            coding_table[element.value] = code

    encoded_message = ""

    for letter in message:
        encoded_message += coding_table[letter]

    return encoded_message, coding_table


def huffman_decode(encoded_message: str, code_table: dict[str, str]) -> str:
    decoded_message = ""
    current_sequence = ""

    for letter in encoded_message:
        current_sequence += letter

        if current_sequence not in code_table:
            continue

        decoded_message += code_table[current_sequence]
        current_sequence = ""

    return decoded_message


clear_text_message = "wyrewolwerowany rewolwerowiec wyrewolwerował wyrewolwerowanego rewolwerowca"
print(f"Tekst do zakodowania: `{clear_text_message}`")

encoded_message, coding_table = huffman_encode(clear_text_message)
print(f"Tablica kodowa: {coding_table}")
print(f"Zakodowany tekst: `{encoded_message}`")

decode_table = {code: letter for letter, code in coding_table.items()}

decoded_message = huffman_decode(encoded_message, decode_table)
print(f"Zdekodowany tekst: `{decoded_message}`")

print(clear_text_message == decoded_message)
