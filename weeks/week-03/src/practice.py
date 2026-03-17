"""
PROJECT STANDARDS:
- Documentation  : Self-documenting code with Type Hints and Docstrings.
- Reliability    : Edge case handling for empty lists, unsorted input, and out-of-range targets.
- Complexity     : Each algorithm includes explicit Big-O analysis in its docstring.
"""

import random

# ─────────────────────────────────────────────
# 0. UTILITIES
# ─────────────────────────────────────────────

def generate_random_unsorted_list(n: int = 20, min_value: int = 0, max_value: int = 1000) -> list:
    """
    Generates a random unsorted list of integers.

    Parameters:
        n         (int): Number of elements in the list.
        min_value (int): Minimum possible random value (inclusive).
        max_value (int): Maximum possible random value (inclusive).

    Returns:
        list: A randomly generated unsorted list of n integers.
    """
    new_list = []
    for _ in range(n):
        new_list.append(random.randint(min_value, max_value))
    return new_list

def generate_random_sorted_list(n: int = 20, min_value: int = 0, max_value: int = 1000) -> list:
    """
    Generates a random sorted (ascending) list of integers.

    Strategy:
        At each step, a random number greater than the previous value is selected. 
        Thus, the list naturally increases without the need for additional sorting

    Parameters:
        n         (int): Number of elements in the list.
        min_value (int): Starting lower bound for the first element.
        max_value (int): Upper bound guidance for step size calculation.

    Returns:
        list: A randomly generated sorted list of n integers.
    """
    new_list = []
    last = min_value
    for _ in range(n):
        last = random.randint(last + 1, last + max(10, max_value // n))
        new_list.append(last)
    return new_list

def is_sorted(source_list: list) -> bool:
    """
    Checks whether a list is in strictly ascending order.

    Strategy:
        Compares each element with the next one.
        Returns False immediately on the first violation — early exit pattern.

    Complexity: O(n)

    Parameters:
        source_list (list): The list to validate.

    Returns:
        bool: True if sorted ascending, False otherwise.
    """
    for i in range(len(source_list) - 1):
        if source_list[i] > source_list[i + 1]:
            return False
    return True

# ─────────────────────────────────────────────
# 1. LINEAR SEARCH  —  O(n)
# ─────────────────────────────────────────────

def search_linear(source_list: list, target: int) -> tuple:
    """
    Scans the list from left to right to locate the target value.

    Strategy:
        Each element is checked sequentially. No sorting precondition.
        Best suited for small lists or one-time lookups on unsorted data.

    Complexity:
        Best case   : O(1)  — target is the first element.
        Worst case  : O(n)  — target is the last element or absent.
        Average case: O(n)

    Parameters:
        source_list (list): The list to search (sorted or unsorted).
        target      (int) : The value to find.

    Returns:
        tuple: (True, index) if found, (False, -1) if not found.
    """
    if not source_list:
        return False, -1

    for index in range(len(source_list)):
        if source_list[index] == target:
            return True, index

    return False, -1

# ─────────────────────────────────────────────
# 2. BINARY SEARCH  —  O(log n)
# ─────────────────────────────────────────────

def search_binary(source_list: list, target: int) -> tuple:
    """
    Searches a sorted list by halving the active search space at each step.

    Precondition:
        The list must be sorted in ascending order.

    Strategy — Two Pointer:
        'start' and 'end' mark the boundaries of the active search window.
        At each iteration the midpoint (mid) is recalculated:
          - target < mid_value  →  end   = mid - 1  (discard right half)
          - target > mid_value  →  start = mid + 1  (discard left half)
          - target == mid_value →  return index immediately.
        Loop exits when start > end, meaning the target is absent.

    Complexity:
        Best case   : O(1)     — target is the first mid.
        Worst case  : O(log n) — search space halves at every step.
        Average case: O(log n)

    Parameters:
        source_list (list): A sorted ascending list.
        target      (int) : The value to find.

    Returns:
        tuple: (True, index) if found, (False, -1) if not found.

    Raises:
        ValueError: If the list is not sorted.
    """
    if not source_list:
        return False, -1

    if not is_sorted(source_list):
        raise ValueError("Binary Search requires a sorted list.")

    start = 0
    end = len(source_list) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_value = source_list[mid]

        if mid_value == target:
            return True, mid
        elif target < mid_value:
            end = mid - 1
        else:
            start = mid + 1

    return False, -1

# ─────────────────────────────────────────────
# 3. JUMP SEARCH  —  O(sqrt n)
# ─────────────────────────────────────────────

def search_jump(source_list: list, target: int) -> tuple:
    """
    Searches a sorted list by skipping fixed-size blocks, then performing
    a linear scan inside the block where the target may reside.

    Precondition:
        The list must be sorted in ascending order.

    Strategy:
        1. Block size is set to floor(sqrt(n)) — the mathematically optimal
           value that minimises the combined jump and scan cost.
        2. The last element of each block is compared to the target:
             last < target  →  skip to the next block.
             last >= target →  target may be here, stop jumping.
        3. Employs a modular linear scan within the block to determine the 
           exact index, adhering to the DRY (Don't Repeat Yourself) principle.

    Complexity:
        Best case   : O(1)
        Worst case  : O(sqrt n)
        Average case: O(sqrt n)

    Parameters:
        source_list (list): A sorted ascending list.
        target      (int) : The value to find.

    Returns:
        tuple: (True, index) if found, (False, -1) if not found.

    Raises:
        ValueError: If the list is not sorted.
    """
    if not source_list:
        return False, -1

    if not is_sorted(source_list):
        raise ValueError("Jump Search requires a sorted list.")

    n = len(source_list)
    block_size = int(n ** 0.5)
    start = 0

    # Phase 1: Jump through blocks to narrow down the target's location.
    while start < n and source_list[min(start + block_size, n) - 1] < target:
        start += block_size

    if start >= n:
        return False, -1

    # Phase 2: Linear scan within the candidate block.
    block = source_list[start: min(start + block_size, n)]
    found, local_index = search_linear(block, target)

    if found:
        return True, start + local_index

    return False, -1

# ─────────────────────────────────────────────
# COMPARISON UTILITY
# ─────────────────────────────────────────────

def compare_algorithms(source_list: list, target: int) -> None:
    """
    Runs all three search algorithms on the same input and prints
    results alongside their Big-O complexity labels.

    Parameters:
        source_list (list): The list to search.
        target      (int) : The value to find.
    """
    print(f"\n{'='*50}")
    print(f"  List size    : {len(source_list)}")
    print(f"  Target value : {target}")
    print(f"  Linear Search O(n) →  {search_linear(source_list, target)}")
    print(f"\n{'='*50}")

    try:
        print(f"  Binary Search O(log n) →  {search_binary(source_list, target)}")
    except ValueError as error:
        print(f"  Binary Search →  Error: {error}")

    try:
        print(f"  Jump Search O(sqrt n) →  {search_jump(source_list, target)}")
    except ValueError as error:
        print(f"  Jump Search →  Error: {error}")
    print(f"\n{'='*50}")
    
# ─────────────────────────────────────────────
# TEST
# ─────────────────────────────────────────────

if __name__ == "__main__":

    # ── Positive case: target exists in a sorted list ──
    sorted_list = generate_random_sorted_list(n=20)
    print("Sorted list:", sorted_list)
    existing_target = sorted_list[random.randint(0, len(sorted_list) - 1)]
    compare_algorithms(sorted_list, existing_target)

    # ── Negative case: target is absent from the list ──
    compare_algorithms(sorted_list, 999999)

    # ── Unsorted input: linear succeeds, binary and jump raise ValueError ──
    unsorted_list = generate_random_unsorted_list(n=10)
    print("Unsorted list:", unsorted_list)
    compare_algorithms(unsorted_list, unsorted_list[0])

    # ── Edge case: empty list ──
    print("Empty list tests:")
    print("  Linear:", search_linear([], 5))
    print("  Binary:", search_binary([], 5))
    print("  Jump  :", search_jump([], 5))