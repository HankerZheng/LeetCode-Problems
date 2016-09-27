# Given an integer n, generate a square matrix filled
# with elements from 1 to n^2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
# Subscribe to see which companies asked this question


# Rumtime: 64ms
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def do_border(base_x, base_y, top_x, top_y, start):
            num = start
            for i in xrange(base_y, top_y):
                res[base_x][i] = num
                num+=1
            for i in xrange(base_x, top_x):
                res[i][top_y] = num
                num+=1
            for i in xrange(top_y, base_y, -1):
                res[top_x][i] = num
                num+=1
            for i in xrange(top_x, base_x, -1):
                res[i][base_y] = num
                num+=1
            return num

        res = [[0 for _ in xrange(n)] for __ in xrange(n)]
        next = 1
        base_x, base_y, top_x, top_y = 0,0,n-1,n-1
        while base_x<top_x and base_y<top_y:
            next = do_border(base_x, base_y, top_x, top_y, next)
            base_x+=1
            base_y+=1
            top_x-=1
            top_y-=1
        if base_x==top_x:
            res[base_x][base_y] = next
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.generateMatrix(0)
    print sol.generateMatrix(1)
    print sol.generateMatrix(2)
    print sol.generateMatrix(3)
    print sol.generateMatrix(4)