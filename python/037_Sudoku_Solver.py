'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

Your input:
	["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

Expected answer:
	["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
'''
import time
class Solution(object):

	# using built-in data structure Set
	# this sol takes 136 ms, beating 83.26%
	dict_num = set(['1','2','3','4','5','6','7','8','9'])
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		def get_board(board):
			col_set, row_set, block_set, empty_cell = [set(Solution.dict_num) for x in range(9)],\
					[set(Solution.dict_num) for x in range(9)],[set(Solution.dict_num) for x in range(9)],[]
			for i,row in enumerate(board):
				for j,char in enumerate(row):
					if char == '.':		empty_cell.append([i,j])
					else:
						col_set[j].remove(char)
						row_set[i].remove(char)
						block_set[(i/3)*3+j/3].remove(char)
			empty_posi = []
			for posi in empty_cell:
				num = len(col_set[posi[1]] & row_set[posi[0]] & block_set[(posi[0]/3)*3+posi[1]/3])
				empty_posi.append((num,posi))
			empty_posi.sort()
			return(col_set, row_set, block_set, empty_posi)

		def backtrack(now, board, col_set, row_set, block_set, empty_posi):
			# if now == empty_count:	ans.append(list(board))		------ find all sol
			if now == empty_count:	return 1
			else:
				row, col = empty_posi[now][1][0], empty_posi[now][1][1]
				num_set = col_set[col] & row_set[row] & block_set[(row/3)*3+col/3]
				for i in num_set:
					board[row] = board[row][:col] + i + board[row][col+1:]
					col_set[col].remove(i)
					row_set[row].remove(i)
					block_set[(row/3)*3+col/3].remove(i)
					if backtrack(now+1, board, col_set, row_set, block_set, empty_posi):
						return 1
					board[row] = board[row][:col] + '.' + board[row][col+1:]
					col_set[col].add(i)
					row_set[row].add(i)
					block_set[(row/3)*3+col/3].add(i)
			return 0

		(col_set, row_set, block_set, empty_posi) = get_board(board)
		empty_count = len(empty_posi)
		backtrack(0, board, col_set, row_set, block_set, empty_posi)

		
if __name__ == '__main__':
	time.clock()
	sol = Solution()
	for i in xrange(8):
		board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
		sol.solveSudoku(board)
	print time.clock()