# Given a set of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# [
#   [7],
#   [2, 2, 3]
# ]
# Subscribe to see which companies asked this question

# Key Points: Backtracing
# 
# Runtime: 120 ms

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(candidates, target, combination):
            if target == 0:
                res.append(combination)
            else:
                for x in candidates:
                    if x <= target and (not combination or x >= combination[-1]):
                        helper(candidates, target - x, combination+[x])
        res = []
        helper(candidates, target, [])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum([3,2,7],7)