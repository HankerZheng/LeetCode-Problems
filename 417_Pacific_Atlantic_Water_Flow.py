# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:

# Given the following 5x5 matrix:

#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic

# Return:

# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def mem_fill(x, y, ocean):
            dp[x][y] |= ocean
            for dx,dy in delta:
                nx, ny = x+dx, y+dy
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] >= matrix[x][y] and not (dp[nx][ny] & ocean):
                    mem_fill(nx, ny, ocean)
        # 1 for Pacific, 8 for Atlantic, others for both
        if not matrix or not matrix[0]:
            return []
        delta = [ [0,1],[1,0], [-1,0], [0,-1]]
        res = []
        PACIFIC = 1
        ATLANTIC = 8
        dp = [[0 for _ in matrix[0]] for __ in matrix]
        for i, _ in enumerate(matrix):
            mem_fill(i, 0, PACIFIC)
            mem_fill(i, len(matrix[0]) - 1, ATLANTIC)

        for j, _ in enumerate(matrix[0]):
            mem_fill(0, j, PACIFIC)
            mem_fill(len(matrix) - 1, j, ATLANTIC)
        return [[i,j] for i in xrange(len(matrix)) for j in xrange(len(matrix[0])) if dp[i][j] == 9]

if __name__ == '__main__':
    sol = Solution()
    # print sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
    print sol.pacificAtlantic([[3,3,3,3,3,3],[3,0,3,3,0,3],[3,3,3,3,3,3]])