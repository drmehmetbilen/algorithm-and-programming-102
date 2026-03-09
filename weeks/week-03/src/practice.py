#0.Utils
#1.Lineer Search
#2.Binaty Search
#3.Jump Search

import random

def generate_random_unsorted_list(n:int = 20, min_value:int = 0,max_value:int = 1000) -> list:
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

def generate_random_sorted_list(n:int = 20, min_value:int = 0, max_value:int = 1000)->list:
    """
    Generate random and sorted list with count n.

    n : List item count
    min_value : minimum random value
    max_value : maximum random value
    """
    new_list = []
    last_added = min_value -1


    for i in range(n):
        #TODO Refine min/max value issue
        start = max(last_added+1,min_value)
        remaining = n - i - 1
        end = max_value - remaining
        if start > end:
            break

        new_value = random.randint(start,end)
        new_list.append(new_value)
        last_added = new_value


    return new_list

def search_linear(source_list:list, target:int,) -> tuple:
    """
    Searches for items by checking each item step by step within the list.
    
    source_list : The list to be searched.
    target : Searched item.
    """
#    index = 0
#    for i in source_list:
#         if i == target:
#             return True, index
#         index+= 1

    for index in range(len(source_list)):
        if source_list[index] == target:
            return True,index
        
    return False, -1

def search_binary(source_list:list, target:int) -> tuple:
    """
    Checks if the list is sorted and searches by dividing the list into two parts each time,
    based on the location of the item being searched for.

    source_list : The list to be searched.
    target : Searched item.

    """
    #TODO Check if the source _list actually sorted. If not raise an error.
    if not source_list: return False,-1

    for i in range(len(source_list)-1):
                if source_list[i] > source_list[i+1]:
                    raise ValueError("The list must be sorted.")

    start = 0
    end = len(source_list)-1
    
    while start<end:
        mid = int((start+end)/2)
        if target > source_list[mid]:
            start = mid + 1
        elif target < source_list[mid]:
            end = mid - 1

        else:
            return True, mid
        
    return False, -1

def search_jump(source_list:list,target:int)-> tuple:
    """
    Checks if the list is sorted and finds the desired item by breaking the list into blocks.

    source_list : The list to be searched.
    target : Searched item.

    """
    
    if not source_list: return False,-1

    for i in range(len(source_list)-1):
        if source_list[i] > source_list[i+1]:
            raise ValueError("The list must be sorted.")
        

    block_size = int(len(source_list) ** 0.5)
    n = len(source_list)
    start = 0
    end = 0
    while end <=n:
        end = min(start + block_size,n-1)
        print(start,end)
        if source_list[end]>=target:
            break
        start = end + 1
        end += block_size

    #TODO Use search_linear method and adjust the indexes

    found,index = search_linear(source_list[start:end+1],target)
    if found:
        return True, start+index
    return False,-1

  

if __name__ == "__main__":
    #TODO Create positive and negative case scenarios.
    print("--------- LINEAR SEARCH TEST ---------")

    unsorted_list = generate_random_unsorted_list()
    print("List:",unsorted_list)

    #Positive case
    target = unsorted_list[5]
    found,index = search_linear(unsorted_list,target)
    print("Positive case:",target,found,index)
    
    #Negative case
    target = -1
    found,index = search_linear(unsorted_list,target)
    print("Negative case:",target,found,index)


    print("\n--------- BINARY SEARCH TEST ---------")

    sorted_list = generate_random_sorted_list()
    print("List:",sorted_list)

    #Positive case
    target = sorted_list[5]
    found,index = search_binary(sorted_list,target)
    print("Positive case:",target,found,index)

    #Negative case
    target = -1
    found,index = search_binary(sorted_list,target)
    print("Negative case:",target,found,index)

    print("\n--------- JUMP SEARCH TEST ---------")

    print("List:",sorted_list)

    #Positive case
    target = sorted_list[5]
    found,index = search_jump(sorted_list,target)
    print("Positive case:",target,found,index)

    #Negative case
    target = -1
    found,index = search_jump(sorted_list,target)
    print("Negative case:",target,found,index)





   
        

