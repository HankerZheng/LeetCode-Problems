# Given an array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Subscribe to see which companies asked this question

# Rumtine: 52 ms

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xorsum = 0
        for i, num in enumerate(nums):
            xorsum ^= num
        return xorsum
