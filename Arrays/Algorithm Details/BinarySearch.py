''' Searching algorithm used in a sorted array by repeatedly dividing the search interval in half. Time - O(logN) worst case
    
    Steps:
    1. Divide the search space into two halves by finding the middle index 'mid'
    2. Compare the middle element of the search space with the key 
    3. If the key is found at the middle element, the process is terminated
    4. If the key is not found at middle element, choose which half will be used as the next search space 
      a. If th key is smaller than the middle element, LEFT side is used 
      b. If the key is larger than the middle element, RIGHT side is used 
    5. Continue till key is found or total search space is exhausted 
  Implementation:
    1. Iterative binary search algorithm
    2. Recursive binary search algorithm 

'''

''' ----------- ITERATIVE BINARY SEARCH ALGO ---------------- '''
def binarySearch(arr, x):
  low, high = 0, len(arr) - 1 # initializing the starting points on the left and right side 
  while low <= high:
    mid = low + (high -low) // 2 # high+low // 2 is not done as a safety for integer overflow in case of large int values 

    # check if x is present at mid 
    if arr[mid] == x: return mid 
    # If x is greater, ignore left half 
    elif arr[mid] < x: 
      low = mid + 1
    else: 
      high = mid - 1

    return -1 
