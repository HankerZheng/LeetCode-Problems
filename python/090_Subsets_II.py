# Given a collection of integers that might contain duplicates,
# nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

# Runtime: 72ms
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(index, ans):
            if index == len(nums):
                res.append([sort[i] for i in ans])
                return 
            helper(index+1, ans)
            if index == 0:
                helper(index+1, ans+[index])
            else:
                if sort[index]==sort[index-1] and ans and ans[-1]==index-1:
                    helper(index+1, ans+[index])
                elif sort[index]!=sort[index-1]:
                    helper(index+1, ans+[index])

        sort = sorted(nums)
        res = []
        helper(0, [])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.subsetsWithDup([1,1,2,2])
    print sol.subsetsWithDup([])
    print sol.subsetsWithDup([1,2])