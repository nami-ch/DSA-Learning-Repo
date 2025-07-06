''' Solution 1:
Intuition - Iterating over the array after sorting and check which all intervals can be clubbed together

[1, 3] [2,4] [3,6] - comparing arr[i][1] and arr[j][1] to see if they overlap 
after updating the ans, if the next interval is already part of the res then no need to perform the operation again. 
  if ans and arr[i][1] <= ans[-1][1]: continue 

Time - o(nlogn + 2n) 
  nlogn - for sorting 
  2n - because not iterating over the entire array two times due to continue or break statements 
  
Space - o(1) excluding ans list

'''
def mergeOverlaps(arr):
    # Step 1: Sort the intervals 
    arr.sort()
    
    # Step 2: Iterating over the array to check the intervals 
    # condition to check overlap: 
    # arr[j][0] < arr[i][1] - then overlapping 
    # then expanding the interval = arr[i][0] to arr[j][1] 
    ans = []
    n = len(arr)
    
    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]
        
        # if the next interval was already accumulated in the ans created then nothing has to be done for the current interval 
        if  ans and arr[i][1] <= ans[-1][1]:
            continue
        
        # if the interval is not part of the ans, then check to create new interval in ans 
        for j in range(i+1,n):
            if arr[i][1] >= arr[j][0]:
                end = max(arr[i][1], arr[j][1])
            else:
                break
    
        ans.append([start,end])
        
    return ans

'''
Solution 2: 

Starting ans intervals with the first element and creating a new addition in the ans list only if the intervals doesn't overlap
Else, checking and combining the intervals 

Time - o(nlogn + n) 
Space - o(1)

'''

def mergeOverlaps(arr):
    n = len(arr)
    arr.sort()
    
    ans = []
    
    for i in range(n):
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
            
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    
    return ans
