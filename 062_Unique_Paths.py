# A robot is located at the top-left corner of a m x n grid
# (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point
# in time. The robot is trying to reach the bottom-right corner
# of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Above is a 3 x 7 grid. How many possible unique paths are there?



# Key Points: DP
#             Subproblem dp[i][j] -- the number of paths to position(i,j)
#             dp[i][j] = dp[i-1][j] + dp[i][j-1]
# Runtime: 52 ms

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for x in xrange(n)] for y in xrange(m)] # dp[m][n]
        for i in xrange(1,m):
            for j in xrange(1,n):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.uniquePaths(3,6)