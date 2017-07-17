"""
Given a linked list and a value x, partition it such that all nodes 
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each 
of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

Subscribe to see which companies asked this question
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#   Key Points: All we need to do is to keep update 2 linked lists,
#               LS linked list and GE linked list.
#               Traverse the linked list and rearrange them into these
#               two linked list.
#   Run time: 56 ms
#

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head

        terverse, ls, ge = head, ListNode(-1), ListNode(-1)
        ls_tmp, ge_tmp = ls, ge
        while terverse:
            if terverse.val < x:
                ls_tmp.next = terverse
                ls_tmp = ls_tmp.next
            else:
                ge_tmp.next = terverse
                ge_tmp = ge_tmp.next
            terverse = terverse.next
        # make them together
        ls_tmp.next, ge_tmp.next =ge.next, None
        return ls.next
