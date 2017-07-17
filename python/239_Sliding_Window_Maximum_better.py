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
# Key Points: If the new-in element is larger than the highest,
#             update the highest with that vaule.
#             If the kicked out element is equal to the highest,
#             update the current highest with max method

# Run time: 188 ms

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        ans = []
        highest = max(nums[:k])        
        for index in xrange(len(nums)-k):
            ans.append(highest)
            if nums[index+k] >= highest:
                highest = nums[index+k]
            elif nums[index] == highest:
                highest = max(nums[index+1:index+1+k])
        ans.append(max(nums[-k:]))
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