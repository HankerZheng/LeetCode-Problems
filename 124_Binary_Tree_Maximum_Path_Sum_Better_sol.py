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
# Key Points: Recursion.
#             Each path must start from one node in the tree
#             and end at one node in the tree.
#             For each node, it could be the start node or not.
#             subpath(root) function returns the max path sum that
#             start from the node `root`.
#
# Run time: 156 ms
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = float("-inf")
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxSubpathSum(root):
            """
            Return the max path sum which starts from the root node.
            This path could be  1) only this node.
                                2) with left or right subtree.
            This function returns the path with only one or no child.
            However, update res with the path that could have 2 children

            In this function, we do two different things.
                1) recursively calculate the max uni-directional path sum
                2) update maxPathSum in self.ans
            """
            if not root:
                return 0
            # left and right subpath
            left = maxSubpathSum(root.left)
            right = maxSubpathSum(root.right)
            # update maxPathSum
            this_ans = root.val + max(left, right, left+right, 0)
            self.ans = max(this_ans, self.ans)
            # return max uni-directional path sum
            return root.val + max(left, right, 0)

        if not root:
            return 0
        maxSubpathSum(root)
        return self.ans