// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution.

// Example:
// Given nums = [2, 7, 11, 15], target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].


public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> visitedNums = new HashMap();
        for (int i = 0; i < nums.length; i++){
            int com = target - nums[i];
            if (visitedNums.containsKey(com)){
                return new int[] {visitedNums.get(com), i};
            }else{
                visitedNums.put(nums[i], i);
            }
        }
        return new int[] {-1,-1};
        
    }
}