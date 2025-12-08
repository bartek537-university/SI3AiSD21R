def caesar_encode(message: str, k: int, alphabet: str) -> str:
    n = len(alphabet)
    result = ""

    for letter in message:
        letter_index = alphabet.index(letter)
        result += alphabet[(letter_index + k) % n]

    return result


def caesar_decode(encoded_message: str, k: int, alphabet: str) -> str:
    n = len(alphabet)
    result = ""

    for letter in encoded_message:
        letter_index = alphabet.index(letter)
        result += alphabet[(letter_index - k) % n]

    return result


clear_text_message = "wyrewolwerowany rewolwerowiec wyrewolwerował wyrewolwerowanego rewolwerowca"
offset = 8
alphabet = "abcdefghijklmnopqrstuvwxyząćęłńóżź "

print(f"Tekst do zakodowania: `{clear_text_message}`")

encoded_message = caesar_encode(clear_text_message, offset, alphabet)
print(f"Zakodowany tekst: `{encoded_message}`")

decoded_message = caesar_decode(encoded_message, offset, alphabet)
print(f"Zdekodowany tekst: `{decoded_message}`")

print(clear_text_message == decoded_message)
