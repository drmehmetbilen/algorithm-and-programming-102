def selection_sort(values):
    """
    Return a sorted copy of values using selection sort.
    """
    arr = values[:]
    n = len(arr)

    for start in range(n):
        min_index = start

        for index in range(start + 1, n):
            if arr[index] < arr[min_index]:
                min_index = index

        arr[start], arr[min_index] = arr[min_index], arr[start]

    return arr


if __name__ == "__main__":
    sample = [29, 10, 14, 37, 13]
    print("Original:", sample)
    print("Sorted:  ", selection_sort(sample))
