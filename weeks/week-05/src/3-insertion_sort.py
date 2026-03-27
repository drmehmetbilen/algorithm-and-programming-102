def insertion_sort(values):
    """
    Return a sorted copy of values using insertion sort.
    """
    arr = values[:]

    for index in range(1, len(arr)):
        key = arr[index]
        position = index - 1

        while position >= 0 and arr[position] > key:
            arr[position + 1] = arr[position]
            position -= 1

        arr[position + 1] = key

    return arr


if __name__ == "__main__":
    sample = [29, 10, 14, 37, 13]
    print("Original:", sample)
    print("Sorted:  ", insertion_sort(sample))
