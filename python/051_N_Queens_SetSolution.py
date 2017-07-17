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
        return ansList
    
    def dfs(self, rowIdx, curAns, colAvl, diagAvl1, diagAvl2, ansList, maxRow):
        if rowIdx == maxRow:
            ansList.append(curAns)
            return
        for colIdx in colAvl:
            diag1 = rowIdx - colIdx
            diag2 = rowIdx + colIdx
            if diag1 in diagAvl1 and diag2 in diagAvl2:
                newLine = "." * colIdx + "Q" + "."*(maxRow-colIdx-1)
                self.dfs(rowIdx + 1, curAns + [newLine], colAvl - {colIdx}, diagAvl1 - {diag1}, diagAvl2 - {diag2}, ansList, maxRow)
            
if __name__ == '__main__':
    sol = Solution()
    print sol.solveNQueens(4)