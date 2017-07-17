"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along
the shortest path from the root node down to the nearest leaf node.
"""


#
# Key Points: Recursion.
#             Leaf node is the node without any children
#             Return the min depth of left and right subtree + 1.
#
# Run time: 76 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getMinDepth(root):
            if not root.left and not root.right:
                return 1
            elif not root.left:
                return getMinDepth(root.right) + 1
            elif not root.right:
                return getMinDepth(root.left) + 1
            else:
                return min(getMinDepth(root.right), getMinDepth(root.left)) + 1
        
        if not root:
            return 0
        return getMinDepth(root)