# Suppose a sorted array is rotated at some pivot
# unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in
# the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.

# Only these three possibility
# 1 3 5 - Accending, none-rorate
# 1 5 3 - Impossible
# 3 1 5 - Impossible
# 3 5 1 - rotated point between 5 and 1
# 5 1 3 - rotated poing between 5 and 1
# 5 3 1 - Impossible
#
# Key Points: Binary Search
#             Consider carefully for the loop-end condition
# Run Time: 52ms

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while right-left>1:
            mid = (left+right)/2
            if nums[left]<=nums[mid] and nums[mid]<=nums[right]:
                if target == nums[right]:
                    return right
                if target < nums[mid]:
                    right = mid
                elif target > nums[mid]:
                    left = mid
                else:
                    return mid
            elif nums[left]<=nums[mid] and nums[mid]>=nums[right]:
                if target <= nums[mid] and target >= nums[left]:
                    right = mid
                else:
                    left = mid
            elif nums[left]>=nums[mid] and nums[mid]<=nums[right]:
                if target <= nums[right] and target >= nums[mid]:
                    left = mid
                else:
                    right = mid
        return left if target==nums[left] else right if target==nums[right] else -1

if __name__=="__main__":
    test = Solution()
    query = [
        ([1,2,3,4,5,6,7], 0), # -1
        ([1,2,3,4,5,6,7], 1), # 0
        ([1,2,3,4,5,6,7], 7), # 6
        ([1,2,3,4,5,6,7], 4), # 3
        ([5,6,7,1,2,3,4], 4), # 6
        ([3,4,5,6,7,1,2], 4), # 1
        ([1], 1), # 0
        ([1,3], 1), # 0
        ([1,3], 3), # 1
        ([1,3], 2), # -1
    ]
    for q in query:
        ans = test.search(q[0],q[1])
        print ans