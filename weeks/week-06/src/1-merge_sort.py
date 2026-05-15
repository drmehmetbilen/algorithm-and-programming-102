def merge_sort(values):
    """
    Return a sorted copy of values using merge sort.
    """
    if len(values) <= 1:
        return values[:]

    middle = len(values) // 2
    left_sorted = merge_sort(values[:middle])
    right_sorted = merge_sort(values[middle:])
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    """
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


if __name__ == "__main__":
    sample = [29, 10, 14, 37, 13, 8]
    print("Original:", sample)
    print("Sorted:  ", merge_sort(sample))
