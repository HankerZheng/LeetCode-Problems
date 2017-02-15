# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k >= len(nums):
            return min(nums)
        import heapq
        myHeap = nums[:k]
        heapq.heapify(myHeap)
        for thisNum in nums[k:]:
            if thisNum > myHeap[0]:
                heapq.heapreplace(myHeap, thisNum)
        return myHeap[0]