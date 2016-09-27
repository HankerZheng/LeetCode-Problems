# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# Subscribe to see which companies asked this question


# Runtime: 60 ms
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1], [1,1]]
        row = 2
        while row < numRows:
            i, ans = 0, []
            while i < len(res[-1])-1:
                ans+=[res[-1][i]+res[-1][i+1]]
                i+=1
            res.append([1]+ans+[1])
            row+=1
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.generate(0)
    print sol.generate(1)
    print sol.generate(2)
    print sol.generate(3)
    print sol.generate(4)
    print sol.generate(5)

