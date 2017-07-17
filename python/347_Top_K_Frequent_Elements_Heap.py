# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # O(n) time to count all the elements
        frequencies = Counter(nums)
        frequentHeap = []
        for value, counts in frequencies.items():
            heapq.heappush(frequentHeap, (-counts, value))
        topK = []
        for i in xrange(k):
            counts, value = heapq.heappop(frequentHeap)
            topK.append(value)
        return topK