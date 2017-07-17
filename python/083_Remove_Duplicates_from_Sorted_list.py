"""
Given a sorted linked list, delete all duplicates such that each element 
appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Subscribe to see which companies asked this question
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#   Key Points: Store the previous pointer and current pointer.
#               Delete the node with same value as its predecessor.
#               For this problem, no need to set dummy.
#   Run time: 65 ms
#


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        prev, cur, thisval = head, head.next, head.val
        while cur:
            if cur.val == thisval:
                # deletion
                prev.next = cur.next
                cur = prev.next
            else:
                # update
                thisval = cur.val
                cur = cur.next
                prev = prev.next
        return head