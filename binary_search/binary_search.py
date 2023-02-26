# binary search function

def binary_search(arr, x):
    """ 
    the function searches for the element x in a sorted array (with or without duplicates).
    we need 2 parameters for the function.
    arr: the sorted array to search
    x(int): the element to search for
    Returns the integer, the index of the element.
    If not found, returns -1.
    
     """
    # set an initial index number
    low = 0
    # the index of the last element in the array is 
    # always 1 less than the length of array
    high = len(arr) -1

    # infinit loop until low exceeds high
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    # if low exceeds high, return -1
    return -1

# Example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15]
x = 20
binary_result = binary_search(arr,x)

if binary_result != -1:
    print(f"Element {x} is present at index {binary_result}")
else:
    print(f"Element {x} is not in the array")