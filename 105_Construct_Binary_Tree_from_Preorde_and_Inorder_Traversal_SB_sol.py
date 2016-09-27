"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

Subscribe to see which companies asked this question
"""
#
# Key Points: Pre-order is `this, this.left, this.right`
#              In-order is `this.left, this, this.right`
#             Therefore, the root of the tree must be the first element
#             in the Pre-order list.
#             Assume the root's value is $A
#             Then, all the elements ahead of $A in In-order list is the
#             In-order traversal of the left subtree, and vice versa.
#
#             Therefore, we could solve this problem by recursion.
#             For the first element $A in the Pre-order list, find its
#             position in the In-order list. Then, all the element ahead
#             of $A forms a new In-order list of root's left subtree while
#             all the element behind of $A forms a new In-order list of root's
#             right subtree.
#             Meanwhile, all the element of the In-order list of the root's left
#             subtree must be continueous(not seperated) in the Pre-order list,
#             otherwise, these two list won't construct a binary tree.
#             Then we got the left subtree's Pre-order list and In-order list.
#
#             Let recursion goes.
#
# MLE: Memory Limit Exceeded.
#      This is because when slice operation of the list is on the right side of
#      `=`, the interpreter would create a copy of the original list.
#      In order to solve this problem, pass the index rather the slice of the list
#      as the parameter of the recursive function.
#
#                       (i)---+ +---(i+1)
#                             ! !
#    PRE-ORDER LIST: R [ LEFT ] [ RIGHT ]
#     IN-ORDER LIST: [ LEFT ] R [ RIGHT ]
#                           ! !
#                   (i-1)---+ +---(i)
#
# Run time: 388 ms
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def getBoarder(total_s, total_e, sub_s, sub_e):
            """
            logN complexity to find the boarder
            return the index of the last in total that also belongs to leftsubtree
            """
            if sub_s == sub_e:
                return total_e-1

            start, end = total_s, total_e
            while end-start != 1:
                if preorder[(start+end)/2] in inorder[sub_s: sub_e]:
                    start = (start+end)/2
                else:
                    end = (start+end)/2
            return start

        def buildSubtree(p_s, p_e, i_s, i_e):
            """
            All the paremeters are index of the original list.
            Index p_e and i_e are not included.
            """
            if p_e - p_s == 1:
                # only one item left in the list
                return TreeNode(preorder[p_s])

            subroot = TreeNode(preorder[p_s])
            # find the position of the root node
                # if i == i_s, there is no left subtreee
                # if i == i_e-1, there is no right subtree
            i = inorder[i_s:i_e].index(preorder[p_s]) + i_s
            # find the position of the end of left subtree
            j = getBoarder(p_s+1, p_e, i_s, i) if i!=i_s else p_s
            if j != p_s:
                # there is left subtree
                subroot.left = buildSubtree(p_s+1, j+1, i_s, i)
            if i != i_e-1:
                # there is right subtree
                subroot.right = buildSubtree(j+1, p_e, i+1, i_e)
            return subroot

        if not preorder:
            return None
        return buildSubtree(0, len(preorder),0, len(inorder))