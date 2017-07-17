# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes
# the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Subscribe to see which companies asked this question

# Key Point: DP
#            Subproblem: dp[i][j] the minimum path sum to position(i,j)
#            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
# 
# Runtime: 84ms
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col, row = len(grid[0]), len(grid)
        dp = [[0 for x in grid[0]] for y in grid]
        for i in xrange(row):
            for j in xrange(col):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                elif i==0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j==0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[row-1][col-1]

if __name__ == '__main__':
    sol = Solution()
    grid = [[1,2,3], [2,3,4], [3,4,5]]
    print sol.minPathSum(grid)