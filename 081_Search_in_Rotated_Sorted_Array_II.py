# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# Would this affect the run-time complexity? How and why?
# Write a function to determine if a given target is in the array.

# Key Points: The rotate point must between a>=b
# Run time: 56 ms
# 
# 

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start+(end-start)/2
            if nums[mid]==target:
                return True
            if nums[start]==nums[mid] and nums[mid]==nums[end]:
                return self.search(nums[start+1:mid], target) or self.search(nums[mid+1:end],target)
            if target<nums[mid]:
                if target>=nums[start]:
                    end = mid -1
                elif nums[start]>nums[mid]:
                    end = mid -1
                else:
                    start = mid+1
            else:# nums[mid]<target
                if target<=nums[end]:
                    start = mid+1
                elif nums[mid] > nums[end]:
                    start = mid+1
                else:
                    end = mid-1

        return False