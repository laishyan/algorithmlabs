"""Beginner implementations of Bubble Sort and Heap Sort."""


def bubble_sort(numbers: list[int]) -> list[int]:
    """Sort a list by swapping neighboring numbers."""
    result = numbers.copy()

    for end in range(len(result) - 1, 0, -1):
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]

    return result


def heapify(numbers: list[int], heap_size: int, root_index: int) -> None:
    """Move the largest value in a small heap to its root."""
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2

    if left_child < heap_size and numbers[left_child] > numbers[largest]:
        largest = left_child

    if right_child < heap_size and numbers[right_child] > numbers[largest]:
        largest = right_child

    if largest != root_index:
        numbers[root_index], numbers[largest] = numbers[largest], numbers[root_index]
        heapify(numbers, heap_size, largest)


def heap_sort(numbers: list[int]) -> list[int]:
    """Sort a list by building a max heap and removing its largest values."""
    result = numbers.copy()
    size = len(result)

    # Build a max heap.
    for index in range(size // 2 - 1, -1, -1):
        heapify(result, size, index)

    # Move the largest value to the end one at a time.
    for end in range(size - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        heapify(result, end, 0)

    return result


if __name__ == "__main__":
    values = [7, 2, 9, 1, 5, 3]

    print("Original list:", values)
    print("Bubble Sort:", bubble_sort(values))
    print("Heap Sort:", heap_sort(values))
