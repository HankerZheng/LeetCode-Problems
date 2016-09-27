'''
The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Subscribe to see which companies asked this question
'''

class Solution(object):
	# advanced improved by storing the cross index in a list
	# cuz the data scale is not so big, this sol is better than the second one for judgement line
	# 'in' operation's time complexity is O(n), therefore, when data scale grows, the second judgement line is better
	def solveNQueens_fastest(self, n):
		def backtrack(place, cross_plus, cross_minus):
			length = len(place)
			if length == n:	ans.append(place)
			else:
				for i in xrange(n):
					if (not i in place) and (not i+length in cross_plus) and (not i-length in cross_minus):
						backtrack(place+[i], cross_plus+[i+length], cross_minus+[i-length])
		ans = []
		backtrack([],[],[])
		return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in ans]

	# below has been improved:
	#   1. set place as the parameter of the backtrack() function
	#   2. no place initialization. use '+' operator rather than .append() to add element
	# this improved sol takes 168 ms, beating 45.5%
	# for short circuit condition, the judgment line could be improved
	def solveNQueens_improvd(self, n):
		def backtrack(now, place):
			if now == n:	ans.append(place)
			else:
				for i in xrange(n):
					put = True
					for row,col in enumerate(place[:now]):
						if not ((i-col) and (i+now-row-col) and (i-now-col+row)):	
							put = False
							break
					if put:
						backtrack(now + 1, place+[i])
		place, ans = [], []
		backtrack(0, place)
		return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in ans]

	# my original sol through backtracking
	# this sol takes 188 ms
	def solveNQueens_original(self, n):
		def backtrack(now):
			if now == n:	ans.append(list(place))
			else:
				for i in xrange(n):
					put = True
					for row,col in enumerate(place[:now]):
						if not  (i-col)*(i+now-row-col)*(i-now-col+row):	
							put = False
							break
					if put:
						place[now] = i
						backtrack(now + 1)
		place, ans = [None for x in xrange(n)], []
		backtrack(0)
		return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in ans]

if __name__ == '__main__':
	sol = Solution()
	print sol.solveNQueens_fastest(4)