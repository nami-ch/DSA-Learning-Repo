''' Optimized solution - using three pointer approach 
time - o(m+n+o)
space - o(1) excluding output array if not then max(m,n,o) worst case 
''''

def findCommon(arr1, arr2, arr3):
    p1, p2, p3 = 0, 0, 0
    
    res = []
    
    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            # check for duplicates
            if not res or res[-1] != arr1[p1]:
                res.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        elif arr2[p2] < arr3[p3]:
            p2 += 1
        else:
            p3 += 1
            
    return res


''' Brute force: my solution - two pointer then check separetely for the last array 
Takes more space + time '''
def findCommon(arr1, arr2, arr3):
    n, m, o = len(arr1), len(arr2), len(arr3)
    p1, p2 = 0, 0
    res1 = []

    while p1 < n and p2 < m:
        if arr1[p1] == arr2[p2]:
            res1.append(arr1[p1])
            p1 += 1
            p2 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        else:
            p2 += 1

    res1 = [x for x in res1 if x in arr3]  # Fix: avoid modifying list in-place
    return res1
