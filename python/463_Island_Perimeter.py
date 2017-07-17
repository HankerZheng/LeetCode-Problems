# You are given a map in form of a two-dimensional integer grid where 1 represents
# land and 0 represents water. Grid cells are connected horizontally/vertically 
# (not diagonally). The grid is completely surrounded by water, and there is exactly
# one island (i.e., one or more connected land cells). The island doesn't have "lakes"
# (water inside that isn't connected to the water around the island). One cell is 
# a square with side length 1. The grid is rectangular, width and height don't 
# exceed 100. Determine the perimeter of the island.

class Solution(object):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        perimeter = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    cnt = self.neighborLands(grid, i, j)
                    perimeter += (4 - cnt)
        return perimeter
    
    def neighborLands(self, grid, i, j):
        cnt = 0
        for index in xrange(4):
            ni, nj = i + Solution.dx[index], j + Solution.dy[index]
            if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj] == 1:
                cnt += 1
        return cnt
        
                