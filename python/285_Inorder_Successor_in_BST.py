# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

# Note: If the given node has no in-order successor in the tree, return null.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # early termination
        # if p has right subtree, return the left most of that tree
        if p.right:
            thisNode = p.right
            while thisNode.left:
                thisNode = thisNode.left
            return thisNode

        # Now, p has no right subtree
        # init the potential ans to None
        potential = None
        thisNode = root
        while thisNode:
            if thisNode.val < p.val:
                # p must in the right subtree of thisNode
                # then thisNode can't be its successor
                thisNode = thisNode.right
            elif thisNode.val == p.val:
                # find the target node, ans is the potential ans
                return potential
            else:
                # p must in the left subtree of thisNode
                # thisNode could be the potential ans
                # continue to traverse thisNode's left subtree
                potential = thisNode
                thisNode = thisNode.left
        # target node does not exist in the tree
        return None
            
