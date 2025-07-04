'''
1) Brute force: nested loops. try all possible combinations to find the sum. time-On^2) space - O(1)
2) Using extra space: store the complements in a hashset. find the number == complement then return it time - O(n) space - O(1)
3) Using two-pointer approach: 
  Using the conditions to correctly move the left and right pointers after finding the pivot is important. 
  Use modulus function to pick the remainder upon dividing by n 
  time - O(n) space - O(1)
'''

def PairSumInSortedRotated(arr):
    i = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            break
        
    # if whole array is sorted max element will be at last index
    if arr[i] <= arr[i+1]:
        i += 1
    
    l = (i + 1) % n # diving by length and picking the remainder 
    r = i 
        
    while l != r:
        if arr[l] + arr[r] == target:
            return True
        if arr[l] + arr[r] < target:
            l = (l+1)%n
        else:
            r = (r-1+n) % n # + n ensures no negative
    return False
