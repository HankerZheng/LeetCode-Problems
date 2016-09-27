"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
"""
# Key Points: Same as 099_Validate_BST.
#             First, inorder traversal the BST and find the only 2 wrong nodes.
#             Then, swap these 2 nodes.
#             In my implementation, I only swap the value. How to swap the node?
#
# Run time: 160 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def inorder_traversal(root):
            if root.left:
                for node in inorder_traversal(root.left):
                    yield node
            yield root
            if root.right:
                for node in inorder_traversal(root.right):
                    yield node
        generator = inorder_traversal(root)
        prev = generator.next()
        wrong_nodes = list()
        for i in xrange(2):
            for node in generator:
                if node.val <= prev.val:
                    wrong_nodes.append(prev)
                    wrong_nodes.append(node)
                    prev = node
                    break
                prev = node
        length = len(wrong_nodes)
        wrong_nodes[0].val, wrong_nodes[length-1].val = \
                wrong_nodes[length-1].val, wrong_nodes[0].val
        return