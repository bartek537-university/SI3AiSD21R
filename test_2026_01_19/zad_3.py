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


if __name__ == "__main__":
    clear_text = "bartosz_2024"

    print(f"Tekst do zakodowania: \"{clear_text}\"")  # Tekst do zakodowania: `bartosz_2024`

    encoded_message, coding_table = shannon_fano_encode(clear_text)
    print(f"Zakodowany tekst: \"{encoded_message}\"")
    print(f"Tablica kodowa: \"{coding_table}\"")

    # Zakodowany tekst: "001010001010111000100110111000001101000111"
    # Tablica kodowa: "{'2': '000', 'b': '001', 't': '011', 'z': '101', '4': '111', 'a': '0100', 'r': '0101', 'o': '1000', 's': '1001', '_': '1100', '0': '1101'}"
