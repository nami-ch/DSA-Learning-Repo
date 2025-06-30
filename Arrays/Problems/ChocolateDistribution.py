''' Given an array arr[] of n integers where arr[i] represents the number of chocolates in ith packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

i) Each student gets exactly one packet.
ii) The difference between the maximum and minimum number of chocolates in the packets given to the students is minimized

Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 3 
Output: 2 
Explanation: If we distribute chocolate packets {3, 2, 4}, we will get the minimum difference, that is 2. 
'''

''' Sliding window approach post sorting the array (without sorting only the sliding window might not work because the packets may not be consecutive necessarily) '''
''' Time complexity - O(nlogn + n/m + 1 ) Space - o(1) '''
''' Brute force method would be to make all possible subsets of size m from the original array. Time - O(N^M) ''''

class Solution():
    def chocolate_dist(self, arr, m):
        if len(arr) < m:
            return None
            
        arr.sort() # Sorting because sliding window wont work without

        diff = arr[len(arr)-1] - arr[0] # setting it to a larger value in the beginning 
        
        # Iterate over the array with the specified window 
        for i in range(len(arr) - m + 1):
            diff = min(arr[i+m-1] - arr[i], diff)
            
        return diff
