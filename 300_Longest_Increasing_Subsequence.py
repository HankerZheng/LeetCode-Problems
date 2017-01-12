# Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. 
# Note that there may be more than one LIS combination, it is only necessary for you to return the length.

# Your algorithm should run in O(n2) complexity.

# Follow up: Could you improve it to O(n log n) time complexity?

# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question


# DP Solution is obvious
# 
# NlogN solution is based on the fact that if there is several subsequence with the same length,
# say, [3,5,7,8], [3,6,8,9], [5,7,9,10], we would always choose the subsequence with the smallest
# ending element. Because all the elements which could be appended after the other 2 subsequences,
# could also be append on the list we choose.
# Based on this fact, we only need to keep track of one list for each length.
# 
# if the input list is [0, 8, 4, 12, 2, 10,| 6, 14, 1, 9, 5, 13 ,3]
# when we travese the array to the element 10, the list we keep should be
#   length 1: 0
#   length 2: 0, 2
#   length 3: 0, 2, 10
# The next element we get is 6, then we could update the list of length 3 with [0, 2, 6]
#   length 1: 0
#   length 2: 0, 2
#   length 3: 0, 2, 6
# The next element we get is 14, then we could add a list of length 4 with [0, 2, 6, 14]
#   length 1: 0
#   length 2: 0, 2
#   length 3: 0, 2, 10
#   length 4: 0, 2, 6, 14
# The next element we get is 1, then we could update the list of length 2 with [0, 1]
#   length 1: 0
#   length 2: 0, 1
#   length 3: 0, 2, 10
#   length 4: 0, 2, 6, 14
# The next element we get is 9, then we could update the list of length 4 with [0, 2, 9]
#   length 1: 0
#   length 2: 0, 2
#   length 3: 0, 2, 9
#   length 4: 0, 2, 6, 14
# And so on so forth.
# 
# To improve the algorithm, instead of keeping all the elements of each list, we could only
# keep track of the last element of each list.
# 
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        active = []
        for num in nums:
            if not active:
                active.append(num)
                continue
            if num <= active[0]:
                active[0] = num
            elif num > active[-1]:
                active.append(num)
            else:
                i = 0 
                while i < len(active) and num > active[i]:
                    i += 1
                active[i] = num
        return len(active)



    def lengthOfLIS_DP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0 for num in nums]
        for i, num in enumerate(nums):
            if i == 0:
                dp[i] = 1
                continue
            ans = 0
            for k in xrange(i):
                if nums[k] < nums[i]:
                    ans = max(dp[k], ans)
            dp[i] = ans + 1

        return max(dp)
