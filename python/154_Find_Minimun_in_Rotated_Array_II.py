# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# The array may contain duplicates.

# Example:
# 0001 1 2233 (1)
# 0011 2 2330 (2.a)
# 0112 2 3300 (2.a)
# 1122 3 3000 (3)
# 1223 3 0001 (2.a)
# 2233 0 0011 (3)
# 2330 0 0112 (2.c)
# 3300 0 1122 (3)
# 3000 1 1223 (2.c)
# 
# Run time: 56 ms

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return float('inf')
        if len(nums)==1:
            return nums[0]
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start+(end-start)/2
            if nums[start]<nums[end]: #(1)
                return nums[start]
            elif nums[start]==nums[end]: #(2)
                if nums[mid]>nums[start]: #(2.a)
                    start = mid+1
                elif nums[mid]==nums[start]: #(2.b)
                    return min(nums[mid],self.findMin(nums[start:mid]),self.findMin(nums[mid:end]))
                else: #(2.c)
                    end = mid
            else: #(3)
                if nums[mid]>=nums[start]:
                    start = mid+1
                elif nums[mid]<=nums[end]:
                    end = mid
        return nums[end]