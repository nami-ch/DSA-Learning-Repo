# Given an integer array nums, find the subarray with the largest sum, and return its sum

# Brute force - O(N^2) time and O(1) space
def maxSubarray_bruteforce(self, arr):
    # Edge case: If the array is empty, sum is 0
    if not arr:
        return 0
    
    n = len(arr)
    # brute force method: to create all possible subarrays and maitain a variable for max subarray sum 
    max_sum = nums[0] # lowest value
    
    for i in range(n):
        local_sum = arr[i]
        for j in range(i+1,n):
            local_sum += arr[j]
            max_sum = max(max_sum, local_sum)
            
    return max_sum

# Optimized approach using Kadane's algorithm. Time - O(N) and Space- O(1)
def maxSubarray_optimized(self, arr):
    # Edge case: If the array is empty, sum is 0
    if not arr:
        return 0
    
    n = len(arr)
    # Optimized approach - Kadane's algorithm
    
    # Initializing variables
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num) # include or restart # this decides whether to start from a new element or continue the current one. 
        max_sum = max(max_sum, current_sum)
    
    return max_sum 

# ----- Test cases ----- # 
# Input: [5, -5, 6] == Kadane's. current = 5 + -5 = 0 num = -5 hence, current = 0. max (when moving the pointer) = 0 + 6 = 6 (continuing with the previous one) 
# Input: [-5, 6] == Kadane's. currnet = -5 max = -5, current = max(6, 6 + -5 = 1) = 6 max = 6 (new element got picked) 

