'''Solution 1 (brute force method): iterating over the strings and for each one taken in the nested loop, 
check for all others and see if they have the same characters as the starting string. 
If yes, then sort the local ans and compare in res and append if not present - to aviod duplicates getting added 


Brute force method - this doesn't work for cases where aa in str1 and a in str2 
cause the frequency is not matching and thus wont be anagrams

Time - o(n^2 + n^2logn) 
Space - 2*(m*n)

Very bad solution in terms of performance 

'''
''' ********* this solution is incorrect but was the first approach that i thought of in the first attempt ***''''
def groupAnagrams(strs):
    n = len(strs)
    res = []
    
    # Brute force method 
    
    for i in range(n):
        local_res = [strs[i]]
        chars = set(strs[i])
        
        for j in range(n):
            
            if i != j:
                if set(strs[i]) == set(strs[j]):
                    local_res.append(strs[j])
                    
        local_res.sort()
        
        if local_res not in res:
            res.append(local_res)
    return res


''' solution 1: optimized from the above one and correct solution 
with each iteration - 
['eat']
['eat', 'tea']
['tan']
['eat', 'tea', 'ate']
['tan', 'nat']
['bat']
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

time = o(n*LlogL) = sorting each word of max length L 
space = o(n*L) = storing each word of max lenth L

'''
from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        # sort the word and use as key 
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
        
    return list(anagram_map.values())

'''solution 2: further optmization by removing the sorting method. instead of just keeping a tuple to count the frequencies of chars 
the characters can be only range in 26 alphabet letters 

time - o(n*l)
space - o(n*l)
'''
from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        # create a frequency count of 26 lettesr for the word 
        freq = [0] *26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
            
        key = tuple(freq) # tuples are hashable, so can be dict keys 
        anagram_map[key].append(word)
        
    return list(anagram_map.values())

