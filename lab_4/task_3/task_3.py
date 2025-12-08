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


def shannon_fano_encode(message: str) -> tuple[str, dict[str, str]]:
    assert len(message) > 0

    occurrences: dict[str, int] = {}

    for letter in message:
        if letter not in occurrences:
            occurrences[letter] = 0
        occurrences[letter] += 1

    assert len(occurrences) > 1

    sorted_letters = [*occurrences.items()]
    sorted_letters.sort(key=lambda symbol: symbol[1], reverse=True)

    tree_queue = Queue[tuple[list[str], str]](capacity=2 * len(occurrences) - 1)
    tree_queue.enqueue((sorted_letters, ""))

    coding_table: dict[str, str] = {}

    while len(tree_queue) > 0:
        symbols, prefix = tree_queue.dequeue()

        if len(symbols) < 2:
            letter, _ = symbols[0]
            coding_table[letter] = prefix
            continue

        weight_left = 0
        weight_right = 0

        for _, letter_weight in symbols:
            weight_right += letter_weight

        splitter = 0

        for _, letter_weight in symbols:
            if abs(weight_right - weight_left - 2 * letter_weight) > abs(weight_right - weight_left):
                break

            weight_left += letter_weight
            weight_right -= letter_weight

            splitter += 1

        tree_queue.enqueue((symbols[:splitter], f"{prefix}0"))
        tree_queue.enqueue((symbols[splitter:], f"{prefix}1"))

    encoded_message = ""

    for letter in message:
        encoded_message += coding_table[letter]

    return encoded_message, coding_table


def shannon_fano_decode(encoded_message: str, code_table: dict[str, str]) -> str:
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

encoded_message, coding_table = shannon_fano_encode(clear_text_message)
print(f"Tablica kodowa: {coding_table}")
print(f"Zakodowany tekst: `{encoded_message}`")

decode_table = {code: letter for letter, code in coding_table.items()}

decoded_message = shannon_fano_decode(encoded_message, decode_table)
print(f"Zdekodowany tekst: `{decoded_message}`")

print(clear_text_message == decoded_message)
