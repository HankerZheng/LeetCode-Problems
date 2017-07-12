// Given a collection of integers that might contain duplicates, nums, return all possible subsets.

// Note: The solution set must not contain duplicate subsets.

// For example,
// If nums = [1,2,2], a solution is:

// [
//   [2],
//   [1],
//   [1,2,2],
//   [2,2],
//   [1,2],
//   []
// ]


// Runtime: 4ms


public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        Map<Integer, Integer> count = new HashMap<>();
        
        for (int i = 0; i < nums.length; i ++) {
            count.put(nums[i], count.getOrDefault(nums[i], 0) + 1);
        }
        int[] candidates = new int[count.size()];
        int i = 0;
        for (Integer key: count.keySet()){
            candidates[i++] = key;
        }
        
        helper(res, count, candidates, current, 0);
        return res;
    }
    
    public void helper(List<List<Integer>> res, Map<Integer, Integer> count, int[] candidates, List<Integer> current, int pos) {
        if (pos == candidates.length) {
            res.add(new ArrayList(current));
            return;
        }
        // add nothing
        helper(res, count, candidates, current, pos + 1);
        // add current number
        for (int i = 0; i < count.get(candidates[pos]); i ++){
            current.add(candidates[pos]);
            helper(res, count, candidates, current, pos + 1);
        }
        // remove the last added element
        for (int i = 0; i < count.get(candidates[pos]); i ++) {
            current.remove(current.size() - 1);
        }
    }
}