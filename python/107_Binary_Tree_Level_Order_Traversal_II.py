"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
#
# Key Points: Same as 102. Return the 102 result.reverse()
#
# Run time: 64 ms
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue, count = [root], 1
        res, this_level = [],[]
        while len(queue):
            this_node = queue.pop(0)
            if this_node:
                this_level.append(this_node.val)
                queue.append(this_node.left)
                queue.append(this_node.right)
            count -= 1
            if count == 0 and this_level:
                res.append(this_level)
                count = len(queue)
                this_level = []
        res.reverse()
        return res