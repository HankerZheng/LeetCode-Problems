'''
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
'''
#
# Key Points: Recursion.
#             If a tree is symmetric, its left subtree and right subtree
#             are also symmetric.
#
# Run time: 60 ms
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symmetric(left, right):
            if not left and not right:
                return True
            elif not left:
                return False
            elif not right:
                return False

            return left.val == right.val and\
                  symmetric(left.left, right.right) and\
                  symmetric(left.right, right.left)
        if not root:
            return True
        return symmetric(root.left, root.right)