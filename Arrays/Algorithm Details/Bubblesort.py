'''
---------- Bubble sort -----------

Continuously swap the elements next to each other to take the largest element at the end of the array

time - o(n^2)
space - o(1)

In-place sorting 

'''

def bubbleSort(arr):
    
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        if not swapped:
            break # no swaps means array is already sorted 
            
                
    return arr
