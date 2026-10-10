"""A simple Selection Sort example."""


def selection_sort(numbers: list[int]) -> list[int]:
    result = numbers.copy()

    for start in range(len(result)):
        smallest_index = start

        for current in range(start + 1, len(result)):
            if result[current] < result[smallest_index]:
                smallest_index = current

        result[start], result[smallest_index] = (
            result[smallest_index],
            result[start],
        )

    return result


if __name__ == "__main__":
    values = [8, 3, 6, 1, 9, 2]
    print(selection_sort(values))
