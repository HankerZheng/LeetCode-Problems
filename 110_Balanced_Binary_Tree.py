"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined
as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""

#
# Key Points: Recursion.
#             If a tree is a balanced tree, its left and right subtrees
#             must both be balanced tree and their depth can't differ
#             more than 1
#
#             Therefore, define a new function isSubtreeBalanced(root).
#             If root is balanced, return its depth, else return -1
#
# Run time: 80 ms
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSubtreeBalanced(root):
            if not root:
                return 0
            left = isSubtreeBalanced(root.left)
            right = isSubtreeBalanced(root.right)
            if left >=0 and right >= 0 and abs(left-right) <=1:
                return max(left, right) + 1
            else:
                return -1
        if isSubtreeBalanced(root) >= 0:
            return True
        return False
