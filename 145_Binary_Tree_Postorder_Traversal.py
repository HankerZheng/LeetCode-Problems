"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

Subscribe to see which companies asked this question

Show Tags
Show Similar Problems
"""

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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue, res = [root], []
        while queue:
            this_node = queue.pop(0)
            if isinstance(this_node, TreeNode):                
                queue.append(this_node.val)
                if this_node.right:
                    queue.append(this_node.right)
                if this_node.left:
                    queue.append(this_node.left)
            else:
                res.append(this_node)
        return res
