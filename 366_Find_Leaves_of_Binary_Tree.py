# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

# Example:
# Given binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Returns [4, 5, 3], [2], [1].

# Explanation:
# 1. Removing the leaves [4, 5, 3] would result in this tree:

#           1
#          / 
#         2          
# 2. Now removing the leaf [2] would result in this tree:

#           1          
# 3. Now removing the leaf [1] would result in the empty tree:

#           []         
# Returns [4, 5, 3], [2], [1].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def getHeight(node):
            if not node: return -1
            
            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            thisHeight = max(leftHeight, rightHeight) + 1
            
            if thisHeight < len(ans):
                ans[thisHeight].append(node.val)
            else:
                ans.append([])
                ans[-1].append(node.val)
            return thisHeight
        # get height of each node in the tree
        ans = []
        getHeight(root)
        return ans
        