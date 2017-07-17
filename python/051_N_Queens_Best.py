"""
Create 3 sets for available positon.
    - colAvl: the set contains the available colNumber for the Queen
    - diagAvl1: the set contains the available (colIdx - rowIdx) for the Queen
                which represents the top-left to bottom-right diagonal
    - diagAvl2: the set contains the available (colIdx + rowIdx) for the Queen
                which represents the top-right to bottom-left diagonal

for each ans, we don't create the List[List[str]] to represent the board,
Instead, we only use a simple List[int] to represent a board. For example,
[1,3,2,0] represents the board showed below:
    . Q . .
    . . . Q
    . . Q .         The index in the list represents the rowIdx of the Queen
    Q . . .         The value in the list represents the colIdx of the Queen
Once an ans is found, we store the representive list into `ansList`
And at last, we create the String-representing board at `createBoard` function.
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n:
            return []
        ansList = []
        colAvl = set(range(n))
        diagAvl1 = set(range(1-n, n))
        diagAvl2 = set(range(2*n - 1))
        self.dfs(0, [], colAvl, diagAvl1, diagAvl2, ansList, n)
        return self.createBoard(ansList, n)
    
    def dfs(self, rowIdx, curAns, colAvl, diagAvl1, diagAvl2, ansList, maxRow):
        if rowIdx == maxRow:
            ansList.append(curAns)
            return
        for colIdx in colAvl:
            diag1 = rowIdx - colIdx
            diag2 = rowIdx + colIdx
            if diag1 in diagAvl1 and diag2 in diagAvl2:
                self.dfs(rowIdx + 1, curAns + [colIdx], colAvl - {colIdx}, diagAvl1 - {diag1}, diagAvl2 - {diag2}, ansList, maxRow)

    def createBoard(self, ansList, maxRow):
        fianlBoard = []
        for thisAns in ansList:
            thisBoard = ["."*colIdx + "Q" + "."*(maxRow-1-colIdx) for colIdx in thisAns]
            fianlBoard.append(thisBoard)
        return fianlBoard
            
if __name__ == '__main__':
    sol = Solution()
    print sol.solveNQueens(4)