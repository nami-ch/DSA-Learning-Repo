# Finding the min and max elements in an array with the least no. of comparisons. 
def findMinMax(self, arr):
    # Edge case: if the array is empty 
    if not arr: 
        return None
        
    min_val, max_val = arr[0], arr[0]
    n = len(arr)
    
    for i in range(n):
        min_val = min(min_val, arr[i])
        max_val = max(max_val, arr[i])
    
    return [min_val, max_val]
