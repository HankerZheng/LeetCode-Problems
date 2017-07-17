"""
Given a binary tree, return the level order traversal of its
nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Key Points: FIFO queue to store new node.
#
# Run time: 68 ms
#           It takes 112 ms to solve this problem by Queue.Queue
#           Queue.Queue() is to solve multi-thread custom-consume problem.
#
#           While it takes only 68 to solve through list().
#           List Implementation of queue:
#                   put  <=> list.append(item)
#                   get  <=> list.pop(0)
#           List Implementation of stack:
#                   push <=> list.append(item)
#                   pop  <=> list.pop(-1)
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue, res = [], []      
        count, this_level = 1, []
        queue.append(root)

        while queue:
            node = queue.pop(0)
            this_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            count -= 1
            if count == 0:
                count = len(queue)
                res.append(this_level)
                this_level = []
        return res

