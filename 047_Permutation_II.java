// Given a collection of numbers that might contain duplicates,
// return all possible unique permutations.

// For example,
// [1,1,2] have the following unique permutations:
// [
//   [1,1,2],
//   [1,2,1],
//   [2,1,1]
// ]

// Runtime: 21 ms



public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Integer[] current = new Integer[nums.length];
        boolean[] chosen = new boolean[nums.length];
        helper(res, nums, current, 0, chosen);
        return res;
    }
    
    private void helper(List<List<Integer>> res, int[] nums, Integer[] current, int pos, boolean[] chosen) {
        if (pos == nums.length) {
            res.add(new ArrayList<>(Arrays.asList(current)));
            return;
        }
        Set<Integer> visited = new HashSet<>();
        for(int i = 0; i < nums.length; i++) {
            if (!visited.contains(nums[i]) && !chosen[i]) {
                visited.add(nums[i]);
                chosen[i] = true;
                current[pos] = nums[i];
                helper(res, nums, current, pos + 1, chosen);
                chosen[i] = false;
            }
        }
    }
}