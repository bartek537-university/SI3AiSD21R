input_text = "3.14;5;;2"

max_number: None | float = None

partial_number = ""
input_text += ";"

for i in range(len(input_text)):
    current_char = input_text[i]

    if current_char != ";":
        partial_number += current_char
        continue

    if partial_number == "":
        continue

    current_number = float(partial_number)

    if max_number is None or current_number > max_number:
        max_number = current_number

    partial_number = ""

print(max_number)
