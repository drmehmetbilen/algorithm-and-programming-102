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


def generate_random_sorted_list(n:int=20, min_value:int=0, max_value:int=1000) ->list:
    new_list = []
    last_added = 0
    new_value = 0

    for i in range():
        # TODO Refine min/max value issue,
        new_value = random.randint(last_added +1,max(last_added,new_value))

        # Prevent value from exceeding max_value
        new_value = min(new_value,max_value)

        new_list.appen(new_value)

        last_added = new_value


    return new_list



def search_linear(source_list:list,target:int) ->tuple:

    for index in range(len(source_list)):
        if source_list[index] == target:
            return True, index
    
    return False , -1



def search_binary(source_list:list,target:int) ->tuple:

    # TODO Check if the source_list actually sorted. If not raise an error.
    
    # Check if list is sorted
    if not all(source_list[i] <= source_list[i+1] for i in range(len(source_list)-1)):
        raise ValueError("List must be sorted for binary search.")
    
    start = 0
    end = len(source_list)-1
    while start<end:
        mid = int((start + end) / 2)
        if target>source_list[mid]:
            start = mid + 1
        elif target<source_list[mid]:
            end = mid -1
        else :
           return True, mid
   
    return False, -1

def search_jump(source_list:list,target:int) ->tuple:
    block_size = int(len(source_list) ** 0.5)
    n = len(source_list)
    start = 0
    end = 0


    while end <= n :
        end = start + block_size
        # Prevent IndexError
        if end < n and source_list[end] > target:
            break 
        elif end >= n:
            break 

        start = end + 1
        end += block_size


    # TODO Use search_linear method and adjust the indexes
    
    # Use linear search for the specific block
    is_found, local_index = search_linear(source_list[start:min(end, n)], target)
    if is_found:
        return True, start + local_index
    return False, -1

    for i in range(start,end):
        if source_list[i]==target:
            return True, i
    
    return False, -1


if __name__ == "__main__":

    # TODO Create positive and negative case scenarios.
    
    # Test 1: Fixed list

    test_list = [10,20,30,40,50,60,70,80,90,100]

    print("Fixed List:", test_list)
    print("Search 70 (Positive):", search_linear(test_list, 70), search_binary(test_list, 70), search_jump(test_list, 70))
    print("Search 999 (Negative):", search_linear(test_list, 999), search_binary(test_list, 999), search_jump(test_list, 999))
    
    print("\n" + "-"*30 + "\n")
    
    # Test 2: Random sorted list
    my_list = generate_random_sorted_list(15, 0, 150)
    target = my_list[5] # Pick an existing element for positive test
    
    print("Random List:", my_list)
    print(f"Search {target} (Positive):")
    print("Linear:", search_linear(my_list, target))
    print("Binary:", search_binary(my_list, target))
    print("Jump:  ", search_jump(my_list, target))
    
    print(f"\nSearch 500 (Negative):")
    print("Linear:", search_linear(my_list, 500))
    print("Binary:", search_binary(my_list, 500))
    print("Jump:  ", search_jump(my_list, 500))







