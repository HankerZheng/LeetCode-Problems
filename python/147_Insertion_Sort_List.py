# Sort a linked list using insertion sort.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 384 ms

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def insert_after(node1, node2):
            # insert node2 after node1
            tmp = node1.next
            node1.next = node2
            node2.next = tmp
        if head is None:
            return None
        start, last, check = head, head, head.next
        while check:
            if check.val >= last.val:
                # move check and last one stop ahead
                last = last.next
                check = check.next
                continue
            if check.val <= start.val:
                # make check as the start
                # last doesn't change while check move one step
                tmp = check.next
                check.next = start
                last.next = tmp
                start = check
                check = tmp
                continue
            tmp, this_node = start, start.next
            while this_node:
                if this_node.val >= check.val:
                    new_check = check.next
                    insert_after(tmp, check)
                    last.next = new_check
                    break
                tmp = tmp.next
                this_node = this_node.next
            check = new_check
        return start
