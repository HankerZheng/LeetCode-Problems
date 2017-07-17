"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical
and the nodes have the same value.
"""

# Key Points: 
#
# Run time: 52 ms
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def compare_subtree(p,q):
            if not p and not q:
                return True
            elif not p:
                return False
            elif not q:
                return False

            return p.val == q.val and \
                  compare_subtree(p.left, q.left) and \
                  compare_subtree(p.right, q.right)

        return compare_subtree(p,q)