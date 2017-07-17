// Given a collection of distinct numbers, return all possible permutations.

// For example,
// [1,2,3] have the following permutations:
// [
//   [1,2,3],
//   [1,3,2],
//   [2,1,3],
//   [2,3,1],
//   [3,1,2],
//   [3,2,1]
// ]


// Runtime: 6ms
// Corner Case: 
//      1. the content of Arrays.asList(arr) would change if the arr changes

public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums.length == 0){
            return res;
        }
        
        Integer[] current = new Integer[nums.length];
        boolean[] visited = new boolean[nums.length];
        helper(res, nums, current, 0, visited);
        return res;        
    }
    
    private void helper(List<List<Integer>> res, int[] nums, Integer[] current, int pos, boolean[] visited) {
        if (pos == nums.length) {
            List<Integer> thisRes = new ArrayList<>(Arrays.asList(current));
            res.add(thisRes);
            return;
        }
        for (int i = 0; i < nums.length; i ++) {
            if (visited[i]) continue;
            visited[i] = true;
            current[pos] = nums[i];
            helper(res, nums, current, pos + 1, visited);
            visited[i] = false;
        }
    }
}