# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules, return -1.


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def getNeighbor(x, y):
            for dx, dy in delta:
                nx, ny = x+dx, y+dy
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == 0:
                    yield (nx, ny)
            
        def updateRes(x, y):
            # calculate dist from all the empty slots in the grid
            # to the position (x,y)
            queue = [(x,y)]
            new_queue = []
            visited = set()
            dist = 0
            while queue:
                for thisx, thisy in queue:
                    res[thisx][thisy] += dist
                    for nei in getNeighbor(thisx, thisy):
                        if nei not in visited:
                            visited.add(nei)
                            new_queue.append(nei)
                dist += 1
                queue = new_queue
                new_queue = []
            return visited
        
        # check the boundary condition
        if not grid or not grid[0]: return -1
        # init the res matrix and other params
        res = [[0 for _ in line] for line in grid]
        reachable = set([(i,j) for j,_ in enumerate(line) for i,line in enumerate(grid)])
        delta = [(0,1), (1,0), (0,-1), (-1,0)]
        # traverse the grid, update the res matrix if elem == "1"
        for i, line in enumerate(grid):
            for j, elem in enumerate(line):
                if elem == 1:
                    visited = updateRes(i, j)
                    reachable &= visited
                    if not reachable:   return -1
        # traverse the res matrix to get the ans
        ans = float("inf")
        for i, line in enumerate(res):
            for j, elem in enumerate(line):
                if (i, j) in reachable:
                    ans = min(ans, elem)
        if ans == float("inf"):
            return -1
        return ans
