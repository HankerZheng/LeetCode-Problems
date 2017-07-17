# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
# prove that at least one duplicate number must exist. 
# Assume that there is only one duplicate number, find the duplicate one.

# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        fast = nums[nums[0]]
        slow = nums[0]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast

if __name__ == '__main__':
    sol = Solution()
    print sol.findDuplicate([1,5,4,2,3,2])
    print sol.findDuplicate([1,1,1,1,1,1])