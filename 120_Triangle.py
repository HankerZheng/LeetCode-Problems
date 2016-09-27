# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.

# Subscribe to see which companies asked this question

# Runtime: 116ms

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        old_dp = [0]
        for i,row in enumerate(triangle):
            this_dp = [0 for _ in row]
            if i == 0:
                this_dp = row
            else:
                for j,num in enumerate(row):
                    if j == 0:
                        this_dp[j] = old_dp[j] + num
                    elif j == len(row)-1:
                        this_dp[j] = old_dp[j-1] + num
                    else:
                        this_dp[j] = min(old_dp[j-1], old_dp[j]) + num
            old_dp = this_dp
        return min(old_dp)

if __name__ == '__main__':
    sol = Solution()
    print sol.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])