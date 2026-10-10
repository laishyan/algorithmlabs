"""A simple Quick Sort example."""


def quick_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    smaller_numbers = []
    equal_numbers = []
    bigger_numbers = []

    for number in numbers:
        if number < pivot:
            smaller_numbers.append(number)
        elif number > pivot:
            bigger_numbers.append(number)
        else:
            equal_numbers.append(number)

    return quick_sort(smaller_numbers) + equal_numbers + quick_sort(bigger_numbers)


if __name__ == "__main__":
    values = [8, 3, 6, 1, 9, 2]
    print(quick_sort(values))
