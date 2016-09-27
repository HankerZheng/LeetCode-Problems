# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011

# Answer: 3



class UnionFind(object):
    def __init__(self, n):
        self._data = range(n)

    def find(self, index):
        stack = []
        this_element = index
        while self._data[this_element] != this_element:
            stack.append(index)
            this_element = self._data[this_element]
        ans = this_element
        while stack:
            this_element = stack.pop(-1)
            self._data[this_element] = ans
        return self._data[index]

    def union(self,index1, index2):
        parent1 = self.find(index1)
        parent2 = self.find(index2)
        self._data[parent1] = parent2

    def num_union(self):
        ans = set()
        for i in self._data:
            ans.add(self.find(i))
        return len(ans)


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def search_neighbor(this_x, this_y):
            for delta_x, delta_y in delta:
                x, y = this_x + delta_x, this_y + delta_y
                if 0 <= x < top_x and 0 <= y < top_y and grid[x][y] == "1" and (x*top_y +y) not in visited:
                    visited.add(x*top_y + y)
                    search_neighbor(x, y)

        if not grid or not grid[0]:
            return 0
        delta = [(0,1), (1,0), (-1,0), (0,-1)]
        top_x = len(grid)
        top_y = len(grid[0])
        count = 0
        visited = set()
        for i, line in enumerate(grid):
            for j, num in enumerate(line):
                if grid[i][j] == "1" and (i*top_y + j) not in visited:
                    visited.add(i*top_y+j)
                    search_neighbor(i, j)
                    count += 1
        return count

    def numIslands_unionFind(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def union_neighbor(this_x, this_y):
            for delta_x, delta_y in delta:
                x, y = this_x + delta_x, this_y + delta_y
                if 0 <= x < top_x and 0 <= y < top_y and grid[x][y]=="1":
                    unionFind.union(this_x*top_y + this_y, x*top_y + y)

        if not grid or not grid[0]:
            return 0
        delta = [(0,1), (1,0), (-1,0), (0,-1)]
        top_x = len(grid)
        top_y = len(grid[0])
        unionFind = UnionFind(top_x*top_y)
        water = 0
        for i, line in enumerate(grid):
            for j, num in enumerate(line):
                if num == '1':
                    union_neighbor(i,j)
                else:
                    water += 1
        return unionFind.num_union() - water


if __name__ == '__main__':
    sol = Solution()
    # grid = [    [1,1,1,1,0,0,0],
    #             [0,0,0,1,0,0,1],
    #             [0,0,1,0,1,0,1],
    #             [0,0,1,0,1,1,1],
    #             [0,1,1,0,0,0,1]]
    # grid = [ [1,1,1],
    #          [1,0,0],
    #          [0,0,1]]
    grid = ["111", "100", "001"]
    # grid = ["1", "1"]
    print sol.numIslands(grid)