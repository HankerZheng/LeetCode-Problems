"""
Given a binary tree containing digits from 0-9 only,
each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

Subscribe to see which companies asked this question
"""

# Key Points: Recursion.
#
# Run time: 68 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        Recursion from bottom to top(leaves to root).
        That is, current status is based on subtree's status.
        """
        def subtreeNumGenerator(root):
            if not root.left and not root.right:
                yield str(root.val)
            if root.left:
                # get result from sub-problem first
                for num in subtreeNumGenerator(root.left):
                    # then update the current status
                    yield str(root.val)+str(num)
            if root.right:
                for num in subtreeNumGenerator(root.right):
                    yield str(root.val)+str(num)

        if not root:
            return 0
        res = reduce(lambda x,y: int(x)+int(y), subtreeNumGenerator(root))
        return int(res)


    def BetterSumNumbers(self, root):
        """
        Recursion from top to bottom.
        That is, update status information before access to sub-result.
        """
        def subsum(sum, root):
            """
            When root's parents represents sum,
            return the sum of tree root.

            SUM  - store the information of root's parents.
            ROOT - the tree has not been traversed.
            Return the SumNumbers of root with root's parents info in sum
            """
            if not root:
                return 0
            # update status first
            sum = sum*10 + root.val
            if not root.left and not root.right:
                return sum
            # then get result from sub-problem
            return subsum(sum, root.left) + subsum(sum, root.right)

        if not root:
            return 0
        return subsum(0,root)