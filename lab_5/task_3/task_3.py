def boyer_moore_find(text: str, pattern: str) -> list[int]:
    text_length = len(text)
    pattern_length = len(pattern)

    last_occurrence_table = {}

    for in_pattern_index, letter in enumerate(pattern):
        last_occurrence_table[letter] = in_pattern_index

    matches = []
    pattern_start_index = 0

    while pattern_start_index + pattern_length <= text_length:
        in_pattern_index = pattern_length - 1

        while in_pattern_index >= 0 and text[pattern_start_index + in_pattern_index] == pattern[in_pattern_index]:
            in_pattern_index -= 1

        if in_pattern_index < 0:
            matches.append(pattern_start_index)
            pattern_start_index += 1
        else:
            current_letter = text[pattern_start_index + in_pattern_index]

            if current_letter in last_occurrence_table:
                last_occurrence_index = last_occurrence_table[current_letter]
                pattern_start_index += max(1, in_pattern_index - last_occurrence_index)
            else:
                pattern_start_index += in_pattern_index + 1

    return matches


print(boyer_moore_find("ABCABCDABC", "AB"))  # [0,3,7]
print(boyer_moore_find("ABCABCDABC", "CD"))  # [5]
print(boyer_moore_find("ABCABCDABC", "CE"))  # []
print(boyer_moore_find("ABDCCABCABCCC", "CABC"))  # [4, 7]
