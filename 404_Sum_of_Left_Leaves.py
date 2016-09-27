# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
# Subscribe to see which companies asked this question


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        stack = [root.left, root.right]
        res = 0
        while stack:
            left_child = stack.pop(0)
            right_child = stack.pop(0)
            if left_child and left_child.left is None and left_child.right is None:
                res += left_child.val
            if left_child:
                stack.append(left_child.left)
                stack.append(left_child.right)
            if right_child:
                stack.append(right_child.left)
                stack.append(right_child.right)
        return res

    def sumOfLeftLeaves_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if node is None:
                return 0
            res = 0
            if node.left is not None and node.left.left is None and node.left.right is None:
                res += node.left.val
            return res + helper(node.left) + helper(node.right)

        return helper(root)


