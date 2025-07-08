'''Solution 1: Brute force method: making all possible substrings 
time - o(n^2) space - o(26) - since all alphabet characters are possible ''''
from collections import defaultdict
def characterReplacement(s, k):
    # Brute force method: Generate all the substrings 
    
    # Hashmap to maintain the frequencies of the characters in the string 
    n = len(s)
    max_length = 0 
    
    for i in range(len(s)):
        freq = defaultdict(int)
        max_freq = 0
        
        for j in range(i, n):
            freq[s[j]] += 1
            max_freq = max(max_freq, freq[s[j]])
            changes = (j - i + 1) - max_freq
            
            if changes <= k:
                max_length = max(max_length, j-i+1)
            else:
                break
            
    return max_length 

'''Solution 2: Sliding window + Two-pointer approach 
A sliding window is used wherever a contiguous substring/subarray is required of variable or fixed window 
time - o( (n+n)*26 ); 26 - for re-computing the max_freq in the hashmap 
space - o(26)
'''

from collections import defaultdict
def characterReplacement(s, k):
    # Optimized approach
    left,right = 0,0
    max_freq = 0
    max_length = 0 
    freq = defaultdict(int)
    
    while right < len(s):
        freq[s[right]] += 1
        max_freq = max(max_freq, freq[s[right]])
        
        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            max_freq = 0 
            for i in range(26):
                max_freq = max(max_freq, freq[i])
            left += 1
        
        if (right - left + 1) - max_freq <= k:
            max_length = max(max_length, (right - left + 1))
        right += 1
        
    return max_length 

'''Solution 3: Most optimized: Comparison to reevaluate the max_freq is not needed 
time - o(n)
space -o(26) '''

def characterReplacement(s,k):
    left,right = 0,0
    max_freq = 0
    max_length = 0
    freq = defaultdict(int)

    while right < len(s):

        freq[s[right]] += 1
        max_freq = max(max_freq, freq[s[right]])

        # condition if the substring is invalid - moving the left pointers
        if (right - left + 1) - max_freq > k:
            # if invalid, no point in reducing the max_freq and re-evaluating the max_length again as we know it has to be bigger than the current one for being the ans
            freq[s[left]] -= 1 #reducing the counter of that char
            left += 1 #moving the left pointer to start the new substring

     
        # if valid substring then update the max_length
        max_length = max((right - left + 1), max_length)
        # move the right pointer to check for further
        right += 1 

    return max_length
 
