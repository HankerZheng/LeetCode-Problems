"""
Given a binary tree, find the lowest common ancestor (LCA) of
two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest
common ancestor is defined between two nodes v and w as the lowest
node in T that has both v and w as descendants (where we allow a node
to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Subscribe to see which companies asked this question
"""
#
# Key Points: the lowest comman ancestor is the node that have
#             p and q in different subtrees. Or p or q is this node.
#             
# Run time: 96 ms
#
# ANOTHER SOLUTION: https://leetcode.com/discuss/88812/120ms-python-tricky-solution
#
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    p_dict = {}
    q_dict = {}
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def pInTree(root):
            if not root:
                return False

            if root == p:
                self.p_dict.update({root:True})
                return True
            else:
                res = pInTree(root.left) or pInTree(root.right)
                self.p_dict.update({root:res})
                return res

        def qInTree(root):            
            if not root:
                return False

            if root == q:
                self.q_dict.update({root:True})
                return True
            else:
                res = qInTree(root.left) or qInTree(root.right)
                self.q_dict.update({root:res})
                return res

        # optimized for Leetcode testcase!!
        if pInTree(q):
            return q
        if qInTree(p):
            return p

        this_node = root
        while this_node:
            if not this_node or this_node in (q,p):
                return this_node


            pl = self.p_dict.get(this_node.left, None)
            ql = self.q_dict.get(this_node.left, None)
            if pl is None:
                pl = pInTree(this_node.left)
            if ql is None:
                ql = qInTree(this_node.left)
            if pl ^ ql:
                # in different subtree
                return this_node
            elif pl:
                # both in left subtree
                this_node = this_node.left
            else:
                # both in right subtree
                this_node = this_node.right

