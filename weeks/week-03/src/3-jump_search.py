import math

def jump_search(sorted_arr, target):
    """
    Return index of target in sorted_arr using jump search, else -1.
    """
    n = len(sorted_arr)
    if n == 0:
        return -1

    block_size = int(math.sqrt(n))
    start = 0
    end = block_size

    while start < n and sorted_arr[min(end, n) - 1] < target:
        start = end
        end += block_size

    if start >= n:
        return -1

    for index in range(start, min(end, n)):
        if sorted_arr[index] == target:
            return index

    return -1

