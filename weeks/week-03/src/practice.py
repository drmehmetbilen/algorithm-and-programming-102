import random

def generate_random_unsorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    """
    Returns a random and unsorted list with count n.
    
    Args:
        n : List item count
        min_value : Minimum random value
        max_value : Maximum random value
    """
    new_list = []
    for i in range(n):
        new_list.append(random.randint(min_value,max_value))

    return new_list

def generate_random_sorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    """
    Returns a random and natively sorted list with count n.

    Args:
        n : List item count
        min_value : Minimum random value
        max_value : Maximum random value
    """
    new_list = []
    for i in range(n):
        new_num = random.randint(min_value,max_value)
        inserted = False
        for i in range(len(new_list)):
            if new_num < new_list[i]:
                new_list.insert(i, new_num)
                inserted = True
                break
        if not inserted:
            new_list.append(new_num)

    return new_list
    
def search_linear(source_list:list, target:int)->tuple:
    """
    Use a linear search algorithm to find targets in a list with time complexity of O(n).

    Args:
        source_list : List to be searched.
        target : Target to be searched in source_list.

    Returns:
        True, target's index; if found
        False, -1; if target is not found
    """
    for index in range(len(source_list)):
        if source_list[index]==target:
            return True, index
    
    return False, -1

def search_binary(source_list:list, target:int)->tuple:
    """
    Use a binary search algorithm to find targets in a sorted list with a time complexity of O(log n).

    Args:
        source_list : Sorted list to be searched.
        target : Target to be searched in source_list.

    Returns:
        True, target's index; if found.
        False, -1; if target is not found.

    Raises:
        ValueError; if source_list is not sorted.
    """
    if check_sort_status(source_list) != True:
        return ValueError("Provided list is not sorted. Provide a sorted list for Binary Searches.")
    
    start = 0
    end = len(source_list)-1
    while start <= end:
        mid = int((start + end) / 2)
        if target>source_list[mid]:
            start = mid + 1
        elif target<source_list[mid]:
            end = mid -1
        else:
           return True, mid
   
    return False, -1

def search_jump(source_list:list, target:int)->tuple:
    """
    Use a jumping search algorithm to find targets in a sorted list with a time complexity of O(sqrt(n))

    Args:
        source_list: Sorted list to be searched.
        target: Target to be searched in source_list.

    Returns:
        True, target's index; if found
        False, -1; if target is not found.
    Raises:
        ValueError; if source_list is not sorted.
    """
    if check_sort_status(source_list) != True:
        return ValueError("Provided list is not sorted. Provide a sorted list for Jump Searches.")

    block_size = int(len(source_list) ** 0.5)
    n = len(source_list)
    start = 0
    end = block_size
    while end < n and source_list[min(end, n) - 1] < target:
        start = end
        end += block_size
    
    block_to_search = source_list[start:end]
    found, local_index = search_linear(block_to_search, target)
    if found:
        return True, start + local_index
    
    return False, -1

def check_sort_status(source_list:list)->bool:
    for i in range(len(source_list) -1):
        if source_list[i] > source_list[i + 1]:
            return False
    return True

if __name__ == "__main__":
    print("\nEnter values for generating lists or leave empty for default values...\nUsage : quantity of numbers,minimum value,maximum value.\n(Default=20,0,1000)")

    selection = input()

    if selection:
        n, min_value, max_value = map(int, selection.split(","))
        false_target = int(min_value - 10)
        selection = (n, min_value, max_value)
        generated_sorted_list = generate_random_sorted_list(*selection)
        generated_unsorted_list = generate_random_unsorted_list(*selection)
    else:
        n, min_value, max_value = 20, 0, 1000
        false_target = int(min_value - 10)
        selection = (n, min_value, max_value)
        generated_sorted_list = generate_random_sorted_list()
        generated_unsorted_list = generate_random_unsorted_list()

    print(f"\nGenerated Unsorted List = {generated_unsorted_list}\n\nGenerated Sorted List   = {generated_sorted_list}\n")
    print("\nSelect a value to search from the unsorted list:")
    target_unsorted_list = int(input())
    print("\nSelect a value to search from the sorted list:")
    target_sorted_list = int(input())

    print("\nTesting unsorted list with searching algorithms...")

    args_unsorted_list = (generated_unsorted_list,target_unsorted_list)
    args_sorted_list   = (generated_sorted_list,target_sorted_list)

    print(f"\nLinear Search = {search_linear(*args_unsorted_list)}")
    print(f"\nBinary Search = {search_binary(*args_unsorted_list)}")
    print(f"\nJump Search   = {search_jump(*args_unsorted_list)}")

    print("\nTesting sorted list with searching algorithms...")

    print(f"\nLinear Search = {search_linear(*args_sorted_list)}")
    print(f"\nBinary Search = {search_binary(*args_sorted_list)}")
    print(f"\nJump Search   = {search_jump(*args_sorted_list)}")

    print("\nTesting non-present values on unsorted lists with searching algorithms...")

    args_false_unsorted_list = (generated_unsorted_list,false_target)
    args_false_sorted_list = (generated_sorted_list,false_target)

    print(f"\nLinear Search = {search_linear(*args_false_unsorted_list)}")
    print(f"\nBinary Search = {search_binary(*args_false_unsorted_list)}")
    print(f"\nJump Search   = {search_jump(*args_false_unsorted_list)}")

    print("\nTesting non-present values on unsorted lists with searching algorithms...")

    print(f"\nLinear Search = {search_linear(*args_false_sorted_list)}")
    print(f"\nBinary Search = {search_binary(*args_false_sorted_list)}")
    print(f"\nJump Search   = {search_jump(*args_false_sorted_list)}")