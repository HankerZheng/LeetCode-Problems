// Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

// You may assume that the array is non-empty and the majority element always exist in the array.

// Credits:
// Special thanks to @ts for adding this problem and creating all test cases.


// Runtime: 2 ms


public class Solution {
    public int majorityElement(int[] nums) {
        int major = nums[0];
        int count = 1;
        for (int i = 1; i < nums.length; i ++) {
            if (nums[i] == major) {
                count ++;
            } else {
                count --;
                if (count == 0) {
                    count = 1;
                    major = nums[i];
                }
            }
        }
        return major;
        
    }
}