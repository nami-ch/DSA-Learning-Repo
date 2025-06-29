# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct
# Based on the requirement - Time optimized or Space optimized, the solution will change. Learn: different sorting algorithms 

# Solution 1: Using Hashset. Time - O(N) - to iterate over the array and Space - O(N) - worst case if the array doesn't have any duplicates 
def contains_duplicates(self, arr):
    # Edge case: if nums is empty or has only 1 element then duplicates = 0 
    if not arr or len(arr) == 1:
        return False
    
    # using hashset to track visited nums
    visited = set()
    
    # looping over the array to track nums
    for num in arr:
        if num not in visited:
            visited.add(num)
        else:
            return True
            
    return False

# Solution 2: Using sorting algorithm. Bubble sort - O(N^2). Python built-in .sort() --> Time -O(n log n) Space - O(1)
def contains_duplicates_sortingalo(self, arr):
    # Edge case: if nums is empty or has only 1 element then duplicates = 0 
    if not arr or len(arr) == 1:
        return False
    
    arr.sort()
    
    for i in range(len(arr) -1 ):
        if arr[i] == arr[i+1]:
            return True
    
    return False
