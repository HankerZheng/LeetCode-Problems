'''Given a list, rotate the list to the right by k places, 
where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

Subscribe to see which companies asked this question

Show Tags
Show Similar Problems
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Key Point: The key point to solve this problem is to
#            find a way to get the first element after
#            rotating. If found, things left to be done
#            are only to rearrange the pointer.
#            In order to find the first element after
#            rotating, we could first set two pointer, 
#            pointing two different elements with k-1 
#            elements in between. Then move both pointer
#            until the last one hit the boundary. Then, 
#            the element that the first pointer points is
#            the element we want to find.
# Run time: 64 ms

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 1:
            return head
        if head is None or head.next is None:
            return head
        # set dummy pointer
        dummy = ListNode(-1)
        dummy.next = head
        left = right = dummy
        length = 0
        # set the right pointer
        for x in xrange(k):
            right = right.next
            if right.next is None:
                length = x+1
                right = dummy
                break
        if length:
            right = dummy
            for x in xrange(k%length):
                right = right.next
        # boundary condition
        if right == left:
            return head
        # swap the pointer
        while right.next:
            left = left.next
            right = right.next
        # set boundary
        start = left.next
        left.next = right.next
        right.next = head
        dummy.next = start
        return dummy.next
