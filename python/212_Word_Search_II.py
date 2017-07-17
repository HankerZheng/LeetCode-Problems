# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.

# For example,
# Given words = ["oath","pea","eat","rain"] and board =

# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

# click to show hint.

# Subscribe to see which companies asked this question


class TrieNode(object):
    def __init__(self, char, isWord=False):
        self.char = char
        self.children = {}
        self.isWord = False

class TrieTree(object):
    def __init__(self):
        self.root = TrieNode("dummy")

    def build_tree(self, word):
        if not word:
            return
        this_node = self.root
        for ch in word:
            if ch not in this_node.children:
                this_node.children[ch] = TrieNode(ch)
            this_node = this_node.children[ch]
        this_node.isWord = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(node, this_x, this_y, ans):
            # dfs search the node, and current posi is at (this_x, this_y)
            if node is None:
                return
            if node.isWord:
                res.add(ans)
            for delta_x, delta_y in delta:
                x, y = this_x+delta_x, this_y+delta_y
                if 0 <= x < top_x and 0 <= y < top_y and (x,y) not in visited:
                    this_char = board[x][y]
                    visited.add((x,y))
                    dfs(node.children.get(this_char, None), x, y, ans+this_char)
                    visited.remove((x,y))


        if not board or not board[0]:
            return []
        myTrieTree = TrieTree()
        for word in words:
            myTrieTree.build_tree(word)
        top_x, top_y = len(board), len(board[0])
        delta = [(0,1), (1,0), (-1,0), (0,-1)]
        res = set()
        visited = set()
        for i, line in enumerate(board):
            for j, char in enumerate(line):
                if char in myTrieTree.root.children:
                    visited.add((i,j))
                    dfs(myTrieTree.root.children[char], i, j, char)
                    visited.remove((i,j))
        return list(res)

if __name__ == '__main__':
    board = [   ['o','a','a','n'],
                ['e','t','a','e'],
                ['i','h','k','r'],
                ['i','f','l','v']]
    sol = Solution()
    print sol.findWords(board, ["oath","pea","eat","rain"])