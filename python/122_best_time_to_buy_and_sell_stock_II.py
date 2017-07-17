# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions
# as you like (ie, buy one and sell one share of the stock multiple times). However, you may
# not engage in multiple transactions at the same time (ie, you must sell the stock before
# you buy again).

# Subscribe to see which companies asked this question

# KeyPoints: Find the peak and valley
# Runtime: 80 ms
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sell = prices[0]
        buy = prices[0]
        maxprofit = 0
        i = 1
        while i < len(prices):
            while i<len(prices) and prices[i]>=prices[i-1]:
                i+=1
            maxprofit += prices[i-1] - buy
            while i<len(prices) and prices[i]<prices[i-1]:
                i+=1
            buy = prices[i-1]
        return maxprofit

if __name__ == '__main__':
    sol = Solution()
    print sol.maxProfit([1,2,3,4,3,2,1,2,3,4])
    print sol.maxProfit([1])
    print sol.maxProfit([])
    print sol.maxProfit([1,7,5,3,6,8])
