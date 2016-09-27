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
#
#   Key Points: Store the previous node and current node.
#               In while loop, move current pointer to the next
#               until current val is not equal to its predecessor.
#               Delete one node when cur.val == cur.next.val.
#               End loop when cur is None or cur.next is None.
#               If u want to delete a node from the linked list,
#               make sure you keep previous node in memory.
#
#   Run time: 68 ms

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, head
        while cur and cur.next:
            if cur.val == cur.next.val:
                # deletion done by while
                tmp = cur
                while tmp and tmp.val == cur.val:
                    tmp = tmp.next
                prev.next = tmp
                cur = tmp
            else:
                # update
                prev = prev.next
                cur = cur.next
        if cur is None:
            prev.next = cur
        return dummy.next

