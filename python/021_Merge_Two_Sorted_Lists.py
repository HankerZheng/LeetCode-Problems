'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Subscribe to see which companies asked this question
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	#this sol takes 52 ms, beating 78.83%
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if l1 == None:
			return l2
		if l2 == None:
			return l1

		ans, insert_point, temp = l1, l1, l2
		if temp.val < insert_point.val:
			mark = temp
			while temp.next != None and temp.next.val < insert_point.val:
				temp = temp.next
			ans, temp.next, temp  = mark, l1, temp.next

		old_point, insert_point = insert_point, insert_point.next
		while insert_point!=None and temp != None:
			if temp.val < insert_point.val:
				mark = temp
				while temp.next != None and temp.next.val < insert_point.val:
					temp = temp.next
				old_point.next, temp.next, temp  = mark, insert_point, temp.next
			old_point, insert_point = insert_point, insert_point.next
		if temp != None:
			old_point.next = temp
		return ans
