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
        maxreach = 0
        dest, i = len(nums)-1, 0
        while i<= maxreach:
            maxreach = max(maxreach, i+nums[i])
            if maxreach >= dest:
                return True
            i+=1
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.canJump([])
    print sol.canJump([1])
    print sol.canJump([0])
    print sol.canJump([0,1])
    print sol.canJump([3,2,1,0,1])