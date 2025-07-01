## Brute force method: Nested loops, time - O(N^2) space - O(1)
def maxProduct(self,nums):
    
    # Edge case: if the nums is empty 
    if not nums:
        return None
    
    max_prod = 1
    # brute force - possible subarrays 
    for i in range(len(nums)):
        local_prod = nums[i]
        for j in range(i+1,len(nums)):
            local_prod *= nums[j]
            max_prod = max(max_prod, local_prod)
    
    return max_prod

# Modified Kadane's algorithm to also maintain the min_prod and check - num, num*max_prod, num*min_prod to account for sign change due to -1 * -1
# Time - O(n) space - O(1)
def maxProduct(self,nums):
    
    # Edge case: if the nums is empty 
    if not nums:
        return None
    
    max_prod = nums[0]
    # Kadane's??? whether or not to include an element in the subarray or start from a new one. 
    # doesn't work directly. Maintain two variables to handle negatives 
    min_prod = nums[0]
    max_prod = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        # checking whether to start from a new element or continue the existing one
        temp_max = max_prod 
        max_prod = max(nums[i], temp_max*nums[i], min_prod*nums[i])
        min_prod = min(nums[i], temp_max*nums[i], min_prod*nums[i])
        
        result = max(result, max_prod)
        
    return result
