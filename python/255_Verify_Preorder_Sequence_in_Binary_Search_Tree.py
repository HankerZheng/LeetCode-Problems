# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

# You may assume each number in the sequence is unique.

# Follow up:
# Could you do it using only constant space complexity?

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        minValue = float("-inf")
        for num in preorder:
            if num <= minValue:
                return False
            while stack and stack[-1] < num:
                minValue = stack.pop(-1)
            stack.append(num)
        return True
