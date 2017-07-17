# Given a sorted array and a target value, return the index
# if the target is found. If not, return the index where it
# would be if it were inserted in order.

# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

# Key Points: Binary Search
# Run time: 52 ms

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start + (end-start)/2
            if nums[mid] > target:
                end = mid -1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        # if nums[start]<target and nums[end]>target and start+1=end
        # then mid would be equal to start
        # then start would be assigned to end
        # then both nums[start] and nums[end] are larger target
        # then end would be assigned to start - 1
        # Therefore, when jump out of loop, 
        # it would be -- nums[start]>target
        #                nums[end]<target
        return start