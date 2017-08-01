// Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

// Example:

// nums = [1, 2, 3]
// target = 4

// The possible combination ways are:
// (1, 1, 1, 1)
// (1, 1, 2)
// (1, 2, 1)
// (1, 3)
// (2, 1, 1)
// (2, 2)
// (3, 1)

// Note that different sequences are counted as different combinations.

// Therefore the output is 7.
// Follow up:
// What if negative numbers are allowed in the given array?
// How does it change the problem?
// What limitation we need to add to the question to allow negative numbers?

// Credits:
// Special thanks to @pbrother for adding this problem and creating all test cases.


// Runtime: 7ms
// Time Complexity: O(n), n is the number of possible sum less than or equal to target.

public class Solution {
    public int combinationSum4(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        return memSearch(nums, hashmap, target);
    }
    
    public int memSearch(int[] nums, HashMap<Integer, Integer> hashmap, int target) {
        if (target == 0) { return 1;}
        if (target < 0)  { return 0; }
        if (hashmap.containsKey(target)) { return hashmap.get(target); }
        int res = 0;
        for(int i = 0; i < nums.length; i ++) {
            res += memSearch(nums, hashmap, target - nums[i]);
        }
        hashmap.put(target, res);
        return res;
    }
}