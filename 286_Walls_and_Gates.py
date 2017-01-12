# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# For example, given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        def getNeighbor(x, y):
            for dx, dy in delta:
                nx, ny = x+dx, y+dy
                if 0<=nx<len(rooms) and 0<=ny<len(rooms[0]) and rooms[nx][ny] != 0 and rooms[nx][ny] != -1:
                    yield (nx, ny)

        def updateRes(x, y):
            queue = [(x,y)]
            new_queue = []
            visited = set()
            dist = 0
            while queue:
                for tx, ty in queue:
                    rooms[tx][ty] = min(rooms[tx][ty], dist)
                    for nx, ny in getNeighbor(tx, ty):
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            new_queue.append((nx, ny))
                queue = new_queue
                new_queue = []
                dist += 1
            rooms[x][y] = 0

        if not rooms or not rooms[0]:   return
        delta = [(0,1), (1,0), (-1,0), (0,-1)]
        for i, line in enumerate(rooms):
            for j, elem in enumerate(line):
                if elem == 0:
                    updateRes(i, j)

if __name__ == '__main__':
    sol = Solution()
    matrix = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    sol.wallsAndGates(matrix)
    for line in matrix:
        print line