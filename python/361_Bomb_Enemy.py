# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.

# Example:
# For the given grid

# 0 E 0 0
# E 0 W E
# 0 E 0 0

# return 3. (Placing a bomb at (1,1) kills 3 enemies)
# Credits:
# For each enemy, find the place that could bomb it
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        up = [[0 for elem in line] for line in grid]
        down = [[0 for elem in line] for line in grid]
        right = [[0 for elem in line] for line in grid]
        left = [[0 for elem in line] for line in grid]
        ans = 0
        for i, line in enumerate(grid):
            for j, elem in enumerate(line):
                if elem == "W": continue
                if i == 0 and j == 0:
                    up[i][j] = 1 if elem == "E" else 0
                    left[i][j] = 1 if elem == "E" else 0
                elif i == 0:
                    up[i][j] = 1 if elem == "E" else 0
                    left[i][j] = left[i][j-1] + (1 if elem == "E" else 0)
                elif j == 0:
                    up[i][j] = up[i-1][j] + (1 if elem == "E" else 0)
                    left[i][j] = 1 if elem == "E" else 0
                elif elem != "W":
                    up[i][j] = up[i-1][j] + (1 if elem == "E" else 0)
                    left[i][j] = left[i][j-1] + (1 if elem == "E" else 0)
        for i in xrange(len(grid)-1, -1, -1):
            for j in xrange(len(grid[0])-1, -1, -1):
                elem = grid[i][j]
                if elem == "W": continue
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    down[i][j] = 1 if elem == "E" else 0
                    right[i][j] = 1 if elem == "E" else 0
                elif j == len(grid[0]) - 1:
                    down[i][j] = down[i+1][j] + (1 if elem == "E" else 0)
                    right[i][j] = 1 if elem == "E" else 0
                elif i == len(grid) - 1:
                    down[i][j] = 1 if elem == "E" else 0
                    right[i][j] = right[i][j+1] + (1 if elem == "E" else 0)
                elif elem != "W":
                    down[i][j] = down[i+1][j] + (1 if elem == "E" else 0)
                    right[i][j] = right[i][j+1] + (1 if elem == "E" else 0)
                if elem == "0":
                    ans = max(ans, down[i][j] + up[i][j] + right[i][j] + left[i][j])
        return ans
                
                    
                