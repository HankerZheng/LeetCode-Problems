// Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

// Example 1:
// Input: [1,1,2,3,3,4,4,8,8]
// Output: 2
// Example 2:
// Input: [3,3,7,7,10,11,11]
// Output: 10
// Note: Your solution should run in O(log n) time and O(1) space.


// Runtime: 1 ms


public class Solution {
    public int singleNonDuplicate(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        int start = 0, end = nums.length - 1;
        int mid = 0;
        while (start < end) {
            mid = (start + end) >>> 1;
            if (nums[mid] == nums[mid^1]) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return nums[start];
    }
}