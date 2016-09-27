"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

Subscribe to see which companies asked this question
"""


#
# Key Points: Same as 105, recursion
#
# Run time: 89 ms
#           index method of list instance is O(n)
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def buildSubtree(index_dict, i_s, i_e, p_s, p_e):
            if i_s == i_e:
                return None
            subroot = TreeNode(postorder[p_e-1])
            # get the number of nodes in left subtree
            i = index_dict[postorder[p_e-1]] - i_s
            subroot.left = buildSubtree(index_dict, i_s, i_s+i, p_s, p_s+i)
            subroot.right = buildSubtree(index_dict, i_s+i+1, i_e, p_s+i, p_e-1)
            return subroot

        if not inorder:
            return None
        index_dict = {v:i for i,v in enumerate(inorder)}
        return buildSubtree(index_dict, 0, len(inorder), 0, len(postorder))