// Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

// For example, given the array [2,3,1,2,4,3] and s = 7,
// the subarray [4,3] has the minimal length under the problem constraint.

// click to show more practice.

// Credits:
// Special thanks to @Freezen for adding this problem and creating all test cases.



// Runtime: 6 ms

public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int[] sums = new int[nums.length + 1];
        sums[0] = 0;
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i ++) {
            sums[i+1] = sums[i] + nums[i];
            int findIdx = binarySearch(sums, sums[i+1] - s, i+1);
            if (findIdx >= 0) {
                ans = Math.min(ans, i + 1 - findIdx);
            }
        }
        return ans == Integer.MAX_VALUE ? 0 : ans;
    }
    
    private int binarySearch(int[] nums, int target, int end) {
        if (target < 0) return -1;
        int left = 0, right = end;
        while (left <= right) {
            int mid = (left + right ) >>> 1;
            if (nums[mid] > target) right = mid - 1;
            else left = mid + 1;
        }
        return right;
    }
}