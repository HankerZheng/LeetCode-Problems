# Given a collection of numbers that might contain duplicates,
# return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
# Subscribe to see which companies asked this question


# Runtime: 152ms
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, length, used, ans):
            if length == len(nums):
                res.append(ans)
                return
            this_used = {num: 0 for num in nums}
            for i, num in enumerate(nums):
                if used[i] == 0 and this_used[num]==0:
                    this_used[num]=1
                    used[i] = 1
                    helper(nums, length+1, used, ans+[num])
                    used[i] = 0


        res = []
        used = {i:0 for i, _ in enumerate(nums)}
        helper(nums, 0, used, [])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.permuteUnique([1,2])