def bubble_sort(values):
    """
    Return a sorted copy of values using bubble sort.
    """
    arr = values[:]
    n = len(arr)

    for end in range(n - 1, 0, -1):
        swapped = False

        for index in range(end):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swapped = True

        if not swapped:
            break

    return arr


if __name__ == "__main__":
    sample = [29, 10, 14, 37, 13]
    print("Original:", sample)
    print("Sorted:  ", bubble_sort(sample))
