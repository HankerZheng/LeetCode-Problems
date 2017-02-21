"""Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

Subscribe to see which companies asked this question

Show Tags
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode("dummy")
        dummy.next = head
        currentNode = dummy
        while currentNode:
            tmpNode = currentNode.next
            # if next 2 nodes are equal, skip all nodes with the same value
            while tmpNode and tmpNode.next and tmpNode.val == tmpNode.next.val:
                removeVal = tmpNode.val
                while tmpNode and tmpNode.val == removeVal:
                    tmpNode = tmpNode.next
            currentNode.next = tmpNode
            currentNode = tmpNode
        return dummy.next
                
            