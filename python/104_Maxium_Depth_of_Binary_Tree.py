"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.

Subscribe to see which companies asked this question
"""

#
# Key Points: Recursion
#
# Run time: 72 ms
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_depth(root):
            if not root.left and not root.right:
                return 1
            elif not root.left:
                return 1+find_depth(root.right)
            elif not root.right:
                return 1+find_depth(root.left)
            else:
                return 1+max(find_depth(root.left),find_depth(root.right))
        if not root:
            return 0
        return find_depth(root)