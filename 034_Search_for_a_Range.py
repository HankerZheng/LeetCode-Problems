# Given a sorted array of integers, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

# Key Points: Binary Search.
#             Find left margin first, then right
#             If left margin > right margin, return [-1,-1]
#
# Run time: 88 ms

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        while left <= right:
            # mid = (left+right)/2  may overflow!!
            # mid would always points to the one on the right
            mid = left + (right-left)/2
            if nums[mid]< target:
                left = mid+1
            else: # larger than or equal to
                right = mid-1
        # nums[left] would be target itself if exist
        # or would be the nearest num larger than target
        # or out of index range
        res_left = left

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] > target:
                right = mid-1
            else: # less than or equal to
                left = mid+1
        # nums[right] would be target itself if exist
        # or would be the nearest num less than target
        # or out of index range
        res_right = right

        if res_left > res_right:
            return [-1,-1]
        else:
            return [res_left, res_right]



if __name__=="__main__":
    test = Solution()
    query = [
        ([1,1,3,3,3,4,4,5], 1), # 0,1
        ([1,1,3,3,3,4,4,5], 2), # -1,-1
        ([1,1,3,3,3,4,4,5], 3), # 2,4
        ([1,1,3,3,3,4,4,5], 4), # 5,6
        ([1,1,3,3,3,4,4,5], 5), # 7,7
        ([1,1,3,3,3,4,4,5], 6), # -1,-1
        ([1], 1), # 0,0
        ([1], 0), # -1,-1
        ([1], 2), # -1,-1
        ([], 2), # -1,-1
    ]
    for q in query:
        ans = test.searchRange(q[0],q[1])
        print ans