def find_max(input_text: str) -> float | None:
    input_text += ";"

    max_number: None | float = None

    current_number = 0.0
    decimal_numerator = 0
    is_negative = False

    for current_char in input_text:
        if current_char.isnumeric():
            if decimal_numerator > 0:
                current_number += int(current_char) * 10 ** (-decimal_numerator)
                decimal_numerator += 1
            else:
                current_number = current_number * 10 + int(current_char)
            continue

        if current_char == ".":
            decimal_numerator = 1
            continue

        if current_char == "-":
            is_negative = True
            continue

        if is_negative:
            current_number *= -1

        if max_number is None or current_number > max_number:
            max_number = current_number

        current_number = 0.0
        decimal_numerator = 0
        is_negative = False

    return max_number


print(find_max("31.415;42;-15"))
