from typing import Final


class Stack[T]:
    def __init__(self):
        self.elements = []

    def put(self, element: T) -> None:
        self.elements.append(element)

    def peek(self) -> T:
        if self.__len__() < 1:
            raise IndexError("The stack is empty.")
        return self.elements[-1]

    def pop(self) -> T:
        if self.__len__() < 1:
            raise IndexError("The stack is empty.")
        return self.elements.pop()

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return str(self.elements)


OPERATION_ORDER = {
    "(": 0,
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
}


def infix_to_postfix(infix_equation: str) -> str:
    infix_equation = f"({infix_equation})"

    values = Stack[str]()
    operations = Stack[str]()

    is_previous_symbol_numeric = False

    for current_char in infix_equation:
        if current_char.isnumeric():
            if is_previous_symbol_numeric:
                values.put(values.pop() + current_char)
            else:
                values.put(current_char)
            is_previous_symbol_numeric = True
            continue

        is_previous_symbol_numeric = False

        if current_char == " ":
            continue

        if current_char == "(":
            operations.put(current_char)
            continue

        if current_char == ")":
            while operations.peek() != "(":
                values.put("{1} {0} {2}".format(values.pop(), values.pop(), operations.pop()))
            operations.pop()  # Remove "(".
            continue

        while OPERATION_ORDER[current_char] < OPERATION_ORDER[operations.peek()]:
            values.put("{1} {0} {2}".format(values.pop(), values.pop(), operations.pop()))
        operations.put(current_char)

    return values.peek()


EMPTY_OPERATION: Final[str] = ""


def postfix_to_infix(postfix_equation: str) -> str:
    values = Stack[str]()
    operations = Stack[str]()

    is_previous_symbol_numeric = False

    for current_char in postfix_equation:
        if current_char.isnumeric():
            if is_previous_symbol_numeric:
                values.put(values.pop() + current_char)
            else:
                values.put(current_char)
                operations.put(EMPTY_OPERATION)
            is_previous_symbol_numeric = True
            continue

        is_previous_symbol_numeric = False

        if current_char == " ":
            continue

        right_value = values.pop()
        right_operation = operations.pop()

        if right_operation != EMPTY_OPERATION and OPERATION_ORDER[current_char] > OPERATION_ORDER[right_operation]:
            right_value = f"({right_value})"

        left_value = values.pop()
        left_operation = operations.pop()

        if left_operation != EMPTY_OPERATION and OPERATION_ORDER[current_char] > OPERATION_ORDER[left_operation]:
            left_value = f"({left_value})"

        values.put(f"{left_value}{current_char}{right_value}")
        operations.put(current_char)

    return values.peek()


infix_operations = [
    "9-3*2",
    "  1+2* 3  +4",
    "  (   1+    2*3^4)*5",
    "(9-  3)*2",
    "25    * 64",
    "(4-1)*(3+5)^2"
]

print(f"{"Infiksowa (wejście)":<25}{"Postfiksowa":<25}{"Infiksowa":<25}")
for infix_operation in infix_operations:
    converted_postfix_operation = infix_to_postfix(infix_operation)
    converted_infix_operation = postfix_to_infix(converted_postfix_operation)

    print(f"{infix_operation:<25}{converted_postfix_operation:<25}{converted_infix_operation:<25}")
