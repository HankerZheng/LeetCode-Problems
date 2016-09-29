# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.

# Subscribe to see which companies asked this question

# Naive Solution: sort the array and return the first missing number
# Better Solution:
#     Since there is only n num in the arrays, then the missing number
#     must be in [1,n+1]. Thus, if num[i] belongs to [1, n], swap num[i]
#     with num[num[i]-1]. Thus, number k that belong to [1,n] would be in
#     num[k-1]. Traverse the list, if num[i] != i+1, then return i+1
#           slot i --- i+1    slot 0 --- 1

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            this_num = num
            while 0 < this_num < len(nums) and nums[this_num-1] != this_num:
                nums[this_num-1], nums[i] = nums[i], nums[this_num-1]
                this_num = nums[i]
        for i,num in enumerate(nums):
            if num != i+1:
                return i+1
        return len(nums)+1

    def firstMissingPositive_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        missing = 1
        for num in nums:
            if num == missing:
                missing += 1
            elif num > missing:
                return missing
        return missing

if __name__ == '__main__':
    sol = Solution()
    print sol.firstMissingPositive([-1,4,2,1,9,10])
    print sol.firstMissingPositive([1])