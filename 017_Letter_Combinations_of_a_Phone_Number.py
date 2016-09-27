'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution(object):
	# by using [a+b for a in list1 for b in list c]
	# this sol takes 40 ms
	def letterCombinations_just_create(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		dic, res = {'0':' ', '1':'*', '2':'abc', '3':'def', '4':'ghi','5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'} , []
		for x in digits:
		    res = [pre + c for c in dic[x] for pre in res or ['']]
		return res 

	# implemented through FIFO, from collections import deque -- popleft and append
	# the type would be deque, it should be converted to list
	# this sol takes 42 ms
	def letterCombinations_FIFO(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		from collections import deque
		if len(digits) == 0:
			return []
		letter_dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno' ,'7':'pqrs','8':'tuv', '9':'wxyz'}
		ans = deque()
		ans.append('')
		for i in xrange(len(digits)):
			old = ans.popleft()
			print len(old)
			while len(old) == i:
				for letter in letter_dic[digits[i]]:
					ans.append(old+letter)
				old = ans.popleft()
			ans.append(old)
		return list(ans)


	# create 2 lists
	# pop form first list and add letter and append them on the next list
	# time complexity is sigma{0,n, 3^n} 
	# this sol takes 52 ms
	def letterCombinations_original(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if len(digits) == 0:
			return []
		letter_dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno' ,'7':'pqrs','8':'tuv', '9':'wxyz'}
		ans = [[],[]]
		for i, digit in enumerate(digits):
			if i == 0:
				for letter in letter_dic[digit]:
					ans[0].append(letter)
				continue
			while len(ans[(1+i)%2]):
				word = ans[(1+i)%2].pop()
				for letter in letter_dic[digit]:
					ans[i%2].append(word+letter)
		return ans[0] if len(ans[0]) else ans[1]



sol = Solution()
print sol.letterCombinations_FIFO('452')
