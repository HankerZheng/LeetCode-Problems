class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(used, current):
            if len(current) == len(nums):
                res.append(current)
                return
            for i in xrange(len(nums)):
                if used[i] != 1:
                    used[i] = 1
                    helper(used, current+[nums[i]])
                    used[i] = 0

        res, used = [], [0 for num in nums]
        helper(used, [])
        return res

if __name__ == '__main__':
    sol=Solution()
    print sol.permute([1,2,3])