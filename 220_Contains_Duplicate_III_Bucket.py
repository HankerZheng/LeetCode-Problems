# Given an array of integers, find out whether there are two distinct indices 
# i and j in the array such that the absolute difference between nums[i] and nums[j]
# is at most t and the absolute difference between i and j is at most k.
# 

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums:
            return False
        if t < 0:
            return False
        buckets = {}
        rmIdx = 0
        bucketBase = t + 1
        for num in nums:
            bucketNum = num / bucketBase
            if bucketNum in buckets:
                return True
            if bucketNum + 1 in buckets and buckets[bucketNum + 1] - num <= t:
                return True
            if bucketNum - 1 in buckets and num - buckets[bucketNum - 1] <= t:
                return True
            buckets[bucketNum] = num
            if len(buckets) > k:
                buckets.pop(nums[rmIdx] / bucketBase)
                rmIdx += 1
        return Falsehttps://leetcode.com/submissions/detail/93116538/   