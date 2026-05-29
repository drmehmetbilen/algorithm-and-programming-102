# 0. Utils
# 1. Linear Search
# 2. Binary Search
# 3. Jump Search

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
    lst = [random.randint(min_value, max_value) for _ in range(n)]
    lst.sort()
    return lst
# TODO Refine min/max value issue
#This issue was solved by creating the list randomly and then sorting it.
    
def search_linear(source_list:list, target:int)->tuple:
    # index = 0
    # for i in source_list:
    #     if i==target:
    #         return True, index
    #     index += 1
    
    for index in range(len(source_list)):
        if source_list[index]==target:
            return True, index
    
    return False, -1

def search_binary(source_list:list, target:int) -> tuple:
    # TODO Check if the source_list actually sorted. If not raise an error.
    #It raises a ValueError if the list is not sorted.
    if source_list != sorted(source_list):
        raise ValueError("Binary search requires a sorted list!")  # <--- TODO completed

    start = 0
    end = len(source_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if target > source_list[mid]:
            start = mid + 1
        elif target < source_list[mid]:
            end = mid - 1
        else:
            return True, mid

    return False, -1
    


def search_jump(source_list: list, target: int) -> tuple:
    n = len(source_list)
    if n == 0:
        return False, -1

    block_size = int(n ** 0.5)
    start = 0
    end = block_size

    # Jump phase
    while start < n and source_list[min(end, n)-1] < target:
        
        start = end
        end += block_size

    # Linear search phase
    for i in range(start, min(end, n)):
        if source_list[i] == target:
            return True, i

    return False, -1
    
    # TODO Use search_linear method and adjust the indexes
    #The search_linear method was used and the indexes were adjusted.



    # TODO Create positive and negative case scenarios.
    #positive and negative cases are created.

if __name__ == "__main__":

    # create lists
    unsorted_list = generate_random_unsorted_list()
    sorted_list = generate_random_sorted_list()

    print("Unsorted:", unsorted_list)
    print("Sorted:", sorted_list)
    
    

    # -----------------------
    # Positive test: the target is definitely on the list.
    # -----------------------
    target_in_list = random.choice(sorted_list) #definitely on the list because of "choice" method.
    print("\nPositive test - Target in list:", target_in_list)
    print("Linear:", search_linear(sorted_list, target_in_list))
    print("Binary:", search_binary(sorted_list, target_in_list))
    print("Jump:", search_jump(sorted_list, target_in_list))

    # -----------------------
    # Negative test: target is definitely not on the list.
    # -----------------------
    target_not_in_list = -1000  # definitely not on the list.
    print("\nNegative test - Target not in list:", target_not_in_list)
    print("Linear:", search_linear(sorted_list, target_not_in_list))
    print("Binary:", search_binary(sorted_list, target_not_in_list))
    print("Jump:", search_jump(sorted_list, target_not_in_list))

    # TODO Create positive and negative case scenarios.
