"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.

Subscribe to see which companies asked this question
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#   Key Points: In while loop, find m-th elements in linked list.
#               Start reverse the linked list until count to n.
#   Run time: 52 ms
#

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or m == n:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, head
        for counter in xrange(n+1):
            if counter < m-1: # counter = 0 : m-2
                prev = prev.next
                cur = cur.next
            elif counter == m-1:
                # start reverse:
                start_element = prev
                end_element = cur
                cur = cur.next
                prev = prev.next
            else:
                # loop reverse
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
        # end reverse
        end_element.next = cur
        start_element.next = prev

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
    final = res.reverseBetween(head,1,3)
    final.display_list()