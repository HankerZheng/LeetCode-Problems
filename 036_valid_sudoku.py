'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

Subscribe to see which companies asked this question

Your input:
	[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]

Expected answer:
	true
'''
import time
class Solution(object):

	# using built-in data structure Set
	# this sol takes 76 ms, beating 83.92%
	# try,except sol takes 92 ms, beating 38.75%
	dict_num = set(['1','2','3','4','5','6','7','8','9'])
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		col_set, row_set, block_set = [set(Solution.dict_num) for x in range(9)],\
				[set(Solution.dict_num) for x in range(9)],[set(Solution.dict_num) for x in range(9)]
		for i,row in enumerate(board):
			for j,char in enumerate(row):
				if not char == '.':
					if char in col_set[j]:		col_set[j].remove(char)
					else:						return False
					if char in row_set[i]:		row_set[i].remove(char)
					else:						return False
					if char in block_set[(i/3)*3+j/3]:	block_set[(i/3)*3+j/3].remove(char)
					else:						return False
		return True
		
if __name__ == '__main__':
	time.clock()
	sol = Solution()
	board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
	print sol.isValidSudoku(board)
	print time.clock()