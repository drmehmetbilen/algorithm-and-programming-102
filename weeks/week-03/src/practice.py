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
    
    new_list = []
    last_added = 0
    new_value = 0
    
    for i in range(n):
        # TODO Refine min/max value issue
        new_value = random.randint(last_added+1, max(last_added+10,max_value))
        new_list.append(new_value)
        last_added = new_value
    
    return new_list
    
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

def search_binary(source_list:list, target:int)->tuple:
    # TODO Check if the source_list actually sorted. If not raise an error.
    
    
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
    
    # TODO Use search_linear method and adjust the indexes
    for i in range(start,end):
        if source_list[i]==target:
            return True, i
    
    return False, -1

if __name__ == "__main__":
    # TODO Create positive and negative case scenarios.
    pass