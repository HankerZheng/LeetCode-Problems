# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Examples:

# Given binary tree [3,9,20,null,null,15,7],
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
# return its vertical order traversal as:
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Given binary tree [3,9,8,4,0,1,7],
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
# return its vertical order traversal as:
# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
# return its vertical order traversal as:
# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]
# Show Company Tags
# Show Tags
# Show Similar Problems


import collections

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def bfs(node):
            baseIdx = 0
            queue = [(node, 0)]
            while queue:
                thisNode, currentPos = queue.pop(0)
                thisIdx = currentPos + baseIdx
                if thisIdx < 0:
                    baseIdx += 1
                    ans.appendleft([thisNode.val])
                elif thisIdx >= len(ans):
                    ans.append([thisNode.val])
                else:
                    ans[thisIdx].append(thisNode.val)
                if thisNode.left:
                    queue.append((thisNode.left, currentPos-1))
                if thisNode.right:
                    queue.append((thisNode.right, currentPos+1))
            
        
        if not root:
            return []
        ans = collections.deque()
        bfs(root)
        return ans