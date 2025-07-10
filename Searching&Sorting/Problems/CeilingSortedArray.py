# Brute force or Naive solution 
def findCeiling(arr, x):
    
    for i in range(len(arr)):
        
        if arr[i] > x:
            return i
    
    return -1

'''
 optimzied - 
 time - o(logn) using binary search algo cause the array is sorted 
 space - o(1)
 '''

def findCeiling(arr, x):
    
    left, right = 0, len(arr) -1 
    res = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] < x:
            left = mid + 1
        else: # potential ceiling found 
            res = mid 
            right = mid - 1
        
    return res 
        
