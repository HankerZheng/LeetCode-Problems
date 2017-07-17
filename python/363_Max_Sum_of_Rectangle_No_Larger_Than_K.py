# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

# Example:
# Given matrix = [
#   [1,  0, 1],
#   [0, -2, 3]
# ]
# k = 2
# The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

# Note:
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def getMostSumSmallerThanK(nums, k):
            thisAns = float("-inf")
            nums.append(0)
            for startIdx in xrange(len(nums) - 1):
                for endIdx in xrange(startIdx, len(nums) - 1):
                    thisSum = nums[endIdx] - nums[startIdx-1]
                    if thisSum <= k:
                        thisAns = max(thisAns, thisSum)
            nums.pop(-1)
            return thisAns
                

        # parameter init
        finalSum = float("-inf")
        height, width = len(matrix), len(matrix[0])
        basicPresum = [[0 for j in xrange(width)] for i in xrange(height)]
        # O(mn) initialization
        for i in xrange(height):
            for j in xrange(width):
                if j == 0:
                    basicPresum[i][j] = matrix[i][j]
                else:
                    basicPresum[i][j] = basicPresum[i][j-1] + matrix[i][j]
        # main loop for this algorithm
        thisPresum = [[0 for j in xrange(width)] for i in xrange(height)]
        for rectHeight in xrange(height): # - O(n)
            rowIdx = 0
            while rowIdx + rectHeight < height: # O(n)
                for j in xrange(width): # - O(m)
                    thisPresum[rowIdx][j] = thisPresum[rowIdx][j] + basicPresum[rectHeight + rowIdx][j]
                thisSum = getMostSumSmallerThanK(thisPresum[rowIdx], k) # - O(m*m)
                finalSum = max(finalSum, thisSum)
                rowIdx += 1
        return finalSum if finalSum != float("-inf") else 0