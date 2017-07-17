"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3       0   ->
   / \
  9  20     1   <-
    /  \
   15   7   2   ->
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
Subscribe to see which companies asked this question
"""

# Key Points: Queue and keep track of current depth.
#             Get new item from the queue by pop(-1)
#             If the depth is odd number, traverse from right to left,
#                   append new node into queue from right to left
#             If the depth is even number, traverse from left to right,
#                   append new node into queue from left to right
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        depth, queue, next_queue = 0, [root], []
        res, this_level = [],[]
        while queue:
            this_node = queue.pop(-1)
            if this_node:
                this_level.append(this_node.val)
                if depth & 1:
                    next_queue.append(this_node.right)
                    next_queue.append(this_node.left)
                else:
                    next_queue.append(this_node.left)
                    next_queue.append(this_node.right)
            if not queue and this_level:
                queue, next_queue = next_queue, []
                res.append(this_level)
                this_level = []
                depth += 1

        return res


