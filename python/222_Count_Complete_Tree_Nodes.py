"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Subscribe to see which companies asked this question
"""

#
# Key Points: Since it's complete Binary Tree, go left and left
#             to find the depth of the tree. DEF:[0] has depth of 1
#             Then, num of nodes is between 2**(depth-1) and 2**depth-1
#
#             Use binary search to find the first None node at last level.
#
# Run time: 192 ms
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_node(num):
            """
            Given the node's index, return the node
            """
            this_node, tmp = root, num
            for i in xrange(depth-1):
                if tmp&self.filter:
                    this_node = this_node.right
                else:
                    this_node = this_node.left
                tmp = tmp<<1
            return this_node

        # find depth
        this_node, depth = root, 0
        while this_node:
            this_node = this_node.left
            depth += 1
        # special case
        if depth == 0:
            return 0
        elif depth == 1:
            return 1
        self.filter = 1<<(depth-2)
        # leftmost represents 0, rightmost represents 11...11
        start, end = 0,1<<(depth-1)
        while abs(end-start)>1:
            index = (start+end)/2
            node = get_node(index)
            if node is None:
                end = index
            else:
                start = index

        return start+(1<<(depth-1))


    def countNodes_Better(self, root):        
        def getHeight(self, root):
            height = 0
            while root:
                height += 1
                root = root.left
            return height

        count = 0
        while root:
            l = getHeight(root.left)
            r = getHeight(root.right)
            if l == r:
                count += 2 ** l
                root = root.right
            else:
                count += 2 ** r
                root = root.left
        return count