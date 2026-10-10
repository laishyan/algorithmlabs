"""A simple Boyer-Moore string search example."""


def make_last_position_table(pattern: str) -> dict[str, int]:
    table = {}
    for index in range(len(pattern)):
        table[pattern[index]] = index
    return table


def boyer_moore_search(text: str, pattern: str) -> int:
    if pattern == "":
        return 0

    last_position = make_last_position_table(pattern)
    start = 0

    while start <= len(text) - len(pattern):
        pattern_index = len(pattern) - 1

        while pattern_index >= 0 and pattern[pattern_index] == text[start + pattern_index]:
            pattern_index -= 1

        if pattern_index < 0:
            return start

        letter = text[start + pattern_index]
        start += max(1, pattern_index - last_position.get(letter, -1))

    return -1


if __name__ == "__main__":
    print(boyer_moore_search("I like learning algorithms.", "algorithms"))
