# After robbing those houses on that street,
# the thief has found himself a new place for his thievery so that he will not get too much attention.
# This time, all houses at this place are arranged in a circle. 
# That means the first house is the neighbor of the last one. 
# Meanwhile, the security system for these houses remain the same as for those in the previous street.

# Given a list of non-negative integers representing the amount of money of each house, 
# determine the maximum amount of money you can rob tonight without alerting the police.

# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob_house(nums):
            dp = [0,0,0]
            for i, num in enumerate(nums):
                if i == 0:
                    dp[0] = nums[0]
                elif i == 1:
                    dp[1] = max(nums[0], nums[1])
                else:
                    dp[i%3] = max(num + dp[(i-2)%3], dp[(i-1)%3])
            return dp[i%3]

        if len(nums) <= 3:
            return max([0] + nums)
        return max(nums[0]+rob_house(nums[2:-1]), rob_house(nums[1:]))

if __name__ == '__main__':
    sol = Solution()
    print sol.rob([1,2,3,4,5,3,2])