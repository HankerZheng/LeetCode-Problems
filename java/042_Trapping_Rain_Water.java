// Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

// For example, 
// Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


// Runtime: 18 ms


public class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) return 0;
        int left = 0, right = height.length - 1;
        int res = 0;
        int curHeight = Math.min(height[left], height[right]);
        while (left < right){
            while (left < right && height[left] <= curHeight) {
                res += (curHeight - height[left++]);
            }
            curHeight = Math.min(height[left], height[right]);
            while (left < right && height[right] <= curHeight) {
                res += (curHeight - height[right--]);
            }
            curHeight = Math.min(height[left], height[right]);
        }
        return res;
    }
}