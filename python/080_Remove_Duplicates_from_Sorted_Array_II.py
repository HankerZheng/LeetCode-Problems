# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with
# the first five elements of nums being 1, 1, 2, 2 and 3.
# It doesn't matter what you leave beyond the new length.

# Subscribe to see which companies asked this question

# Runtime: 96ms
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        if not nums:
            return -1
        ordered=0
        check = 1
        count = 0
        while check<len(nums):
            if nums[check] == nums[ordered]:
                if count == 1:
                    check+=1
                else:
                    swap(check, ordered+1)
                    check+=1
                    ordered+=1
                    count += 1
            else:
                swap(check, ordered+1)
                check+=1
                ordered+=1
                count = 0
        return ordered+1

if __name__ == '__main__':
    sol = Solution()
    # nums = [1,1,1,2]
    # print sol.removeDuplicates(nums)
    # print nums
    # nums = [1,1,1,2,2,3]
    # print sol.removeDuplicates(nums)
    # print nums
    # nums = [1]
    # print sol.removeDuplicates(nums)
    # print nums
    # nums = []
    # print sol.removeDuplicates(nums)
    # print nums
    nums = [1,1,1,2,2,2,3,3]
    print sol.removeDuplicates(nums)
    print nums

