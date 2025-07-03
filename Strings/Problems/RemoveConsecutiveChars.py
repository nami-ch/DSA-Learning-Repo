#--- solution 1----#
def removeConsecutive(s):
    # Soln 1: Using extra space for storing unique elements
    # Time - O(n) Space - O(n)
    unique = set()
    
    for char in s:
        if char not in unique:
            unique.add(char)
    
    return ''.join(unique)
#--- solution 2----#
def removeConsecutive(s):
    # Sol2: For preserving the original order of the characters
    seen = set()
    result = []
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return "".join(result)
