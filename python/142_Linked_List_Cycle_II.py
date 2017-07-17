# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?

# Subscribe to see which companies asked this question

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return None
        slow = head.next
        if slow is None:
            return None
        fast = head.next.next
        while slow and fast:
            if slow == fast:
                break
            slow = slow.next
            if fast.next is None:
                return None
            fast = fast.next.next
        m1 = slow
        slow = head
        while slow and fast:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next