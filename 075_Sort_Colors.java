// Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

// Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

// Note:
// You are not suppose to use the library's sort function for this problem.

// click to show follow up.

public class Solution {
    public void sortColors(int[] nums) {
        int zeroIdx = 0, twoIdx = nums.length - 1, curIdx = 0;
        while (curIdx <= twoIdx){
            while (curIdx < twoIdx && nums[curIdx] == 2){
                swap(nums, curIdx, twoIdx --);
            }
            while (curIdx > zeroIdx && nums[curIdx] == 0){
                swap(nums, curIdx, zeroIdx ++);
            }
            curIdx ++;
        }
    }
    
    public void swap(int[] nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}