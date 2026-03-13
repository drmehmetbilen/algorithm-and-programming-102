import random

def generate_random_unsorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    """
    Generate random and unsorted list with count n.

    Args:    
        n : List item count
        min_value : minimum random value
        max_value : maximum random value
    Returns:
        new_list : Unsorted List.
    """
    new_list = []
    for i in range(n):
        new_list.append(random.randint(min_value,max_value))

    return new_list

def generate_random_sorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    """
    Generate random and sorted list with count n.
    
    Args:    
        n : List item count
        min_value : minimum random value
        max_value : maximum random value

    Returns:
        new_list : Sorted List.
    """
    new_list = []
    list_length = len(new_list)
    while list_length < n:
        if list_length == 0:
            new_list.append(random.randint(min_value,int((max_value/4))))
        elif list_length <= n/3:
            new_list.append(random.randint(new_list[-1],int((max_value/4))))
        elif list_length <= (2*n)/3:
            new_list.append(random.randint(new_list[-1],int((max_value/2))))
        elif list_length <= n:
            new_list.append(random.randint(new_list[-1],int(max_value)))

    return new_list
            
def search_linear(source_list:list, target:int)->tuple:
    """
    Searches for a target value by iterating through each index of the array.

    Args:
        source_list (list): The list of elements to be searched.
        target (int): The value to locate within the array.

    Returns:
        tuple: A pair containing a boolean (True if found, False otherwise) 
               and the integer index of the element (index if found, -1 otherwise).
        
    """
    if not source_list: return False, -1

    for index in range(len(source_list)):
        if source_list[index]==target:
            return True, index
    
    return False, -1

def search_binary(source_list:list, target:int)->tuple:
    """
    Searches a sorted list for the target value in logarithmic time.

    Args:
        source_list (list): The list of elements to be searched.
        target (int): The value to locate within the array.
    
    Returns:
        tuple: A pair containing a boolean (True if found, False otherwise) 
               and the integer index of the element (index if found, -1 otherwise).    
    """
    if not source_list: return False, -1

    for i in range(len(source_list) - 1):
        if source_list[i] > source_list[i + 1]:
            raise ValueError("The list must be sorted.")
    
    start = 0
    end = len(source_list)-1

    while start <= end:
        mid = (start + end) // 2
        if target>source_list[mid]:
            start = mid + 1
        elif target<source_list[mid]:
            end = mid -1
        else:
           return True, mid
   
    return False, -1

def search_jump(source_list:list, target:int)->tuple:
    """
    Finds a target value in a sorted list using the Jump Search algorithm.

    This function divides the list into blocks of size sqrt(n) and 'jumps' 
    between them to locate the specific block where the target might reside. 
    Once the block is identified, it performs a linear search within that range.

    Args:
        source_list (list): A sorted list of integers.
        target (int): The integer value to search for.

    Returns:
        tuple: A pair of (bool, int). (True, index) if the element is found, 
               (False, -1) otherwise.

    Note:
        The efficiency of this algorithm is O(sqrt(n)), making it faster than 
        linear search but slower than binary search.
    """
    if not source_list: return False, -1

    for i in range(len(source_list) - 1):
        if source_list[i] > source_list[i + 1]:
            raise ValueError("The list must be sorted.")

    n = len(source_list)
    block_size = int( n ** 0.5)
    start = 0
    end = block_size

    while start<n and source_list[min(end, n) - 1] < target:
        start = end
        end += block_size
        if start >= n:
            break

    actual_end = min(end,n)
    found, sub_index =search_linear(source_list[start:actual_end],target)
    if found:
        return True, start + sub_index

    return False, -1

if __name__ == "__main__":
    #Generates Lists and Select the Target
    my_list_empty = []
    my_list_unsorted = generate_random_unsorted_list()
    my_list_sorted = generate_random_sorted_list()
    unsorted_target = my_list_unsorted[3]
    sorted_target = my_list_sorted[3]
    false_target = 0
    print("-------------------------------------------------------")
    #Lists and Targets    
    print(f"Unsorted List: {my_list_unsorted}")
    print(f"Sorted List: {my_list_sorted}")
    print(f"Unsorted List Target: {my_list_unsorted[3]}")
    print(f"Sorted List Target: {my_list_sorted[3]}")
    print("-------------------------------------------------------")
    #Linear Search Cases
    print(f"---Linear Search Positive Case--- \n Target: {unsorted_target} , Result: {search_linear(my_list_unsorted,unsorted_target)}")    
    print(f"---Linear Search Negative Case--- \n Target: {false_target} , Result: {search_linear(my_list_unsorted,false_target)}")
    print("-------------------------------------------------------")
    #Binary Search Cases
    print(f"---Binary Search Positive Case--- \n Target: {sorted_target} , Result: {search_binary(my_list_sorted,sorted_target)}")
    print(f"---Binary Search Negative Case--- \n Target: {false_target} , Result: {search_binary(my_list_sorted,false_target)}")
    print("-------------------------------------------------------")
    #Jump Search Cases
    print(f"---Jump Search Positive Case--- \n Target: {sorted_target} , Result: {search_jump(my_list_sorted,sorted_target)}")
    print(f"---Jump Search Negative Case--- \n Target: {false_target} , Result: {search_jump(my_list_sorted,false_target)}")
    print("-------------------------------------------------------")
    #Empty List Cases
    print(f"---The List May Be Empty--- \n Linear Search: {search_linear(my_list_empty,unsorted_target)} \n Binary Search: {search_binary(my_list_empty,sorted_target)} \n Jump Search: {search_jump(my_list_empty,sorted_target)}")

    