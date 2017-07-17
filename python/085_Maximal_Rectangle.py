# Given a 2D binary matrix filled with 0's and 1's,
# find the largest rectangle containing only 1's and return its area.

# For example, given the following matrix:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 6.

# Key Points: DP as a line
#             dp[i] represents that the histogram based line i
#             dp[i] don't depend on dp[i-1], no need to maintain an array.
# 
#  10100 - dp = 1,0,1,0,0 - maxarea = 1
#  10111 - dp = 2,0,2,1,1 - maxarea = 3
#  11111 - dp = 3,1,3,2,2 - maxarea = 6
#  10010 - dp = 4,0,0,3,0 - maxarea = 4
# 
# Runtime: 212ms

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def calarea(nums):
            """
            calculate the maxarea from the nums.
            """
            nums += [0]
            maxarea = 0
            stack = [0]
            for i, height in enumerate(nums):
                if i == 0:
                    continue
                if height >= nums[stack[-1]]:
                    stack.append(i)
                else:
                    while stack and nums[stack[-1]]>height:
                        posi = stack.pop(-1)
                        maxarea = max(maxarea, nums[posi]*(i-stack[-1]-1 if stack else i))
                    stack.append(i)
            return maxarea

        if not matrix:
            return 0
        if len(matrix)==1:
            return calarea([int(ch) for ch in matrix[0]])
        histogram = [int(ch) for ch in matrix[0]]
        maxarea = calarea(histogram)
        for line in matrix[1:]:
            histogram = map(lambda x,y: x+y if y else 0, histogram, [int(ch) for ch in line])
            maxarea = max(maxarea, calarea(histogram))
        return maxarea

if __name__ == '__main__':
    sol = Solution()
    print sol.maximalRectangle(["101111011","010100000","000010110","111010101"])