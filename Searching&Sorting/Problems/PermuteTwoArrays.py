# Permute two arrays that sum of every pair is greater or equal to K 

''' Solution 1: Using in-built python sorting function 
time - o(nlogn + nlogn + n) - sorting two arrays + iterating through the length once 
space - o(1) - sorting the arrays in place 
'''
def permuteArrs(arr1, arr2, K):
    
    # sorting both the arr1 
    arr1.sort() # asc
    arr2.sort(reverse = True) # dsc
    
    for i in range(len(arr1)):
        if arr1[i] + arr2[i] < K:
            return 'No'
    
    return 'Yes'

''' Solution2: Without using in-built function 
Bubble sorting algorithm 

time - o(n^2 + n^2)
space - o(1) - in-place sorting 
'''
def permuteArrs(arr1, arr2, K):
    
    n = len(arr1)
    
    # sorting in ascending order 
    for i in range(n):
        for j in range(0, n-i-1):
            if arr1[j+1] < arr1[j]:
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
                
    # sorting in descending order 
    for i in range(n):
        for j in range(0, n-i-1):
            if arr2[j] < arr2[j+1]:
                arr2[j+1], arr2[j] = arr2[j], arr2[j+1]
            
    
    for i in range(n):
        if arr1[i] + arr2[i] < K:
            return 'No'
    
    return 'Yes'


