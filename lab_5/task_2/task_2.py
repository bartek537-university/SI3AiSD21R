from typing import Callable


def karp_rabin_find(text: str, pattern: str, hash_function: Callable[[str], int]) -> list[int]:
    text_length = len(text)
    pattern_length = len(pattern)

    matches = []
    pattern_hash = hash_function(pattern)

    for i in range(text_length - pattern_length + 1):
        slice_text = text[i:i + pattern_length]
        slice_hash = hash_function(slice_text)

        if pattern_hash == slice_hash:
            matches.append(i)

    return matches


def string_hash_function(text: str) -> int:
    hash_value = 0

    for letter in text:
        hash_value = (hash_value * 31 + ord(letter)) % 17

    return hash_value

print(karp_rabin_find("ABCABCDABC", "AB", string_hash_function))  # [0,3,7]
print(karp_rabin_find("ABABBBACABABB", "BAB", string_hash_function))  # [1,9]
print(karp_rabin_find("ABCABCDABC", "CD", string_hash_function))  # [5]
print(karp_rabin_find("ABCABCDABC", "CE", string_hash_function))  # []
