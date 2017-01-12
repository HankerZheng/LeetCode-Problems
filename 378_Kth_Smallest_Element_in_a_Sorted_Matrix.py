# Given a n x n matrix where each of the rows and columns
# are sorted in ascending order, find the kth smallest elemen
# in the matrix.

# Note that it is the kth smallest element in the sorted order,
# not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.


import bisect
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def getRank(mid):
            minRank = maxRank = 0
            for i in xrange(len(matrix)):
                minRank += bisect.bisect_left(matrix[i], mid)
                maxRank += bisect.bisect_right(matrix[i], mid)
            return minRank, maxRank
        
        left, right = matrix[0][0], matrix[-1][-1]
        while left <= right:
            mid = (left + right) /2
            minRank, maxRank = getRank(mid)
            if minRank <= k <= maxRank:
                right = mid - 1
            elif maxRank < k:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    sol = Solution()
    matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
    print sol.kthSmallest(matrix, 2)
    matrix = [
   [1, 2],
   [1, 3]
]
    print sol.kthSmallest(matrix, 2)
