'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

Subscribe to see which companies asked this question
'''


class Solution(object):
	# without stack, just use left and right
	# cuz only one kind of parenthesis, for each step, only have to keep left > right
	# this sol takes 44 ms, beating 85.31%
	def generateParenthesis(self, n):
	    def generate(p, left, right, parens=[]):
	        if left:         generate(p + '(', left-1, right)	# anytime, it is legal to add a left parenthesis
	        if right > left: generate(p + ')', left, right-1)	# if right > left, there must be a left parenthesis compatibal with right
	        if not right:    parens += p,						# ends when right is used up. lefts are always used up before rights cuz the above
	        return parens
	    return generate('', n, n)
	# with stack, sol keeps in a string manner
	# this sol takes 52 ms, beating 35%
	def generateParenthesis_string(self, n):
		paren_dic = {0:'(', 1:')'}
		def backtrack(now, stack, sol):
			if now == n*2:		ans.append(str(sol))
			else:
				for i in xrange(2):
					if used[i] > 0:
						if i == 1 and stack == 0:	continue
						used[i] -= 1
						backtrack(now+1, stack-1 if i else stack+1, sol[:now] + paren_dic[i])
						used[i] += 1
		ans, used, stack = [], [n - 1, n], 1
		backtrack(1, stack, '(')
		return ans
	# with stack, sol keeps in a list manner
	# this sol takes 54 ms
	def generateParenthesis_original(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		paren_dic = {0:'(', 1:')'}
		def backtrack(now, stack):
			if now == n*2:		ans.append(str(sol))
			else:
				for i in xrange(2):
					if used[i] > 0:
						if i == 1 and stack == 0:	continue
						sol[now] = paren_dic[i]
						used[i] -= 1
						backtrack(now+1, stack-1 if i else stack+1)
						used[i] += 1

		sol = [None for x in xrange(2*n)]
		sol[0], ans, used, stack = '(', [], [n - 1, n], 1
		backtrack(1, stack)
		return ans

if __name__ == '__main__':
	this = Solution()
	print this.generateParenthesis(6)