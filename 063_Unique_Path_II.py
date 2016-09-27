# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids.
# How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Key Point: DP same as 062_Unique_Paths
#            dp[i][j] = 0 if obstacle[i][j]==1
#            dp[i][j] = dp[i][j-1] + dp[i-1][j] if obstacle[i][j]==0
# Runtime: 68 ms

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]:
            return 0
        col, row = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0 for x in obstacleGrid[0]] for y in obstacleGrid]

        for i in xrange(0,row):
            for j in xrange(0,col):
                if i==0 and j==0:
                    dp[i][j] = 0 if obstacleGrid[i][j] else 1
                elif i==0:
                    dp[i][j] = 0 if obstacleGrid[i][j] else dp[i][j-1]
                elif j==0:
                    dp[i][j] = 0 if obstacleGrid[i][j] else dp[i-1][j]
                else:
                    dp[i][j] = 0 if obstacleGrid[i][j] else dp[i][j-1] + dp[i-1][j]
        return dp[row-1][col-1]