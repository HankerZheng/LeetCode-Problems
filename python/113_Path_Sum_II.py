"""
Given a binary tree and a sum, find all root-to-leaf paths
where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
Subscribe to see which companies asked this question
"""

#
# Key Points: Generator. Yield all possible paths.
#             Generator return a list.
#
# Run time: 84 ms


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def pathGenerator(root, sum):            
            next_sum = sum - root.val
            if not root.left and not root.right:
                if root.val == sum:
                    yield [root.val]

            if root.left:
                for ans in pathGenerator(root.left, next_sum):
                    yield [root.val] + ans
            if root.right:
                for ans in pathGenerator(root.right, next_sum):
                    yield [root.val] + ans

        if not root:
            return []
        res = []
        for path in pathGenerator(root, sum):
            res.append(path)
        return res