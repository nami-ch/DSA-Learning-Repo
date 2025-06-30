
''' Problem statement: 

There is an integer array nums sorted in ascending order (with distinct values)

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums
Expected time complexity - O(logN)

'''

'''
Solution Steps:
Initialize low = 0 and high = len(nums) - 1.

While low <= high:

Calculate mid = (low + high) // 2.

If nums[mid] == target, return mid.

Determine which half is sorted:

If nums[low] <= nums[mid], then the left half is sorted.

Check if target lies between nums[low] and nums[mid].

Else, the right half is sorted.

Check if target lies between nums[mid] and nums[high].

If not found, return -1

'''
class Solution():
    def search_rotated_sorted_arr(self, nums, target):
        # For logN soln, binary search can be used but the arr has to be sorted. Need to find the pivot first 
        low, high = 0, len(nums) -1 
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
                
            # Left half is sorted 
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1 
        return -1
