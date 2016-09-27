# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 372ms

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        p1, p2 = headA, headB
        length1, length2 = 1, 1

        # traverse headA
        while p1.next:
            length1 += 1
            p1 = p1.next
        while p2.next:
            length2 += 1
            p2 = p2.next
        if p1 != p2:
            # No intersection at all
            return None
        # find the common node
        delta = abs(length1 - length2)
        p1, p2 = headA, headB
        if length1 > length2:
            for i in xrange(delta):
                p1 = p1.next
        else:
            for i in xrange(delta):
                p2 = p2.next
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

