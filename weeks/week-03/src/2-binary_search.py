
def binary_search(sorted_arr, target):
    """
    Return index of target in sorted_arr using iterative binary search, else -1.
    """


    left = 0
    right = len(sorted_arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_arr[mid]

        if mid_value == target:
            return mid
        if target < mid_value:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    sorted_sample = [-5, 1, 3, 8, 13, 21, 34]
    print("Sorted array:", sorted_sample)
    print("Find 13 ->", binary_search(sorted_sample, 13))
    print("Find 2  ->", binary_search(sorted_sample, 2))

    unsorted_sample = [4, 1, 7, 2]
    print("Unsorted array:", unsorted_sample)
    try:
        print(binary_search(unsorted_sample, 7))
    except ValueError as error:
        print("Error:", error)
