# Given a m x n matrix, if an element is 0, set its entire row
# and column to 0. Do it in place.

# click to show follow up.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems

# Runtime: 200ms

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        column_zero = []
        for i, row in enumerate(matrix):
            flag = 0
            for j,num in enumerate(row):
                if num == 0:
                    column_zero.append(j)
                    flag = 1
            if flag:
                matrix[i] = [0 for _ in row]
        for col in column_zero:
            for i,row in enumerate(matrix):
                matrix[i][col] = 0

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,2,3],
              [2,3,4],
              [3,4,0]]
    sol.setZeroes(matrix)
    print matrix 