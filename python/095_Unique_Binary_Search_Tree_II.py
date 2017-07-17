"""
Given n, generate all structurally unique TreeNode's (binary search trees) that
store values 1...n.

For example,
Given n = 3, your program should return all 5 unique TreeNode's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Key Points: Same way as Leetcode096, Dynamic Programming
#             For each root, generte its subtree based on previous ans
#
# Run Time: 108 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateSubtrees(in_list):
            """
            use the items in in_list to form subtrees
            """
            length = len(in_list)
            if length == 0:
                yield None
                return
            elif length == 1:
                yield TreeNode(in_list[0])
                return
            for item in in_list:
                for leftsubtree in generateSubtrees(range(in_list[0],item)):
                    for rightsubtree in generateSubtrees(range(item+1, in_list[0]+length)):
                        this_ans = TreeNode(item)
                        this_ans.left = leftsubtree
                        this_ans.right = rightsubtree
                        yield this_ans
            return

        if n == 0:
            return []
        ans = list()
        for tree in generateSubtrees(range(1,n+1)):
            ans.append(tree)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.generateTrees(4)