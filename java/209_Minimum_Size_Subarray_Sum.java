// Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

// For example, given the array [2,3,1,2,4,3] and s = 7,
// the subarray [4,3] has the minimal length under the problem constraint.

// click to show more practice.

// Credits:
// Special thanks to @Freezen for adding this problem and creating all test cases.



// Runtime: 3 ms


public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int curSum = 0;
        int start = 0, end = 0;
        int ans = Integer.MAX_VALUE;
        while (end < nums.length) {
            while (end < nums.length && curSum < s){
                curSum += nums[end++];                
            }
            while (start < end && curSum >= s) {
                curSum -= nums[start++];
                ans = Math.min(ans, end - start + 1);
            }
        }
        return ans == Integer.MAX_VALUE ? 0 : ans;
    }
}