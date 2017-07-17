# Find the contiguous subarray within an array (containing at least
# one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# Key Points: DP
#             dp[i] == dp[i-1] if nums[i] < 0
#             dp[i] == max(dp[i-1], current_sum) if nums[i] >= 0
#             where current_sum is the sum of contiguous positive nums to i.
# Runtime: 72ms

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for num in nums]        
        dp[0] = nums[0]
        max_sum = nums[0]
        for i in xrange(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            max_sum = max(dp[i], max_sum)
        return max_sum



if __name__ == '__main__':
    sol = Solution()
    print sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])