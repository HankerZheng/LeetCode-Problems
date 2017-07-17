# Given n non-negative integers representing the histogram's
# bar height where the width of each bar is 1, find the area
# of largest rectangle in the histogram.


# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.


# Key Points: 1) for the largest rectangle, the height must be one of the bar
#                Then, traverse the bars as every bar is the height of the rectangle
#                   2 - area = 2
#                   1 - area = 6
#                   5 - area = 10
#                   6 - area = 6
#                   2 - area = 6
#                   3 - area = 6
#                This sol would work, but result TL
# 
#              2) Stack. 
# 
# Runtime: 112ms

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights += [0]
        maxarea = 0
        stack = [0]
        for i, height in enumerate(heights):
            if i==0:
                continue
            if heights[i]>=heights[stack[-1]]:
                stack.append(i)
            else:
                c_posi = i
                while stack and heights[i]<heights[stack[-1]]:
                    posi = stack.pop(-1)
                    maxarea = max(maxarea, heights[posi]*(c_posi-stack[-1]-1 if stack else i))
                stack.append(i)
        return maxarea

    def largestRectangleArea_N2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxarea = 0
        for i, height in enumerate(heights):
            j, left, right = i-1, 0, 0
            while j>=0 and heights[j]>=heights[i]:
                left+=1
                j-=1
            j = i+1
            while j<len(heights) and heights[j]>=heights[i]:
                left+=1
                j+=1
            maxarea = max((left+right+1)*heights[i], maxarea)
        return maxarea

if __name__ == '__main__':
    sol = Solution()
    print sol.largestRectangleArea([4,2,0,3,2,5])

