import random

# 0. Utils
def generate_random_unsorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    new_list = []
    for i in range(n):
        new_list.append(random.randint(min_value,max_value))
    return new_list

def generate_random_sorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    new_list = []
    # Fixed: Started from min_value to respect the lower bound constraint
    last_added = min_value 
    
    for i in range(n):
        # Refined min/max logic: Ensuring the value stays within the specified max_value
        # and remains strictly increasing.
        step = (max_value - last_added) // (n - i)
        new_value = random.randint(last_added + 1, last_added + max(1, step))
        new_list.append(new_value)
        last_added = new_value
    
    return new_list
    
# 1. Linear Search
def search_linear(source_list:list, target:int)->tuple:
    for index in range(len(source_list)):
        if source_list[index] == target:
            return True, index
    return False, -1

# 2. Binary Search
def search_binary(source_list:list, target:int)->tuple:
    # Check if the list is sorted; raise ValueError if not to ensure binary search validity
    if source_list != sorted(source_list):
        raise ValueError("Source list must be sorted for binary search.")
    
    start = 0
    end = len(source_list) - 1
    while start <= end: # Fixed: changed < to <= to include the last element
        mid = (start + end) // 2
        if target > source_list[mid]:
            start = mid + 1
        elif target < source_list[mid]:
            end = mid - 1
        else:
            return True, mid
    return False, -1

# 3. Jump Search
def search_jump(source_list:list, target:int)->tuple:
    n = len(source_list)
    block_size = int(n ** 0.5)
    start = 0
    end = block_size
    
    # Identify the block where the target might be located
    while end < n and source_list[min(end, n) - 1] < target:
        start = end
        end += block_size
    
    # Use search_linear logic on the identified block and adjust indices
    sub_list = source_list[start:min(end, n)]
    found, local_index = search_linear(sub_list, target)
    
    if found:
        return True, start + local_index
    return False, -1

if __name__ == "__main__":
    # Test Scenarios
    sorted_list = generate_random_sorted_list(n=15, min_value=10, max_value=100)
    target_exists = sorted_list[5]
    target_missing = 999
    
    print(f"List: {sorted_list}")
    
    # Positive Case: Searching for an existing element
    print(f"\nPositive Case (Target {target_exists}):")
    print(f"Linear: {search_linear(sorted_list, target_exists)}")
    print(f"Binary: {search_binary(sorted_list, target_exists)}")
    print(f"Jump:   {search_jump(sorted_list, target_exists)}")
    
    # Negative Case: Searching for a non-existing element
    print(f"\nNegative Case (Target {target_missing}):")
    print(f"Linear: {search_linear(sorted_list, target_missing)}")
    print(f"Binary: {search_binary(sorted_list, target_missing)}")
    print(f"Jump:   {search_jump(sorted_list, target_missing)}")