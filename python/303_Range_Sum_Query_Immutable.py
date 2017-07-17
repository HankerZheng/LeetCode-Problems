# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.
# Subscribe to see which companies asked this question


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self._data = nums
        self._pre_sum = []
        for i,num in enumerate(nums):
            if i == 0:
                self._pre_sum.append(num)
            else:
                self._pre_sum.append(self._pre_sum[-1]+num)        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self._pre_sum[j]
        else:
            return self._pre_sum[j] - self._pre_sum[i-1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)