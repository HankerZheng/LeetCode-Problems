# Given an integer matrix, find the length of the longest increasing path.

# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

# Example 1:

# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].

# Example 2:

# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # This is a acyclic graph, could be done simply by mem_search
        def mem_search(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            ans = 0
            for dx, dy in delta:
                nx, ny = i + dx, j + dy
                if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]) and matrix[nx][ny] < matrix[i][j]:
                    ans = max(ans, mem_search(nx, ny))
            dp[i][j] = ans + 1
            return ans + 1

        if not matrix or not matrix[0]: return 0

        ans = 0
        delta = [[0,1], [1,0], [0,-1], [-1,0]]
        dp = [[ 0 for _ in matrix[0]] for __ in matrix]
        for i, line in enumerate(matrix):
            for j, _ in enumerate(line):
                ans = max(ans, mem_search(i,j))

        return ans