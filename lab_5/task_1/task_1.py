def naive_find(text: str, pattern: str) -> list[int]:
    text_length = len(text)
    pattern_length = len(pattern)

    matches = []

    for i in range(text_length - pattern_length + 1):
        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                break
        else:
            matches.append(i)

    return matches


print(naive_find("ABCABCDABC", "AB"))  # [0,3,7]
print(naive_find("ABCABCDABC", "CD"))  # [5]
print(naive_find("ABCABCDABC", "CE"))  # []
