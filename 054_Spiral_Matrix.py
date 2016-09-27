# Given a matrix of m x n elements (m rows, n columns),
# return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


# Key Point: Same like Rotate Image.
#            Do the outer then the inner.
# Runtime: 60ms

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def do_outer(base_x, base_y, top_x, top_y):
            for num in matrix[base_x][base_y:top_y]:
                res.append(num)
            for i in xrange(base_x, top_x):
                res.append(matrix[i][top_y])
            for i in xrange(top_y, base_y, -1):
                res.append(matrix[top_x][i])
            for i in xrange(top_x, base_x, -1):
                res.append(matrix[i][base_y])
        if not matrix:
            return []
        res = []
        base_x, base_y, top_x, top_y = 0,0,len(matrix)-1, len(matrix[0])-1
        while base_x<top_x and base_y<top_y:
            do_outer(base_x, base_y, top_x, top_y)
            base_x+=1
            base_y+=1
            top_x-=1
            top_y-=1

        if base_x == top_x and base_y == top_y:
            res.append(matrix[base_x][base_y])
        elif base_x == top_x:
            for num in matrix[base_x][base_y:top_y+1]:
                res.append(num)
        elif base_y == top_y:
            for i in xrange(base_x, top_x+1):
                res.append(matrix[i][base_y])
        return res

if __name__ == '__main__':
    sol = Solution()
    matrix0 = [[ 1, 2, 3 ],
              [ 4, 5, 6 ],
              [ 7, 8, 9 ]]
    matrix1 = [[ 1, 2, 3 ],
              [ 4, 5, 6 ],
              [ 7, 8, 9 ],
              [ 0, 1, 2 ]]
    print sol.spiralOrder(matrix0)
    print sol.spiralOrder(matrix1)
    print sol.spiralOrder([])
    print sol.spiralOrder([[1]])
    print sol.spiralOrder([[1,2,3,4]])
    print sol.spiralOrder([[1],[2],[3],[4]])