# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# Subscribe to see which companies asked this question

# Key Points: 1) profit[i] - the max profit got when sell at day i for the first time
#                profit[i] = prices[i] - min(prices[:i-1]) + maxprofit(prices[i+1:])
#                This sol is O(n^2)
#             2) first[i] - the max profit from the first day to i-th day
#                second[i] - the max profit form the i-th day to the last day
#                Then, profit[i] = first[i] + second[i]
#                where first[i] = max(first[i-1], prices[i]-lowest)
# 
# Runtime: 96ms

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        # in the first round, calculate first[i] which means
        # the max profit of first selling stock in i-th day
        first = [0 for _ in prices]
        buy1 = prices[0]
        for i, price in enumerate(prices):
            if i == 0:
                first[i] = 0
                continue
            buy1 = min(buy1, price)
            first[i] = max(price - buy1, first[i-1])
        # the the second round, calculate second[i] which means
        # the maxprofit of second buying stock in i-th day
        second = [0 for _ in prices]
        sell2 = prices[-1]
        for i in xrange(len(prices)-1, -1, -1):
            if i == len(prices)-1:
                second[i] = 0
                continue
            sell2 = max(sell2, prices[i])
            second[i] = max(sell2 - prices[i], second[i+1])

        maxprofit = 0
        for i in xrange(len(prices)):
            profit = first[i]+second[i]
            maxprofit = max(maxprofit, profit)
        return maxprofit

if __name__ == '__main__':
    sol = Solution()
    print sol.maxProfit([1,2])