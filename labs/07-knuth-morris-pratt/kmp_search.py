"""A simple Knuth-Morris-Pratt string search example."""


def make_prefix_table(pattern: str) -> list[int]:
    table = [0] * len(pattern)
    length = 0
    index = 1

    while index < len(pattern):
        if pattern[index] == pattern[length]:
            length += 1
            table[index] = length
            index += 1
        elif length > 0:
            length = table[length - 1]
        else:
            index += 1

    return table


def kmp_search(text: str, pattern: str) -> int:
    if pattern == "":
        return 0

    table = make_prefix_table(pattern)
    text_index = 0
    pattern_index = 0

    while text_index < len(text):
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1
            if pattern_index == len(pattern):
                return text_index - pattern_index
        elif pattern_index > 0:
            pattern_index = table[pattern_index - 1]
        else:
            text_index += 1

    return -1


if __name__ == "__main__":
    print(kmp_search("I like learning algorithms.", "algorithms"))
