'''
---------- Insertion Sorting Algorithm ----------

iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list

time - o(n^2) 
space - o(1)

'''

def insertionSort(arr):
    
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i] # current element to be placed
        j = i - 1
        
        while j >= 0 and arr[j] > key: # shift the larger elements right 
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key 
        
    return arr
