# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


from collections import Counter, defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # O(n) time to count all the elements
        frequencies = Counter(nums)
        # O(n) time to reverse the mapping
        freqAccess = defaultdict(list)
        for value, counts in frequencies.items():
            freqAccess[counts].append(value)
        # traverse from maxFreq to 0 to get top k
        thisFreq = len(nums)
        topK = []
        while thisFreq >= 0 and len(topK) < k:
            while thisFreq >= 0 and not freqAccess[thisFreq]:
                thisFreq -= 1
            topK.append(freqAccess[thisFreq].pop(-1))
        return topK