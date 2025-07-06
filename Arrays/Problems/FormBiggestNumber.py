'''
Arrage given numbers to form the biggest number

input = [3,30,34,5,9] output= 9534303

sort(key=cmp_to_key(my_compare)) puts s1 before s2 when my_compare(s1, s2) returns -1.

A comparator function:
-1 -> s1 should come before s2 
0 -> s1 and s2 are equal in order 
1 -> s2 should come first 

cmp_to_key() creates a wrapper class where comparisons like <, ==, > are implemented using your my_compare function

sort elements A and B such that:
- if my_compare(A, B) returns -1 → A comes before B
- if my_compare(A, B) returns 1 → A comes after B

'''
from functools import cmp_to_key

def my_compare(s1, s2):
    if s1 + s2 > s2 + s1:
        return -1 
    else: 
        return 1 

def formBiggestNum(arr):
    # have to sort the numbers basis the first digits in the first, second, etc. places 
    numbers = [str(ele) for ele in arr]
    # sort the array using the customer comparator
    numbers.sort(key =cmp_to_key(my_compare))
    
    # Handling the case where all numbers are zero. We are sorting in descending order, so zero in front means complete array contains zero
    if numbers[0] == 0:
        return "0"
    
    return "".join(numbers)
