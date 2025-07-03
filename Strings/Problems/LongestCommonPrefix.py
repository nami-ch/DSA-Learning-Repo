# --- Keeping the first string as the prefix and checking the if the prefix== remaining strings,
# --- Reducing the length of the prefix while it is not equal to the remaining other strings
# -- Time - o(n) space - O(1)
def longestCommonPrefix(strs):
    prefix = strs[0]
    
    for s in strs[1:]:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
        
        if not prefix:
            return ''
            
    return prefix 
