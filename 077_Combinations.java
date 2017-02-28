// Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

// For example,
// If n = 4 and k = 2, a solution is:

// [
//   [2,4],
//   [3,4],
//   [2,3],
//   [1,2],
//   [1,3],
//   [1,4],
// ]

public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> finalAns = new ArrayList();
        int[] tmpAns = new int[k];
        dfs(tmpAns, 0, 1, n, finalAns);
        return finalAns;
    }
    public void dfs(int[] tmpAns, int curIdx, int startNum, int maxNum, List<List<Integer>> finalAns){
        if (curIdx == tmpAns.length){
            List<Integer> newAns = new ArrayList();
            for(int elem: tmpAns){
                newAns.add(elem);
            }
            finalAns.add(newAns);
            return;
        }
        int maxStart = maxNum - tmpAns.length + curIdx + 1;
        for(int i = startNum; i <= maxStart; i++){
            tmpAns[curIdx] = i;
            dfs(tmpAns, curIdx+1, i+1, maxNum, finalAns);
        }
    }
}