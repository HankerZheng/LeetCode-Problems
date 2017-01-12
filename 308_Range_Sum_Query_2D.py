# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self._data = [[0 for elem in line] for line in matrix]
        for i, line in enumerate(matrix):
            pre_sum = 0
            for j, elem in enumerate(line):
                pre_sum += elem
                self._data[i][j] = pre_sum
                
        

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if col == 0:
            delta = val - self._data[row][col]
        else:
            delta = val - (self._data[row][col] - self._data[row][col-1])
        
        for i in xrange(col, len(self._data[0])):
            self._data[row][i] += delta
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if col1 == 0:
            return sum([ self._data[i][col2] for i in xrange(row1, row2+1)])
        ans = 0
        i = row1
        while i <= row2:
            ans += self._data[i][col2] - self._data[i][col1 - 1]
            i += 1
        return ans
            
        

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)

if __name__ == '__main__':
    matrix = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]]
    sol = NumMatrix(matrix)
    print sol.sumRegion(0,1,2,3)
    print sol.update(1,1,10)
    print sol.sumRegion(0,1,2,3)
