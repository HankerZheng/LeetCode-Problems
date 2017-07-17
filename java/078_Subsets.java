// Given a set of distinct integers, nums, return all possible subsets.

// Note: The solution set must not contain duplicate subsets.

// For example,
// If nums = [1,2,3], a solution is:

// [
//   [3],
//   [1],
//   [2],
//   [1,2,3],
//   [1,3],
//   [2,3],
//   [1,2],
//   []
// ]

// Runtime: 2 ms

public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        helper(res, nums, current, 0);
        return res;
    }
    
    private void helper(List<List<Integer>> res, int[] nums, List<Integer> current, int pos) {
        if (pos == nums.length) {
            res.add(new ArrayList(current));
            return;
        }
        // add current num
        current.add(nums[pos]);
        helper(res, nums, current, pos + 1);
        current.remove(current.size() - 1);
        // add nothing
        helper(res, nums, current, pos + 1);
    }
}