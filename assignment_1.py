import time
import random

#random.seed(42)

def time_algorithm(algo, arr):
    start = time.time()
    algo(arr.copy())
    return time.time() - start

def selection_sort(arr):
    ''' Description: Sorts an inputted array (list) by identifying the minimum element and putting it at the front and continuing similarly. 

    Args: arr, an array of n numbers in arbitrary order.
    Returns: new_arr, the sorted version of arr.

    '''
    new_arr = arr

    n = len(new_arr)
    for i in range(n-1):
        smallest_element = min(new_arr[i:])

        new_arr[new_arr[i:].index(smallest_element)+i] = new_arr[i]

        new_arr[i] = smallest_element

        i += 1

    return new_arr

def merge_sort(arr):
    ''' Description: Sorts an inputted array (list).

    Args: arr, an array of n numbers in arbitrary order.
    Returns: new_arr, an array of the same numbers as arr sorted from smallest to largest. 

    '''
    C = arr[:len(arr)//2]
    D = arr[len(arr)//2:]

    c_sorted = C
    d_sorted = D

    if len(C) == 1 and len(D) == 1:
        return merge(C, D)

    if len(C) != 1:
        c_sorted = merge_sort(C)
    
    if len(D) != 1:
        d_sorted = merge_sort(D)

    return merge(c_sorted, d_sorted)

def merge(C, D):
    ''' Description: Merges two sorted arrays (lists) C and D in order from smallest to largest.
    
    Args: C, a sorted array (list) of numbers.
    Returns: D, a sorted array (list) of numbers.
    '''

    i = j = 0
    B = []

    while i < len(C) and j < len(D):
        if C[i] < D[j]:
            B.append(C[i])
            i += 1
        else:
            B.append(D[j])
            j += 1

    B.extend(C[i:])
    B.extend(D[j:])
    return B

# testing 
def test_arr(n):
    template = [i for i in range(n)]
    test = []

    length = n
    for i in range(n):
        test.append(template.pop(random.randint(0, length-1)))
        length += -1
        i += 1
    return test

test_100 = test_arr(100)
test_500 = test_arr(500)
test_1000 = test_arr(1000)
test_5000 = test_arr(5000)
test_10000 = test_arr(10000)

my_tests = [test_100, test_500, test_1000, test_5000, test_10000]

print("Sorting Algorithms:")
for i in range(5):
    print(i)
    for j in range(6):
        print(time_algorithm(merge_sort, my_tests[i]))

for i in range(5):
    print(i)
    for j in range(6):
        print(time_algorithm(selection_sort, my_tests[i]))