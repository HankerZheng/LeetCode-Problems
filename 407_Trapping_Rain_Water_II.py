# Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

# Note:
# Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

# Example:

# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]

# Return 4.

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        def check_neighbor(x, y):
            ans = 0
            for dx, dy in delta:
                nx, ny = x+dx, y+dy
                if 0<=nx<rowN and 0<=ny<colN and (nx, ny) not in visited:
                    yield heightMap[nx][ny], nx, ny


        import heapq
        if not heightMap or not heightMap[0]: return 0

        delta = [(0,1), (1,0), (0,-1), (-1,0)]
        rowN = len(heightMap)
        colN = len(heightMap[0])
        count = 0
        # add the border into heap
        visited = set()
        heap = []
        for i in xrange(rowN):
            heap.append((heightMap[i][0], i, 0))
            heap.append((heightMap[i][colN - 1], i, colN - 1))
            visited.add((i, 0))
            visited.add((i, colN - 1))
        for j in xrange(1, colN - 1):
            heap.append((heightMap[0][j], 0, j))
            heap.append((heightMap[rowN-1][j], rowN - 1, j))
            visited.add((0, j))
            visited.add((rowN - 1, j))
        heapq.heapify(heap)

        count, height = 0, 0
        while heap:
            this_bar, x, y = heapq.heappop(heap)
            height = max(this_bar, height)
            for nh, nx, ny in check_neighbor(x,y):
                visited.add((nx, ny))
                if nh <= height:
                    count += height - nh
                heapq.heappush(heap, (nh, nx, ny))

        return count



if __name__ == '__main__':
    # matrix = [  [1,4,3,1,3,2],
    #             [3,2,1,3,2,4],
    #             [2,3,3,2,3,1]]
    matrix = [  [14,17,18,16,14,16],
                [17,3,10,2,3,8],
                [11,10,4,7,1,7],
                [13,7,2,9,8,10],
                [13,1,3,4,8,6],
                [20,3,3,9,10,8]]
    sol = Solution()
    print sol.trapRainWater(matrix)