'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''

# Key Points: Make use of stack(FILOqueue). Put right_node, nodeval, left_node
#             into the stack respectively.
#             In the WHILE loop, we do:
#                1) Get one item from stack. If this item is a num, append
#             it to the res list. Else, it must be a TreeNode.
#                2) For every node, push right node, node.val and left node
#             into this stack repectively if they exist.
#
# Run time: 56 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import LifoQueue
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack, res = LifoQueue(), list()
        stack.put(root)
        while not stack.empty():
            this_item = stack.get()
            if isinstance(this_item, TreeNode):
                # this_item is a TreeNode
                if this_item.right:
                    stack.put(this_item.right)
                stack.put(this_item.val)
                if this_item.left:
                    stack.put(this_item.left)
            else:
                # this_item is a val of one TreeNode
                res.append(this_item)
        return res
