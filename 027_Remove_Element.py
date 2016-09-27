"""
Given an array and a value, remove all instances of that value in place
and return the new length.

Do not allocate extra space for another array, you must do this in place
with constant memory.

The order of elements can be changed. It doesn't matter what you leave
beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Show Hint 
"""

# Key Points: Use two pointers, one points to the end of new array,
#             the other terverses the entire array
#             If the value of the latter is equal to val, just move
#             the latter forward and keep the former still
#             Else, update the cell pointed by the former.
#
# Run time: 60 ms

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None:
            return nums

        length, current, end = len(nums), 0, 0

        while current < length:
            if nums[current] == val:
                # end of list stay still, current move forward
                current += 1
            else:
                # both pointers move forward
                nums[end] = nums[current]
                end += 1
                current += 1

        # when finishing the loop, current is equal to length
        # end is equal to the length after removed.
        return end
