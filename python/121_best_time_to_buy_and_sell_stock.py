# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one
# share of the stock), design an algorithm to find the maximum profit.

# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5

# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0

# In this case, no transaction is done, i.e. max profit = 0.
# Subscribe to see which companies asked this question

# Key Points: DP, dp[i] represents the max profit if sell stock on day i.
#             Then dp[i] = prices[i] - min(prices[:i])
# 
# Runtime: 68 ms

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float("inf")
        maxprofit = 0
        for i,price in enumerate(prices):
            if i == 0:
                continue
            minprice = min(minprice, prices[i-1])
            profit = prices[i] - minprice
            maxprofit = max(maxprofit, profit)
        return maxprofit

if __name__ == '__main__':
    sol = Solution()
    print sol.maxProfit([7,1,5,3,6,4])
    print sol.maxProfit([7, 6, 4, 3, 1])

