# Given an array of integers and an integer k,
# find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the difference between i and j is at most k.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashtable = {}
        for i, num in enumerate(nums):
            if num in hashtable and (i - hashtable[num]) <= k:
                return True
            hashtable[num] = i
        return False