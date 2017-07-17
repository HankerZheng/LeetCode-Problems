"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.
"""

# Key Points: In pre-order place. Pre-order Traversal.
#
# Run time: 68 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def preorder_traversal(root):
            if not root:
                return []
            return [root] + preorder_traversal(root.left) + preorder_traversal(root.right)

        if not root:
            return root
        preorder = preorder_traversal(root)
        if len(preorder) == 1:
            return

        parent = root
        parent.left = None
        for node in preorder[1:]:
            parent.right = node
            node.left = None
            parent = node
        node.right = None
