# Brute force - nested loop: Time -O(n^2) space - O(1)
def maxArea(height):
    # brute force method: nested loop
    water = 0
    n = len(height)
    
    for i in range(n):
        for j in range(n-1,i, -1):
            curr = min(height[i], height[j]) * (j-i)
            water = max(curr, water)
    return water
# Optimized solution: Using two-pointer | Time - O(n) space - O(1)
# the intuition for moving the pointers is that the min value one has to move cause the max capacity is already being tracked
def maxArea(height):
    # brute force method: nested loop
    water = 0
    n = len(height)
    left, right = 0, n - 1
    
    while left < right:
        # checking current capacity
        curr = min(height[left],height[right]) * (right - left)
        water = max(water, curr)
        
        # checking whichever is lower to move the pointer
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return water
