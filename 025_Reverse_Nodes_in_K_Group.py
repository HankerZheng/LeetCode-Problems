"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Subscribe to see which companies asked this question
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Key Point: How to reverse linked list
#            Be careful while considering boundary condition
# Run time: 72ms
#

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(start, end):
            # reverse from start.next to end.next inclusivly
            # return the last element reversed as the next head
            if end.next is None:
                return None
            last = prev = start.next
            this = prev.next
            while prev != end:
                this.next, prev, this = prev, this, this.next
            start.next, this.next, last.next = this, prev, this.next
            return last

        if k < 2:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        start = end = dummy
        while start and start.next:
            for i in xrange(k-1):
                if end.next:
                    end = end.next
                else:
                    return dummy.next
            # start and end are head pointer for next round
            start = end = reverse(start, end)            

        return dummy.next



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def create_from_array(cls, array):
        res = ListNode(-1)
        res_tmp = res
        for num in array:
            res_tmp.next = ListNode(num)
            res_tmp = res_tmp.next
        return res.next

    def display_list(self):
        tmp = self
        while tmp.next is not None:
            print tmp.val, 
            tmp = tmp.next
        print tmp.val


if __name__ == "__main__":
    head = ListNode.create_from_array([1,2,3,4,5,6,7,8])
    res = Solution()
    final = res.reverseKGroup(head,5)
    final.display_list()