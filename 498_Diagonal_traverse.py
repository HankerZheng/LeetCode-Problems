# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order.

# Example 1:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:

# Note:
# The total number of elements of the given matrix will not exceed 10,000.

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ansList = []
        goingUp = True
        width = len(matrix[0])
        height = len(matrix)
        i = j = 0
        while i + j < width + height - 1:
            thisSum = i + j
            if goingUp:
                while 0 <= i < height and 0 <=  j < width:
                    ansList.append(matrix[i][j])
                    i -= 1
                    j += 1
                j = min(j, width - 1)
                i = thisSum + 1 - j
            else:
                while 0 <= i < height and 0 <=  j < width:
                    ansList.append(matrix[i][j])
                    i += 1
                    j -= 1
                i = min(i, height - 1)
                j = thisSum + 1 - i
            goingUp ^= True
        return ansList

if __name__ == '__main__':
    inputMatrix = [  [ 1, 2, 3 ],
                     [ 4, 5, 6 ],
                     [ 7, 8, 9 ]]
    sol = Solution()
    print sol.findDiagonalOrder(inputMatrix)