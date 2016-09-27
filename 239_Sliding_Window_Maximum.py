# Given an array nums, there is a sliding window of size k which is
# moving from the very left of the array to the very right. You can
# only see the k numbers in the window.
#
# Each time the sliding window moves right by one position.

# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].

# Note: 
# You may assume k is always valid, ie: 1 <= k <= input array's
# size for non-empty array.

#
# Key Points: Maintain 2 maxheap, one is for slidingWindow, the other
#             is for invalid elements
#
#             Everytime, add the first element into the ans list and
#             slide the window one position right.
#
#             If the element kicked off from the slidingWindow is the
#             current max element, pop the element out and keep popping
#             until the max is not equal to the invalid element.
#             If not, push the element into invalid list.

# Run time: 356 ms

from heapq import *

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        ans, invalid, maxheap = [], [], [-x for x in nums[:k]]
        index = 0
        heapify(maxheap)
        while index < len(nums)-k:
            ans.append(-maxheap[0])
            if nums[index] == -maxheap[0]:
                # When the element would be invalid is the max
                heappop(maxheap)
                while maxheap and invalid and maxheap[0] == invalid[0]:
                    heappop(maxheap)
                    heappop(invalid)
            else:
                # Else, just add the last element into invalid
                heappush(invalid, -nums[index])
            heappush(maxheap, -nums[index+k])
            index += 1
        ans.append(-maxheap[0])

        return ans

if __name__ == "__main__":
    test = Solution()
    testcases = [ ([1,3,-1,-3,5,3,6,7],3),
                 ([], 0),
                 ([1], 1),
                 ([1,2,3], 3),
                 ([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 7),
                 ([5,2,1,3,4,5,7,8,4,21,2,3], 7)
                ]
    for testcase in testcases:
        res = test.maxSlidingWindow(testcase[0], testcase[1])
        print "Input is %s, k=%s" % testcase
        print "Answer is %s" % res
        print 