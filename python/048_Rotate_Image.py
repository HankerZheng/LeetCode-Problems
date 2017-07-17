# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Follow up:
# Could you do this in-place?

# Key Points: Swap nums from outer to inner
#             matrix[0][0] -> (0,n)
#             matrix[0][1] -> (1,n)
#             matrix[0][n] -> (n,n)
#             matrix[1][n] -> (n,n-1)
# 
#   starts from [0,0] to [0,n] to [n,n] to [n,0] 
#          from [1,1] to [1,n-1] to [n-1,n-1] to [n-1,0]
# 
# Runtime: 72ms

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def do_outer(base, top):
            for i in xrange(0, top-base):
                tmp = matrix[base][base+i]
                matrix[base][base+i] = matrix[top-i][base]
                matrix[top-i][base] = matrix[top][top-i]
                matrix[top][top-i] = matrix[base+i][top]
                matrix[base+i][top] = tmp 
        base = 0
        while base<len(matrix)/2:
            print base, len(matrix)-base-1
            do_outer(base, len(matrix)-base-1)
            base+=1

if __name__ == '__main__':
    sol = Solution()
    matrix0 = [ [1,2,3],
                [4,5,6],
                [7,8,9]]

    matrix1 = [ [1,2,3,4],
                [4,5,6,7],
                [7,8,9,0],
                [0,11,2,3]]
    matrix2 = [ [1,2],
                [3,4]]
    sol.rotate(matrix0)
    sol.rotate(matrix1)
    sol.rotate(matrix2)
    print matrix0
    print matrix1
    print matrix2