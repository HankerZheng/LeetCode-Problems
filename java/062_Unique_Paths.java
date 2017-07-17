public class Solution {
    public int uniquePaths(int m, int n) {
        Map<Integer, Integer> history = new HashMap<>();
        return memSearch(m - 1, n - 1, n, history);
    }
    public int memSearch(int i, int j, int n, Map<Integer, Integer> history){
        Integer hashCode = i * n + j;
        if (i == 0 || j == 0){
            return 1;
        }else if(history.containsKey(hashCode)){
            return history.get(hashCode);
        }
        int thisAns = memSearch(i - 1, j, n, history) + memSearch(i, j - 1, n, history);
        history.put(hashCode, thisAns);
        return thisAns;
    }
}