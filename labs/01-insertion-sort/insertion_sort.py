"""Insertion sort implementation and a small usage example."""


def insertion_sort_v2(arr: list[int]) -> list[int]:
    """Sort a list in ascending order with the insertion-sort algorithm.

    The input list is sorted in place and returned for convenience.
    """
    # Start from the second element; the first element is already sorted.
    for i in range(1, len(arr)):
        current = arr[i]
        previous = i - 1

        # Shift larger elements one position to the right.
        while previous >= 0 and arr[previous] > current:
            arr[previous + 1] = arr[previous]
            previous -= 1

        # Insert the current element in its correct position.
        arr[previous + 1] = current

    return arr


if __name__ == "__main__":
    numbers = [5, 7, 1, 5, 1, 0, 8, 1]
    print(insertion_sort_v2(numbers))
