
# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 92ms

class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        slow = head.next
        if head.next is None:
            return False
        fast = slow.next
        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next.next
        return False
    def hasCycle_Extra_Space(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        visited = set()
        this_link = head
        while this_link:
            if this_link in visited:
                return True
            visited.add(this_link)
            this_link = this_link.next
        return False