"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
"""

#
# Key Points: Heap. Maintain a heap with size k.
#
# Run time: 68 ms

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None:
            return None

        if k==1:
            return max(nums)
        if k==len(nums):
            return min(nums)

        from heapq import *

        heap = nums[:k]
        heapify(heap)
        for item in nums[k:]:
            if item > heap[0]:
                heapreplace(heap, item)
        return heap[0]