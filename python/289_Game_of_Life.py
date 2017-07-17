# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.

# Follow up: 
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def count_neighbor(this_x, this_y):
            count = 0
            for delta_x, delta_y in neighbors:
                x, y = this_x + delta_x, this_y + delta_y
                if 0 <= x < top_x and 0 <= y < top_y:
                    count += (board[x][y] == 1 or board[x][y] == 2)
            return count
        if not board or not board[0]:
            return
        top_x = len(board)
        top_y = len(board[0])
        neighbors = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]
        for i, line in enumerate(board):
            for j, num in enumerate(line):
                environ = count_neighbor(i, j)
                if num == 1:
                    if environ > 3 or environ < 2:
                        board[i][j] = 2
                else:
                    if environ == 3:
                        board[i][j] = 3
        for i, line in enumerate(board):
            for j, num in enumerate(line):
                if num == 2:
                    board[i][j] = 0
                elif num == 3:
                    board[i][j] = 1

if __name__ == '__main__':
    sol = Solution()
    # board = [   [0,0,0,0,0],
    #             [0,1,1,0,0],
    #             [0,1,0,1,0],
    #             [0,0,1,0,0],
    #             [0,0,0,0,0]]
    # sol.gameOfLife(board)
    # for line in board:
    #     print line
    board = [   [0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,0,0,0]]
    sol.gameOfLife(board)
    for line in board:
        print line