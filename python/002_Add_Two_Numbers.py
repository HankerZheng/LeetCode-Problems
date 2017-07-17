# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Subscribe to see which companies asked this question

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 125 ms

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = l1, l2
        carry = 0
        ans = ListNode("dummy")
        this_node = ans
        while num1 or num2 or carry:
            this_sum = 0
            if num1:
                this_sum += num1.val
                num1 = num1.next
            if num2:
                this_sum += num2.val
                num2 = num2.next
            if carry:
                this_sum += carry
            this_node.next = ListNode(this_sum%10)
            carry = this_sum >= 10
            this_node = this_node.next

        return ans.next

