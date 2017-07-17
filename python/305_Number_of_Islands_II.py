# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example:

# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# We return the result as an array: [1, 1, 2, 3]

class UnionFind(object):
    def __init__(self, size):
        self._data = [i for i in xrange(size)]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        self._data[pb] = pa

    def find(self, a):
        tmp = a
        queue = []
        while tmp != self._data[tmp]:
            queue.append(tmp)
            tmp = self._data[tmp]
        for pos in queue:
            self._data[pos] = tmp
        return tmp

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def checkNeighbor(x, y):
            islands = set()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) in land:
                    islands.add(unionFind.find(nx * n + ny))
            return islands


        unionFind = UnionFind(m*n)
        land = set()
        delta = [(0,1), (1,0), (-1,0), (0, -1)]
        ans = []
        curIslands = 0
        for pos in positions:
            x, y = pos[0], pos[1]
            neiIslands = checkNeighbor(x,y)
            curIslands += 1 - len(neiIslands)
            for island in neiIslands:
                unionFind.union(x*n+y, island)
            land.add((x, y))
            ans.append(curIslands)
        return ans