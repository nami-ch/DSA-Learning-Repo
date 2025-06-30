''' You want to maximize your profit by choosing 
a single day to buy one stock and choosing a different day in the future to sell that stock. ''''

class Solution():
    def maxProfit(self, prices):
        n = len(prices)
        profit = 0
        
        # Edge case: If the prices are given for only a single day 
        if not n or n == 1: 
            return 0
        
        # Brute forece - O(N^2)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         profit = max(profit, prices[j]-prices[i])
                
        # Optimized approach - two pointer approach 
        min_val, max_val = prices[0],prices[0]
        profit = 0
        
        for i in range(n):
            if prices[i] < min_val:
                min_val = prices[i]
                max_val = prices[i] 
            else:
                max_val = max(max_val, prices[i])
                profit = max(profit, max_val - min_val)
                
        return profit
