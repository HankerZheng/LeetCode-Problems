# Given a binary tree, return the preorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Runtime: 40/56ms
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            this_node = stack.pop(-1)
            res.append(this_node.val)
            if this_node.right:
                stack.append(this_node.right)
            if this_node.left:
                stack.append(this_node.left)
        return res

    def preorderTraversal_Recursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traversal(node):
            if node is None:
                return
            res.append(node.val)
            traversal(node.left)
            traversal(node.right)
        res = []
        traversal(root)
        return res