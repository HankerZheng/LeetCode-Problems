# Remove all elements from a linked list of integers that have value val.

# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyNode = ListNode("dummy")
        dummyNode.next = head
        currentNode = dummyNode
        while currentNode.next:
            if currentNode.next.val == val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return dummyNode.next
        