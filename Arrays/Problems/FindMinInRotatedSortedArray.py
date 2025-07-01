'''
the first instance of num[i+1] < nums[i] when iterating over the array will give the lowest value
time - O(n) space - O(1)

'''
def findMin(self,nums):
    if not nums:
        return None
    
    # assumption: not pivoted
    result = nums[0]
    
    # if pivot is found: update result 
    for i in range(len(nums)-1):
        print(nums[i+1], nums[i])
        if nums[i+1] < nums[i]:
            result = nums[i+1]
    
    return result 
