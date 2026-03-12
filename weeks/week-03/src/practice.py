# 0. Utils
# 1. Linear Search
# 2. Binary Search
# 3. Jump Search

import random

def generate_random_unsorted_list(n: int = 20, min_value: int = 0, max_value: int = 1000) -> list:
    """
    Generate a random and unsorted list with count n.
    
    Args:
        n (int): List item count.
        min_value (int): Minimum random value.
        max_value (int): Maximum random value.
        
    Returns:
        list: A list containing n random integers.
    """
    new_list = []
    for i in range(n):
        new_list.append(random.randint(min_value, max_value))
    return new_list

def generate_random_sorted_list(n: int = 20, min_value: int = 0, max_value: int = 1000) -> list:
    """
    Generate a random but sequentially sorted list.
    
    Args:
        n (int): List item count.
        min_value (int): Minimum random value.
        max_value (int): Maximum possible value.
        
    Returns:
        list: A sorted list containing n random integers.
    """
    new_list = []
    last_added = min_value
    new_value = 0
    
    for i in range(n):
        # TODO Refine min/max value issue
        # Solved using manual boundary checks instead of built-in min() or max() methods.
        upper_bound = last_added + 10
        if upper_bound > max_value:
            upper_bound = max_value
            
        lower_bound = last_added + 1
        if lower_bound > upper_bound:
            lower_bound = upper_bound
            
        new_value = random.randint(lower_bound, upper_bound)
        new_list.append(new_value)
        last_added = new_value

    return new_list

def search_linear(source_list: list, target: int) -> tuple:
    """
    Perform a linear search on a given list.
    
    Args:
        source_list (list): The list to be searched.
        target (int): The value to search for.
        
    Returns:
        tuple: (True, index) if found, (False, -1) otherwise.
    """
    for index in range(len(source_list)):
        if source_list[index] == target:
            return True, index

    return False, -1

def search_binary(source_list: list, target: int) -> tuple:
    """
    Perform a binary search on a sorted list.
    
    Args:
        source_list (list): The sorted list to be searched.
        target (int): The value to search for.
        
    Returns:
        tuple: (True, index) if found, (False, -1) otherwise.
        
    Raises:
        ValueError: If the provided list is not sorted.
    """
    # TODO Check if the source_list actually sorted. If not raise an error.
    # Solved by manually comparing adjacent elements without using sort() or sorted().
    for i in range(len(source_list) - 1):
        if source_list[i] > source_list[i + 1]:
            raise ValueError("Error: The list must be sorted to perform Binary Search.")

    start = 0
    end = len(source_list) - 1
    
    while start <= end:
        mid = int((start + end) / 2)
        if target > source_list[mid]:
            start = mid + 1
        elif target < source_list[mid]:
            end = mid - 1
        else:
           return True, mid

    return False, -1

def search_jump(source_list: list, target: int) -> tuple:
    """
    Perform a jump search on a sorted list.
    
    Args:
        source_list (list): The sorted list to be searched.
        target (int): The value to search for.
        
    Returns:
        tuple: (True, index) if found, (False, -1) otherwise.
    """
    n = len(source_list)
    if n == 0:
        return False, -1
        
    block_size = int(n ** 0.5)
    start = 0
    end = block_size
    
    while end < n:
        if source_list[end - 1] >= target:
            break
        start = end
        end += block_size
        
    # Manual boundary check instead of using min(end, n)
    if end > n:
        end = n

    # TODO Use search_linear method and adjust the indexes
    # Solved by manually creating a sub-list with a loop to avoid using Python's built-in slice feature [:]
    sub_list = []
    for i in range(start, end):
        sub_list.append(source_list[i])
        
    is_found, relative_index = search_linear(sub_list, target)
    
    if is_found:
        actual_index = start + relative_index
        return True, actual_index

    return False, -1

if __name__ == "__main__":
    # TODO Create positive and negative case scenarios.
    print("--- Algorithm Test Scenarios ---\n")
    
    test_list = generate_random_sorted_list(15, 0, 100)
    
    print("Generated List:")
    # Printing elements manually to avoid complex string formatting methods
    for item in test_list:
        print(item, end=" ")
    print("\n")
    
    # Positive Scenario (Searching for an existing element)
    target_positive = test_list[7] 
    
    # Negative Scenario (Searching for a non-existing element)
    target_negative = -99 
    
    print("--- POSITIVE SCENARIO (Target:", target_positive, ") ---")
    print("Linear Search :", search_linear(test_list, target_positive))
    print("Binary Search :", search_binary(test_list, target_positive))
    print("Jump Search   :", search_jump(test_list, target_positive))
    
    print("\n--- NEGATIVE SCENARIO (Target:", target_negative, ") ---")
    print("Linear Search :", search_linear(test_list, target_negative))
    print("Binary Search :", search_binary(test_list, target_negative))
    print("Jump Search   :", search_jump(test_list, target_negative))
