# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 <= k <= number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


from collections import Counter, defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def selection(nums, start, end):
            """
            Make tht first element of nums[start: end+1] as the pivot
            Do selection algorithm on that list and return the idx of the pivot
            """
            pivot = nums[start]
            while start < end:
                while start < end and freqDict[nums[end]] <= freqDict[pivot]:
                    end -= 1
                nums[start] = nums[end]
                while start < end and freqDict[nums[start]] >= freqDict[pivot]:
                    start += 1
                nums[end] = nums[start]
            nums[start] = pivot
            return start
                    
        # O(n) time to count all the elements
        freqDict = Counter(nums)
        keyList = freqDict.keys()
        thisRank = len(keyList)
        start, end = 0, len(keyList) - 1
        while thisRank != k:
            if thisRank > k:
                end = thisRank - 1
            elif thisRank < k:
                start = thisRank + 1
            thisRank = selection(keyList, start, end)
        return keyList[:thisRank]

if __name__ == '__main__':
    sol = Solution()
    print sol.topKFrequent([1,1,1,2,2,3], 2)