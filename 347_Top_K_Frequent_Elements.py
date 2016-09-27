# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 <= k <= number of unique elements.
# Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.

# Key Points: Traverse the nums and create a dict containing the freq info.
#             Maintain a k-sized min-heap and add items into that heap.
#
# Time Complexity: O(N+NlogK+K) = O(NlogK)
#
#
# Run Time: 1624 ms

from heapq import *
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return None
        freq = {}
        for num in nums:
            if num not in freq.keys():
                freq[num] = 1
            else:
                freq[num] += 1

        heap = []
        for item in freq.items():
            if len(heap) == k:
                if item[1] > heap[0][0]:
                    heapreplace(heap, (item[1], item[0]))
            else:
                heappush(heap, (item[1], item[0]))
        ans = []
        print heap
        while len(heap):
            ans.append(heappop(heap)[1])
        ans.reverse()
        return ans

if __name__ == "__main__":
    test = Solution()
    for n in xrange(1,7):
        ans = test.topKFrequent([1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,6,6,7], n)
        print ans
    ans = test.topKFrequent([1],1)
    print ans

