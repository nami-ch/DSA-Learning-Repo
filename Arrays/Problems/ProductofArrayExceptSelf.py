class Solution():
    def productExceptSelf(self,nums):
        
        # ** solution 1: brute force: nested (2) for loops for multiple the numbers except itself ** #
        # ** solution 2: using prefix and suffix products ** # Time - O(3N) ~ O(N) Space - O(2N) for storing prefix and suffix sums
        n = len(nums)
        ans = [0]*n
        
        left_multiples = [1]*n
        right_multiples = [1]*n
        
        for i in range(1,n):
            left_multiples[i] = left_multiples[i-1] * nums[i-1]
        
        for j in range(n-2, -1,-1):
            right_multiples[j] = right_multiples[j+1]*nums[j+1]
        
        for i in range(n):
            ans[i] = left_multiples[i] * right_multiples[i]
        
        return ans
      
    # ** solution 3: pass one by one and multiple the result without storing ** # Time - O(3N) ~ O(N) Space - O(1) 
    def productExceptSelf_optimized(nums):
      n = len(nums)
      output = [1]*n
      # Step 1: Left product pass 
      left_product = 1
      for i in range(n):
        output[i] = left_product
        left_product *= nums[i]

      # Step 2: Right product pass 
      right_product = 1
      for i in range(n-1,-1,-1):
        output[i] += right_product
        right_product += nums[i]

      return output 
