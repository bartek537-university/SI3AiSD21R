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

    for symbol in infix_equation:
        if symbol.isnumeric():
            if is_previous_symbol_numeric:
                values.put(values.pop() + symbol)
            else:
                values.put(symbol)
            is_previous_symbol_numeric = True
            continue

        is_previous_symbol_numeric = False

        if symbol == " ":
            continue

        if symbol == "(":
            operations.put(symbol)
        elif symbol == ")":
            while operations.peek() != "(":
                values.put("{1} {0} {2}".format(values.pop(), values.pop(), operations.pop()))
            operations.pop()  # Remove "(".
        else:
            while OPERATION_ORDER[operations.peek()] > OPERATION_ORDER[symbol]:
                values.put("{1} {0} {2}".format(values.pop(), values.pop(), operations.pop()))
            operations.put(symbol)

    return values.peek()


def postfix_to_infix(postfix_equation: str) -> str:
    values = Stack[str]()
    operations = Stack[str]()

    is_previous_symbol_numeric = False

    for symbol in postfix_equation:
        if symbol.isnumeric():
            if is_previous_symbol_numeric:
                values.put(values.pop() + symbol)
            else:
                values.put(symbol)
                operations.put("L")
            is_previous_symbol_numeric = True
            continue

        is_previous_symbol_numeric = False

        if symbol == " ":
            continue

        right_value = values.pop()
        right_operation = operations.pop()

        if right_operation != "L" and OPERATION_ORDER[symbol] > OPERATION_ORDER[right_operation]:
            right_value = f"({right_value})"

        left_value = values.pop()
        left_operation = operations.pop()

        if left_operation != "L" and OPERATION_ORDER[symbol] > OPERATION_ORDER[left_operation]:
            left_value = f"({left_value})"

        values.put(f"{left_value}{symbol}{right_value}")
        operations.put(symbol)

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
