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
    last_added = 0
    new_value = 0
    
    for i in range(n):
        new_value = random.randint(last_added+1, max(last_added+10,max_value))
        new_list.append(new_value)
        last_added = new_value
    
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
    # index = 0
    # for i in source_list:
    #     if i==target:
    #         return True, index
    #     index += 1
    
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
    start = 0
    end = len(source_list)-1
    while start<end:
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
    block_size = int(len(source_list) ** 0.5)
    n = len(source_list)
    start = 0
    end = 0
    while end<=n:
        end = start + block_size
        print(start, end)
        if source_list[end]>target:
            break
        start = end+1
        end += block_size

    for i in range(start,end):
        if source_list[i]==target:
            return True, i
    
    return False, -1

if __name__ == "__main__":
    pass