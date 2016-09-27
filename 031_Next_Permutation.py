# Implement next permutation, which rearranges numbers
# into the lexicographically next greater permutation
# of numbers.
# 
# If such arrangement is not possible, it must rearrange
# it as the lowest possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and
# its corresponding outputs are in the right-hand column.
# 
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1
# Subscribe to see which companies asked this question

# Key Points: If the last 2 elements are in accending order,
#             just swap these 2.
#             Else, find the find the last decending slice.
#
#       For example, [..., 6, 7] -> [..., 7, 6]
#                    [..., 1, 6,4,2] -> [..., 2, 1, 4,6]
#                    [..., 3, 6,4,2] -> [..., 4,2, 3, 6]
#                    [..., 5, 6,4,2] -> [..., 6,2,4, 5 ]
#                    [..., 7, 6,4,2] -> [..., 2,4,6, 7 ]
#                    [..., 4, 6,4,2] -> [..., 6,2, 4, 4]
# https://discuss.leetcode.com/topic/52275/easy-python-solution-based-on-lexicographical-permutation-algorithm
# Run Time: 60 ms

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        if len(nums)==1:
            return
        # If last 2 is in accending order
        if nums[-1]>nums[-2]:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return

        # Find the last decending order -- nums[starter+1:]
        starter = len(nums)-2
        while starter>=0 and nums[starter]>=nums[starter+1]:
            starter -=1
        # If the whole nums is in decending order, reverse it
        if starter == -1:
            nums.reverse()
            return

        # find the least num larger than nums[starter]
        right = starter+1
        while right<len(nums) and nums[starter]<nums[right]:
            right += 1
        nums[right-1], nums[starter] = nums[starter], nums[right-1]
        # print "  %s"%nums[starter+1:]
        nums[starter+1:] = sorted(nums[starter+1:])

if __name__=="__main__":
    test = Solution()
    query = [ [1,2,3,4,5], # 1,2,3,5,4
              [5,4,3,2,1], # 1,2,3,4,5
              [1],
              [],
              [1,4,5,3,2], # 1,5,2,3,4
              [1,3,2] # 2,1,3
            ]
    for q in query:
        test.nextPermutation(q)
        print q