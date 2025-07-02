'''
Brute force method: Nested for loops
Time - O(N^2) Space - O(1)
'''
def pairInSortedRotated(self, nums,target):
    # Edge case: if empty array or len(arr) == 1 then pair of elements not possible
    if not nums or len(nums) == 1:
        return None
    
    n = len(nums)
    
    # Brute force method: Nested loops 
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True

    return False
  
'''
Solution 2: Using hash map (extra space) to store the complements of the elements in the array
Time - O(N) Space - O(N)
'''

def pairInSortedRotated(self, nums,target):
    # Edge case: if empty array or len(arr) == 1 then pair of elements not possible
    if not nums or len(nums) == 1:
        return None
    
    n = len(nums)
    # Soln 2: Using extra space (hashmap) to store the complements 
    
    complements = {}
    
    for i in range(n):
        if nums[i] in complements:
            return True
        else:
            complements[target - nums[i]] = i
    return False
'''
Solution 3: Finding the pivot and rearranging to get the original array 
Still not optimized. 
Time - O(n) Space - O(n) creation of new array in the original order 
'''

def pairInSortedRotated(self, nums,target):
        # Edge case: if empty array or len(arr) == 1 then pair of elements not possible
        if not nums or len(nums) == 1:
            return None
        
        n = len(nums)
        pivot = 0
        
        # Soln3: Most Optimized -
        
        # Step 1: Finding the pivot 
        for i in range(n-1):
            if nums[i+1] < nums[i]:
                pivot = i+1
        
        # Step 2: Updating the array to sort it before rotation 
        nums = nums[pivot:] + nums[:pivot]
        
        # Step 3: Using two-pointers to find the pair of elements = target
        left, right = 0, n-1
        while left < right:
            if nums[left] + nums[right] == target: 
                return True
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return False
'''
Solution 4: rotational index 
Msot optimized
Time - O(n) Space - O(1) 
'''
  def pairInSortedRotated(self, nums,target):
      # Edge case: if empty array or len(arr) == 1 then pair of elements not possible
      if not nums or len(nums) == 1:
          return None
      
      n = len(nums)
      
      # Solt4 (most optimized): without reversing the array back and doing circulatory index 
      # Step 1: finding pivot (i)
      for i in range(n -1):
          if nums[i] > nums[i+1]:
              break
      else:
          i =- 1 # not rotated, fully sorted 
      
      left = (i+1) % n # smallest element 
      right = i        # largest element 
      
      # step 2: use two pointers in circular manner
      while left != right:
          current_sum = nums[left] + nums[right]
          if current_sum == target:
              return True
          elif current_sum < target:
              left = (left + 1) % n
          else:
              right = (n + right - 1) % n
              
      return False


