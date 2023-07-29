# given a collection of numbers, find the pair 
# of numbers that sum to a given number



def bs(array, desired_num):

    start = 0
    end = len(array)
    mid = (end - start) // 2

    while len(array) > 0:
        if array[mid] == desired_num:
            return True
        elif array[mid] > desired_num:
            return bs(array[mid+1:], desired_num)
        else:
            return bs(array[:mid], desired_num)
    
    return False
    

def find_pairs_bs(array, desired_sum):

    for i in range(len(array)):
        num1 = array[i]
        desired_num = desired_sum - num1
        if bs(array[i + 1:], desired_num) == True:
            return (num1, desired_num)

    return False


def find_pairs_max_sum(array, desired_sum):

    i, j = 0, len(array) - 1

    while i < j:
        if array[i] + array[j] == desired_sum:
            return array[i], array[j]
        elif array[i] + array[j] > desired_sum:
            j = j - 1
        elif array[i] + array[j] < desired_sum:
            i = i + 1
            
    return False

def find_pairs_not_sorted(array, desired_sum):

    lookup = {}

    for item in array:
        key = desired_sum - item

        if key in lookup.keys():
            lookup[key] += 1
        else:
            lookup[key] = 1

    for item in array:
        key = desired_sum - item

        if item in lookup.keys():
            if lookup[item] == 1: 
                return (item, key)
            else:
                lookup[item] -= 1

    return False



if __name__ == "__main__":

    desired_sum = 8
    array1 = [1, 2, 3, 9]
    array2 = [1, 2, 4, 5, 4]
    array3 = [2, 1, 6, 3, 11, 2]

    assert(find_pairs_bs(array1, desired_sum) == False)
    assert(find_pairs_bs(array2, desired_sum) == (4, 4))
    assert(find_pairs_max_sum(array1, desired_sum) == False)
    assert(find_pairs_max_sum(array2, desired_sum) == (4,4))
    assert(find_pairs_not_sorted(array1, desired_sum) == False)
    assert(find_pairs_not_sorted(array2, desired_sum) == (4, 4))
    assert(find_pairs_not_sorted(array3, desired_sum) == (2, 6))
