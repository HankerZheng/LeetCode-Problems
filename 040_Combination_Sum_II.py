# Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

# Key Points: Backtracing
# 
# Runtime: 96 ms

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(candidates, target, comb, used, last):
            if target == 0:
                res.append(comb)
            else:
                # If there is a repeated number k,
                # shouldn't use k if the earlier k is not used.
                for i in xrange(last+1, len(candidates)):
                    if candidates[i] <= target:
                        if i>=1 and candidates[i] == candidates[i-1] and used[i-1]==0:
                            continue
                        else:
                            used[i] = 1
                            helper(candidates, target-candidates[i], comb+[candidates[i]], used, i)
                            used[i] = 0
        res, used = [], [0 for i in candidates]
        candidates.sort()
        helper(candidates, target, [], used, -1)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum2([10, 1, 2, 7, 6, 1, 5] ,8)