# Instead of iterating through the array with '1' step in a for loop
# Leveraging the presence of steps and jumping to the abs(arr[i] - x)/ k steps 

'''
time < o(n)
space - o(1)
'''

def searchAdjacent(arr, k, x):
    # brute force- iterate through the array and find the element 
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == x:
            return i 
        
        # instead of moving i += 1, jumping the diff between current and x divided by k
        i = i + max(1, int(abs(arr[i] - x) / k))
    
    return -1 
