''' Sorting + Binary Search the complement 

time - o(nlogn)
space - o(1)

brute force is nested loop taking o(n^2) time ''''

def binarySearch(arr,left,right,target):
    
    while left <= right: 
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return True 
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return False 


def findPairDiff(arr, x):
    
    arr.sort()
    n = len(arr)
    
    for i in range(n):
        
        complement = x + arr[i]
        
        if binarySearch(arr, i+1, n-1, complement):
            return True 
            
    return False 
