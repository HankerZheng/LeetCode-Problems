# Given an array of non-negative integers, you are initially
# positioned at the first index of the array.

# Each element in the array represents your maximum jump length
# at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false.

# Subscribe to see which companies asked this question

# Show Tags

# Rumtime: 80 ms

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        curPos = 0
        maxReach = curPos + nums[curPos]
        while curPos < len(nums) and curPos <= maxReach:
            maxReach = max(maxReach, curPos + nums[curPos])
            curPos += 1
        return maxReach >= len(nums) - 1

if __name__ == '__main__':
    sol = Solution()
    print sol.canJump([])
    print sol.canJump([1])
    print sol.canJump([0])
    print sol.canJump([0,1])
    print sol.canJump([3,2,1,0,1])