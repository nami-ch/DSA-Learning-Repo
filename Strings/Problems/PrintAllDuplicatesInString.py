# ------ using hash maps: to store the no. of times a character came in the string 
# ------- time -O(n) to iterate through the entire string to check frequencies for all the chars
# ------ space - O(k) - worst case n (all duplicates) else average case = k < n 

def printduplicates(s):
    freq = defaultdict(int)
    
    for char in s:
        freq[char] += 1
        
    ans = []
    
    for key in freq:
        if freq[key] > 1:
            ans.append([key, freq[key]])
            
    return ans
