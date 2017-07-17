# Given an array with n objects colored red,
# white or blue, sort them so that objects of
# the same color are adjacent, with the colors
# in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to
# represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.

# Runtime: 49 ms

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        zeroPos, twoPos = 0, len(nums) - 1
        currentPos = 0
        while currentPos <= twoPos:
            while nums[currentPos] == 2 and currentPos < twoPos:
                swap(currentPos, twoPos)
                twoPos -= 1
            while nums[currentPos] == 0 and currentPos > zeroPos:
                swap(currentPos, zeroPos)
                zeroPos += 1
            currentPos += 1
        