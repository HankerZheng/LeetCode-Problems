# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

# Note:
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def getNextNode(root, p):
            if p.right:
                thisNode = p.right
                while thisNode.left:
                    thisNode = thisNode.left
                return thisNode
    
            # Now, p has no right subtree
            potential = None
            thisNode = root
            while thisNode:
                if thisNode.val < p.val:
                    thisNode = thisNode.right
                elif thisNode.val > p.val:
                    potential = thisNode
                    thisNode = thisNode.left
                else:
                    break
            return potential
        
        
        def getPrevNode(root, p):
            if p.left:
                thisNode = p.left
                while thisNode.right:
                    thisNode = thisNode.right
                return thisNode
    
            # Now, p has no left subtree
            potential = None
            thisNode = root
            while thisNode:
                if thisNode.val > p.val:
                    thisNode = thisNode.left
                elif thisNode.val < p.val:
                    potential = thisNode
                    thisNode = thisNode.right
                else:
                    break
            return potential

        visited = set()
        heap = []
        thisNode = root
        while thisNode:
            visited.add(thisNode)
            heapq.heappush(heap, (abs(thisNode.val - target), thisNode))
            if thisNode.val < target:
                thisNode = thisNode.right
            elif thisNode.val > target:
                thisNode = thisNode.left
            else:
                break
        ans = []
        while len(ans) != k:
            dist, thisNode = heapq.heappop(heap)
            ans.append(thisNode.val)
            nextNode = getNextNode(root, thisNode)
            prevNode = getPrevNode(root, thisNode)
            if nextNode and nextNode not in visited:
                visited.add(nextNode)
                heapq.heappush(heap, (abs(nextNode.val - target), nextNode))
            if prevNode and prevNode not in visited:
                visited.add(prevNode)
                heapq.heappush(heap, (abs(prevNode.val - target), prevNode))
        return ans