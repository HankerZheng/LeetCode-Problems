# Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

# Examples 1
# Input:

#   5
#  /  \
# 2   -3
# return [2, -3, 4], since all the values happen only once, return all of them in any order.
# Examples 2
# Input:

#   5
#  /  \
# 2   -5
# return [2], since 2 happens twice, however -5 only occur once.
# Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

# Discuss



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def getSubTreeSum(node):
            if node in history:
                return history[node]
            thisSum = node.val
            if node.left:
                thisSum += getSubTreeSum(node.left)
            if node.right:
                thisSum += getSubTreeSum(node.right)
            history[node] = thisSum
            valueCnt[thisSum] = valueCnt.get(thisSum, 0) + 1
            return thisSum

        if not root:
            return []
        history = {}
        valueCnt = {}
        ansList = []
        getSubTreeSum(root)
        maxFreqVal = max(valueCnt.values())
        for k, v in valueCnt.items():
            if v == maxFreqVal:
                ansList.append(k)
        return ansList
                