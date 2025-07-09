''''

Brute force method - Nested loops for creating all the substrings. Then use a helper function (with o(n) time complexity) to check if the substring 
created is a palindrome or not. If yes, update the counter. 

Time - o(n^3)
Space - o(1)

'''
class Solution(object):
    def checkPalindrome(self, s):
        left,right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True 

    def countSubstrings(self, s):
        n = len(s)
        res = 0

        for i in range(n):
            for j in range(i,n):
                if self.checkPalindrome(s[i:j+1]):
                    res += 1
        return res

''' Opimized approach - checking the palindromes for all the possible centers that can be used for creating the substrings 
Time - O(n^2) 
Space - O(1) 
'''

class Solution(object):

    def countSubstrings(self, s):
        n = len(s)
        res = 0
        
        for center in range(2*n - 1):
            left = center // 2
            right = left + (center % 2)
            
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        
        return res 

