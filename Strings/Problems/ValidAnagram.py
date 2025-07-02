# ---- Anagram - the word created using rearranging the letters in the previous word. 
# ---- All the letters from the previous one should be present in the second word else its not a anagram 
# ---- Time - O(n+m) - iterating through the first string to count the letters and second to compare 
# ---- Space - O(n) - the first string's count of letters is stored for comparison 
def isAnagram(s,t):
    
    # Edge case: if lengths differ, they can't be anagrams 
    if len(s) != len(t):
        return False
    
    # count frequency of each character in s 
    count = defaultdict(int)
    for char in s:
        count[char] += 1
        
    # Subtract frequency based on characters in t 
    for char in t:
        count[char] -= 1
        # if any character count goes negative, they aren't anagrams
        if count[char] < 0:
            return False
            
    # if all counts are zero, they are anagrams        
    return all(value == 0 for value in count.values())
