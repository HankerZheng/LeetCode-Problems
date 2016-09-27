'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Subscribe to see which companies asked this question
'''


class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		dict_ind = {"(":0, ")":0,  '[':1, ']':1,  '{':2, '}':2}
		dict_dir = {"(":1, ")":-1, '[':1, ']':-1, '{':1, '}':-1}
		list_paren = []
		if dict_dir[s[0]] == -1:
			return False
		for char in s:
			if dict_dir[char] == 1:
				list_paren.append(dict_ind[char])
			else:
				if len(list_paren) == 0:
					return False
				elif list_paren.pop() != dict_ind[char]:
					return False


		return False if len(list_paren) else True