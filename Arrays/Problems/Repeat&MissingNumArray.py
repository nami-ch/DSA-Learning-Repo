'''
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example: Ip [3 1 2 5 3]
Op [3 4]

'''
class Solution():
    def repeatedNumber(self, A):
        # x1^2 + x2^2 + ... = n(n+1)(2n+1)/6 
        # x1 + x2 + x3 +... = n(n+1)/2
        
        '''
        B - A + sum = n(n+1)/2
        Therefore, B - A = n(n+1)/2 - sum 
        B^2 - A^2 + sum^2 = n(n+1)(2n+1)/6
        
        (A+B)(B-A) = n(n+1)(2n+1)/6 - sum^2
        Therefore, A + B = ( n(n+1)(2n+1)/6 - sum^2 ) / (B - A)
        
        '''
        n = len(A)
        actual_sum_of_elements = (n*(n+1))//2
        actual_sum_of_squares = (n*(n+1)*(2*n+1) )//6
        sum_of_elements = 0
        sum_of_squares = 0
        
        for i in range(n):
            sum_of_elements += A[i]
            sum_of_squares += A[i]*A[i]
        
        num1 = actual_sum_of_elements - sum_of_elements # b - a
        num2 = (actual_sum_of_squares - sum_of_squares)//num1 # b + a 
        b = (num1 + num2)//2
        a = b - num1
        
        return int(a), int(b)
    
