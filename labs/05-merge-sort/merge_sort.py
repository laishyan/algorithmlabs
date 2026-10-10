"""A simple Merge Sort example."""


def merge_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left_side = merge_sort(numbers[:middle])
    right_side = merge_sort(numbers[middle:])
    return merge(left_side, right_side)


def merge(left_side: list[int], right_side: list[int]) -> list[int]:
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left_side) and right_index < len(right_side):
        if left_side[left_index] < right_side[right_index]:
            result.append(left_side[left_index])
            left_index += 1
        else:
            result.append(right_side[right_index])
            right_index += 1

    result.extend(left_side[left_index:])
    result.extend(right_side[right_index:])
    return result


if __name__ == "__main__":
    values = [8, 3, 6, 1, 9, 2]
    print(merge_sort(values))
