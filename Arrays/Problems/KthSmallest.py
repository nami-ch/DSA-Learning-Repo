## Bubble sort algorithm || time -O(n^2) space - O(1)
def PairSumInSortedRotated(arr,k):
    # WITHOUT in-built sorting functions
    
    # Bubble sort
    n = len(arr)
    
    for i in range(n-1):
        # last element will get sorted as we pass through
        for j in range(n-i-1):
            
            if arr[j] > arr[j+1]:
                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)       
    return arr[k-1]

