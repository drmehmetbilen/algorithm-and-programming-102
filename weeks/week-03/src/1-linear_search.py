def linear_search(arr, target):
    """
    Return the index of the first occurrence of target in arr, else -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    sample = [12, 7, 4, 19, 7, 30]
    print("Array:", sample)
    print("Find 19 ->", linear_search(sample, 19))
    print("Find 7  ->", linear_search(sample, 7))
    print("Find 99 ->", linear_search(sample, 99))
    print("Find in empty ->", linear_search([], 1))
