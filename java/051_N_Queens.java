

public class Solution {

    public List<List<String>> solveNQueens(int n) {
        boolean[] colAvl = new boolean[n];
        boolean[] diagAvl1 = new boolean[(n<<1)-1];
        boolean[] diagAvl2 = new boolean[(n<<1)-1];
        List<List<String>> finalAns = new ArrayList();
        int[] queuePlaced = new int[n];
        dfs(0, n, queuePlaced, colAvl, diagAvl1, diagAvl2, finalAns);
        // System.out.println(finalAns);
        return finalAns;
    }

    public void dfs(int rowIdx, int n, int[] queuePlaced, boolean[] colAvl, boolean[] diagAvl1, boolean[] diagAvl2, List finalAns){
        if (rowIdx == n){
            char[] stringSeq = new char[n];
            List<String> thisAns = new ArrayList();
            for(int row = 0; row < n; row++){
                for(int colIdx = 0; colIdx < n; colIdx++){
                    stringSeq[colIdx] = colIdx==queuePlaced[row]? 'Q' : '.';
                }
                thisAns.add(new String(stringSeq));
            }
            finalAns.add(thisAns);
            return;
        }
        for (int colIdx = 0; colIdx < n; colIdx ++){
            int diag1 = colIdx - rowIdx + n - 1;
            int diag2 = colIdx + rowIdx;
            if ( !colAvl[colIdx] && !diagAvl1[diag1] && !diagAvl2[diag2]){
                colAvl[colIdx] = !colAvl[colIdx];
                diagAvl1[diag1] = !diagAvl1[diag1];
                diagAvl2[diag2] = !diagAvl2[diag2];
                queuePlaced[rowIdx] = colIdx;
                dfs(rowIdx + 1, n, queuePlaced, colAvl, diagAvl1, diagAvl2, finalAns);
                colAvl[colIdx] = !colAvl[colIdx];
                diagAvl1[diag1] = !diagAvl1[diag1];
                diagAvl2[diag2] = !diagAvl2[diag2];
            }
            
        }
    }
}