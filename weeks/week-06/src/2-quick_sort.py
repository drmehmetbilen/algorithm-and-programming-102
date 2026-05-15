def quick_sort(values):
    """
    Return a sorted copy of values using quick sort.
    """
    if len(values) <= 1:
        return values[:]

    pivot = values[-1]
    less = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    greater = [value for value in values if value > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


if __name__ == "__main__":
    sample = [29, 10, 14, 37, 13, 8]
    print("Original:", sample)
    print("Sorted:  ", quick_sort(sample))
