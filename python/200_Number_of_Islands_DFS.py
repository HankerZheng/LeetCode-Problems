class Solution(object):
    deltaPos = [[0,1], [1,0],[-1,0],[0,-1]]
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        count = 0
        visitedPos = set()
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if (i, j) not in visitedPos and grid[i][j] == "1":
                    count += 1
                    visitedPos.add((i,j))
                    self.markAllNeighborLand(grid, i, j, visitedPos)
        return count
    
    def markAllNeighborLand(self, grid, i, j, visitedPos):
        for di, dj in self.deltaPos:
            ni, nj = i + di, j + dj
            if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and (ni, nj) not in visitedPos and grid[ni][nj] == "1":
                visitedPos.add((ni, nj))
                self.markAllNeighborLand(grid, ni, nj, visitedPos)

if __name__ == '__main__':
    sol = Solution()
    testGrid = []
    print sol.numIslands(testGrid)
    testGrid = ["010","110", "000"]
    print sol.numIslands(testGrid)
    testGrid = ["010","011", "000"]
    print sol.numIslands(testGrid)
    testGrid = ["110","100", "000"]
    print sol.numIslands(testGrid)
    testGrid = ["110","010", "000"]
    print sol.numIslands(testGrid)