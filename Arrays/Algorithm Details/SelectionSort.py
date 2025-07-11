''' 
------- Selection Sort --------

Comparison-based sorting algorithm. sorts an array by repeatedly selecting the smallest(or largest) element 
from the unsorted portion and swapping it with the first unsorted element

Time - O(n^2)
Space - O(1)

In-place sorting algorithm 

'''

def selectionSort(arr):
    
    n = len(arr)
    
    for i in range(n):
        # Assuming the current position holds the minimum element
        min_idx = i 
        
        # Iterate through the unsorted portion of the array to find the actual minimum
        for j in range(i+1,n):
            
            # updating the min idx if a smaller element is found
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Move the min element to its correct position        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
