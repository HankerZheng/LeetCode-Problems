"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence
of nodes from some starting node to any node in the
tree along the parent-child connections. The path does not
need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

Subscribe to see which companies asked this question

Show Tags
Show Similar Problems
"""

#
# Key Points: For each node in the tree, there are two choices.
#             In the path or not in the path.
#             If this node is not in the path, the max path sum should
#             be the max of the maxsum of its two subtree
#             If this node is in the path, the max path sum should be
#             left node in path or right node in path or both in path.
#
# TLE Problem: The original solution can solve the problem correctly but
#              takes unacceptable time. Since the return value of root_in
#              function is only dependent on the input root. Once it returns
#              a value, store the value into a dict to aviod repeated calculations.
#
# Run time: 368 ms
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    root_in_dict = {}
    root_not_in_dict = {}
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def root_in(root):
            """
            return the max path sum starts from root
            the path here is defined as unidirectional parent-child path
            """
            if not root:
                return 0
            # whether the ans is in the dict
            res = self.root_in_dict.get(root,None)
            if res is None:
            # if the ans is not in the dict
                # calculate the ans
                res = root.val + max(root_in(root.left), root_in(root.right), 0)
                # update ans dict
                self.root_in_dict.update({root: res})
            return res

        # handle special case
        if not root:
            return 0
        # whether the ans is in the dict
        res = self.root_not_in_dict.get(root,None)

        if res is None:
        # if the ans is not in the dict
            # if root is in this path
            # the path could be from root one way down(left or right child)
            # or from root two ways down(both left and right children)
            value_root_in = root.val + \
                max(0,
                    root_in(root.left), 
                    root_in(root.right),
                    root_in(root.left)+root_in(root.right))
            # if root is not in this path
            # the max path shoud be in either of root's subtree
            value_root_not_in = value_root_in - 1
            if root.left:
                value_root_not_in = max(value_root_not_in, self.maxPathSum(root.left))
            if root.right:
                value_root_not_in = max(value_root_not_in, self.maxPathSum(root.right))
            res = max(value_root_in, value_root_not_in)
            self.root_not_in_dict.update({root:res})
        return res