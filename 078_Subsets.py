# Given a set of distinct integers, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# Runtime: 68ms

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(ans, state):
            if state == len(nums):
                res.append(ans)
                return
            helper(ans+[nums[state]], state+1)
            helper(ans, state+1)
        res = []
        helper([], 0)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.subsets([1,2,3])