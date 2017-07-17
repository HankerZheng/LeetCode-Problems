# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# You may assume no duplicate exists in the array.

# Key Points: Binary Search to find the pivot point
# Only these three possibility
# 1 3 5 - Accending, none-rorate
# 1 5 3 - Impossible
# 3 1 5 - Impossible
# 3 5 1 - rotated point between 5 and 1
# 5 1 3 - rotated poing between 5 and 1
# 5 3 1 - Impossible
#
# Run time: 44 ms


# FOR a rotated array of 1234567
# 2345671 -- 2 5 1
# 3456712 -- 3 6 2
# 4567123 -- 4 7 3
# 5671234 -- 5 1 4
# 6712345 -- 6 2 5
# 7123456 -- 7 3 6
# We have that nums[start]>nums[end]
# We have that nums[mid] can be between nums[start] and nums[end]

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start+(end-start)/2
            if nums[start]<nums[mid] and nums[mid]<nums[end]:
                return nums[start]
            elif nums[start]<nums[mid] and nums[mid]>nums[end]:
                start = mid+1
            elif nums[start]>nums[mid] and nums[mid]<nums[end]:
                end = mid
            else:
                return min(nums[start], nums[mid], nums[end])


        return nums[end]

