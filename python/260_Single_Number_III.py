# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

# For example:

# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        for i in xrange(32):
            if xor_sum & (1 << i):
                break
        num1, num2 = 0, 0
        for num in nums:
            if num & (1 << i):
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]