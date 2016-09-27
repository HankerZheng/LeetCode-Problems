# Write an efficient algorithm that searches for a value
# in an m x n matrix. This matrix has the following properties:
# 
# 1. Integers in each row are sorted from left to right.
# 2. The first integer of each row is greater than the last integer
# of the previous row.
# 
# For example,
# Consider the following matrix:
# 
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

#
# Key Points:
#   1. Line search first and then 1D search
#         O(log(M)+log(N))
#   2. Consider all the element as one 1D list
#         O(log(M*N))
# 
# The first method is easier to write
#
# Run Time: 68 ms


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(matrix)-1
        while start<=end:
            mid = start+ (end-start)/2
            if matrix[mid][0]<target:
                start = mid+1
            elif matrix[mid][0]>target:
                end = mid-1
            else:
                return True
        lockLine = end # matrix[end][0] < target
        start, end = 0, len(matrix[lockLine])-1
        while start<=end:
            mid = start+(end-start)/2
            if matrix[lockLine][mid]<target:
                start = mid+1
            elif matrix[lockLine][mid]>target:
                end = mid-1
            else:
                return True
        return False
