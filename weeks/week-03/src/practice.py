# 0. Utils: 
        # Functions that help other functions
        # Related functions:
            # generate_random_unsorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
            # generate_random_sorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
# 1. Linear Search:
        # Related functions:
        # search_linear(source_list:list, target:int)->tuple:
# 2. Binary Search:
        # Related functions:
        # search_binary(source_list:list, target:int)->tuple:
# 3. Jump Search:
        # Related functions:
        # search_jump(source_list:list, target:int)->tuple:
import random

def generate_random_unsorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    """
    Generate random and unsorted list with count n.
    
    n : List item count
    min_value : minimum random value
    max_value : maximum random value
    """
    new_list = []
    for i in range(n):
        new_list.append(random.randint(min_value,max_value))

    return new_list

def generate_random_sorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    """
    Generate random and sorted list with count n.
    
    n : List item count
    min_value : minimum random value
    max_value : maximum random value
    """
    new_list = []
    while len(new_list) < n:
        if len(new_list) == 0:
            new_list.append(random.randint(min_value,int((max_value/4))))
        elif len(new_list) <= n/3:
            new_list.append(random.randint(new_list[-1],int((max_value/4))))
        elif len(new_list) <= (2*n)/3:
            new_list.append(random.randint(new_list[-1],int((max_value/2))))
        elif len(new_list) <= n:
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

    # TODO Check if the source_list actually sorted. If not raise an error.
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
    # TODO Use search_linear method and adjust the indexes
    actual_end = min(end,n)
    found, sub_index =search_linear(source_list[start:actual_end],target)
    if found:
        return True, start + sub_index

    return False, -1

if __name__ == "__main__":
    # TODO Create positive and negative case scenarios.
    pass