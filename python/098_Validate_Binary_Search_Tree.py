"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
    1) The left subtree of a node contains only nodes with keys less than
       the node's key.
    2) The right subtree of a node contains only nodes with keys greater
       than the node's key.
    3) Both the left and right subtrees must also be binary search trees.
"""

# Key Points: Inorder Traversal of given binary tree.
#             If the list get is in accendent order, it is valid BST.
#             Else, it is not.
# Run time: 108 ms
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder_traversal(root):
            if root.left:
                for value in inorder_traversal(root.left):
                    yield value
            yield root.val
            if root.right:
                for value in inorder_traversal(root.right):
                    yield value

        if not root:
            return True
        generator = inorder_traversal(root)
        prev = generator.next()
        for val in generator:
            if prev >= val:
                return False
            prev = val
        return True


if __name__ == "__main__":
    root = TreeNode(1)
    sol = Solution()
    print sol.isValidBST(root)
