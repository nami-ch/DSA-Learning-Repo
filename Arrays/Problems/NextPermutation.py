
'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
Given an array of integers nums, find the next permutation of nums.
'''

''' Solution intuition: 

We scan from the end to find the first decreasing element arr[i]:

This means everything to the right of i (i.e., arr[i+1:]) is in non-increasing order.

That part is already the highest possible permutation of those elements.

After swapping arr[i] with a slightly bigger number:

We need to make the remaining suffix (arr[i+1:]) the smallest possible to ensure the overall permutation is just the next one (not a big jump ahead).

The smallest permutation of a list is its sorted ascending version — and since arr[i+1:] was in decreasing order, we just reverse it to make it increasing.

'''
class Solution():
    def nextPermutation(self, arr):
        
        n = len(arr)
        
        # Step 1: Find the first decreasing index from the end 
        i = n -2
        while i >= 0 and arr[i] >= arr[i+1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find the next largest element to swap with
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
                
            arr[i], arr[j] = arr[j], arr[i]
        # Step 3: Reverse the subarray from i + 1 to end 
        arr[i +1:] = reversed(arr[i+1:])
        return arr
        
