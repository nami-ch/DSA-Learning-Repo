'''
Find minimum number of merge operations to make an array palindrome

 The only allowed operation is"merging" (of two adjacent elements). Merging two adjacent elements means replacing them with their sum
 
 Expected time complexity = o(n)

'''
def mergeForPalindrome(arr):
    left, right = 0, len(arr) - 1
    res = 0
    
    while left <= right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        elif arr[left] > arr[right]:
                # merging operation at right index
                right -= 1
                arr[right] += arr[right + 1]
                res += 1
        else:
            left += 1
            arr[left] += arr[left-1]
            res += 1

    return res
    
