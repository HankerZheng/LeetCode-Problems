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

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def count_smaller(num):
            # Count the # of elements in the matrix that
            # is smaller than num.
            # Return the number and the largest left-border
            max_border = 0
            i, j = 0, len(matrix[0])-1
            count = 0
            while i < len(matrix) and j > 0:
                if num < matrix[i][j]:
                    j -= 1
                else:
                    max_border = max(max_border, matrix[i][j])
                    count += j+1
                    i += 1
            return count, max_border

        if k == 1:
            return matrix[0][0]

        start, end = matrix[0][0], matrix[-1][-1]
        while start <= end:
            mid = start + (end-start)/2
            count, max_border = count_smaller(mid)
            if count == k:
                return max_border
            elif count > k:
                end = mid - 1
            else:
                start = mid + 1
        return end

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
