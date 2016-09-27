# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# For example,
# Given board =

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

# Key Points: dp
#             dp[i] means the first i-th elements match
# Runtime: 472

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def border_test(x,y):
            return x>=0 and x<len(board) and y>=0 and y<len(board[x])

        def helper(used, info_list, index):
            if index == len(word):
                return True if info_list else False
            if not info_list:
                return False
            for (x,y) in info_list:
                this_list = []
                used[x][y] = 1
                if border_test(x+1,y) and word[index]==board[x+1][y] and not used[x+1][y]:
                    this_list.append((x+1,y))
                if border_test(x-1,y) and word[index]==board[x-1][y] and not used[x-1][y]:
                    this_list.append((x-1,y))
                if border_test(x,y+1) and word[index]==board[x][y+1] and not used[x][y+1]:
                    this_list.append((x,y+1))
                if border_test(x,y-1) and word[index]==board[x][y-1] and not used[x][y-1]:
                    this_list.append((x,y-1))
                if this_list and helper(used, this_list, index+1):
                    return True
                used[x][y] = 0
            return False

        info_list = []
        used = [[0 for _ in board[0]] for __ in board]
        for i,row in enumerate(board):
            for j,ch in enumerate(row):
                if ch == word[0]:
                    info_list.append((i,j))
        return helper(used, info_list, 1)

if __name__ == '__main__':
    sol = Solution()
    # board = [  'ABCE',
    #            'SFCS',
    #            'ADEE']
    # print sol.exist(board, "ABCCED")
    # print sol.exist(board, "SEE")
    # print sol.exist(board, "ABCB")
    # print sol.exist(board, "CD")
    # print sol.exist(board, "ABCE")
    board = ['aa']
    # print sol.exist(board, "aa")
    print sol.exist(board, "aaaa")
    # board = ['ab','cd']
    # print sol.exist(board, "bdca")
    # board = ["CAA","AAA","BCD"]
    # print sol.exist(board, "AAB")