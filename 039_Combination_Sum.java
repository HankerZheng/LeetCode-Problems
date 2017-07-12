// Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

// The same repeated number may be chosen from C unlimited number of times.

// Note:
// All numbers (including target) will be positive integers.
// The solution set must not contain duplicate combinations.
// For example, given candidate set [2, 3, 6, 7] and target 7, 
// A solution set is: 
// [
//   [7],
//   [2, 2, 3]
// ]

// Runtime: 21ms

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        helper(res, candidates, new ArrayList(), target, 0);
        return res;
    }
    
    private void helper(List<List<Integer>> res, int[] candidates, List<Integer> current, int target, int pos) {
        if (pos == candidates.length) {
            if (target == 0) {
                res.add(new ArrayList(current));
            }
            return;
        }
        int curNum = candidates[pos];
        int left = target;
        // do not add curNum
        helper(res, candidates, current, left, pos + 1);
        // add curNum several times
        while (left >= curNum) {
            current.add(curNum);
            helper(res, candidates, current, left - curNum, pos + 1);
            left -= curNum;
        }
        // remove curNum
        for(int i = 0; i < target / curNum; i++) {
            current.remove(current.size() - 1);
        }        
    }
}