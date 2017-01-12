# reference: http://www.geeksforgeeks.org/collect-maximum-points-in-a-grid-using-two-traversals/
# Given a matrix where every cell represents points. How to collect maximum points using two traversals under following conditions?

# Let the dimensions of given grid be R x C.
# 1) The first traversal starts from top left corner, i.e., (0, 0) and should
#    reach left bottom corner, i.e., (R-1, 0). The second traversal starts from
#    top right corner, i.e., (0, C-1) and should reach bottom right corner, i.e., (R-1, C-1)/
# 
# 2) From a point (i, j), we can move to (i+1, j+1) or (i+1, j-1) or (i+1, j)
# 
# 3) A traversal gets all points of a particular cell through which it passes.
#    If one traversal has already collected points of a cell, then the other
#    traversal gets no points if goes through that cell again.

# Input :
#     int arr[R][C] = {{3, 6, 8, 2},
#                      {5, 2, 4, 3},
#                      {1, 1, 20, 10},
#                      {1, 1, 20, 10},
#                      {1, 1, 20, 10},
#                     };
# 
#      Output: 73
# 
# Explanation :
# runninggrid
# First traversal collects total points of value 3 + 2 + 20 + 1 + 1 = 27
# 
# Second traversal collects total points of value 2 + 4 + 10 + 20 + 10 = 46.
# Total Points collected = 27 + 46 = 73.


# getPoint(row, i, j) - the max point we could get when the first traversal arrives
#       at grid[row][i] and the second arrives at grid[row][j]
#       Then we have the recurrence equation
#           getPoint(row, i, j) = MAX{getPoint(row-1, lasti, lastj)} over all possible `lasti`, `lastj`
#       with the constraints:
#           i <= min(row, nCol - 1 - row)
#           j >= max(nCol - 1 - row, nCol - nRow - row)
# 
# Time Complexity: O(M*N*N) - a 3-Dimension DP matrix

def maxPoint2Traversals(grid):
    """
    :type grid: list[list[int]]
    :rtype: int
    """
    def maxPointAtRow(row):
        """
        :type row: int
        :rtype: int

        return the max point we could get when arrive at row `row`
        """
        thisPoint = 0
        for i in xrange(nCol):
            for j in xrange(i + 1, nCol):
                if checkValid(row, i, j):
                    thisPoint = max(thisPoint, getPoint(row, i, j))
        return thisPoint

    def checkValid(row, i, j):
        """
        :type row: int
        :type i: int
        :type j: int
        :rtype: boolean

        make sure the input 2 col # satisfy the col constriants
        col# < MIN(row, nRow - row)
        """
        leftTraversal = i <= min(row, nRow - 1 - row)
        rightTraversal = j >= max(nCol - 1 - row, nCol - nRow + row)
        return i <= j and leftTraversal and rightTraversal

    def getPoint(row, i, j):
        """
        :type row: int
        :type i: int
        :type j: int
        :rtype: int
        
        Please check the validation of (row, i, j) before call this Function!!!
        return the max points we could get if we end at (row, i) and (row, j)
        """
        if (row, i, j) in history:
            return history[(row, i, j)]
        elif row == 0 and nCol > 1:
            return grid[0][0] + grid[0][nCol-1]
        elif row == 0 and nCol == 1:
            return grid[0][0]

        ans = 0
        for lasti in xrange(i-1, i+2):
            for lastj in xrange(j-1, j+2):
                if 0<=lasti<nCol and 0<=lastj<nCol and checkValid(row-1, lasti, lastj):
                    if i == j:
                        ans = max(ans, getPoint(row-1, lasti, lastj) + grid[row][i])
                    else:
                        ans = max(ans, getPoint(row-1, lasti, lastj) + grid[row][i] + grid[row][j])
        history[(row, i, j)] = ans
        return ans

    if not grid or not grid[0]: return 0
    history = {}
    maxPoint = 0
    nRow = len(grid)
    nCol = len(grid[0])
    return maxPointAtRow(nRow - 1)
    # to reduce the stress of the stack we could do
    # 
    # for row in xrange(nRow):
    #     maxPointAtRow(row)
    # return maxPoint(row)


if __name__ == '__main__':
    grid = [[3, 6, 8, 2],
            [5, 2, 4, 3],
            [1, 1, 20, 10],
            [1, 1, 20, 10],
            [1, 1, 20, 10]
    ]
    assert maxPoint2Traversals(grid) == 73