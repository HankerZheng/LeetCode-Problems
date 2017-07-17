"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Subscribe to see which companies asked this question"""

#
# Key Points: Recursion.
#             Get the item in the middle of the list.
#             Then the left subtree consists of all the elements before the middle,
#             while the right subtree consists of all the ...... after ...
#
# Run time: 100 ms
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def buildSubtree(n_s, n_e):
            if n_s == n_e:
                return None
            middle_index = (n_s + n_e - 1) / 2
            subroot = TreeNode(nums[middle_index])
            subroot.left = buildSubtree(n_s, middle_index)
            subroot.right = buildSubtree(middle_index+1, n_e)
            return subroot

        if not nums:
            return None
        return buildSubtree(0, len(nums))