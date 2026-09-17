def insertion_sort_v2(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        current = arr[i]
        previous = i - 1
        while previous >= 0 and arr[previous] > current:
            arr[previous + 1] = arr[previous]
            previous -= 1
        arr[previous + 1] = current

    return arr

if __name__ == "__main__":
    numbers = [5, 7, 1, 5, 1, 0, 8, 1]
    print(insertion_sort_v2(numbers))
