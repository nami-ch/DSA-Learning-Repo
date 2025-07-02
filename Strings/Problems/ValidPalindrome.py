# --- isalnum() function used to check if the character is alphanumeric or not. True is yes else False 
# --- updating the pointers till you find an alphanumeric character for comparison 
# --- time - O(n) space - O(1)

def isPalindrome(s):
    left,right = 0, len(s) -1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
    
