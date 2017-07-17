# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# Example 1:
#      3
#     / \
#    2   3
#     \   \ 
#      3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1
# Maximum amount of money the thief can rob = 4 + 5 = 9.
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def no_rob(node):
            # the max value we could get if we don't rob this node
            if node in hashtable:
                return hashtable[node]
            if node is None:
                return 0

            # if we don't rob node, we could rob its children
            rob_left = rob_right = rob_both = rob_neither = 0
            rob_neither = no_rob(node.left) + no_rob(node.right)
            if node.left:
                rob_left = node.left.val + no_rob(node.left.left) + no_rob(node.left.right) + no_rob(node.right)
            if node.right:
                rob_right = node.right.val + no_rob(node.right.left) + no_rob(node.right.right) + no_rob(node.left)
            if node.right and node.left:
                rob_both = node.right.val + node.left.val + no_rob(node.left.left) + no_rob(node.left.right) + no_rob(node.right.left) + no_rob(node.right.right)

            hashtable[node] = max(rob_left, rob_right, rob_neither, rob_both)
            return hashtable[node]

        if root is None:
            return 0
        hashtable = {}
        return max(root.val + no_rob(root.left) + no_rob(root.right), no_rob(root))

    def rob_simple(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob_node(node, prev):
            if node is None:
                return 0
            if prev is True:
                return rob_node(node.right, prev=False) + rob_node(node.left, prev=False)
            else:
                if node in hashtable:
                    return hashtable[node]
                hashtable[node] = max(node.val+rob_node(node.left, True)+rob_node(node.right, True), rob_node(node.left, False)+rob_node(node.right, False))
                return hashtable[node]
        if root is None:
            return 0
        # store the max value we could get on Tree node
        hashtable = {}
        return rob_node(root, prev=False)