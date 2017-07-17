/*Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.*/

public class Solution {
    public int maxSubArray(int[] nums) {
        if (nums.length == 0) return 0;
        int maxSum = nums[0];
        int curSum = nums[0];
        for (int i = 1; i < nums.length; i++){
            if (curSum + nums[i] < nums[i]){
                curSum = nums[i];
            }else{
                curSum += nums[i];
            }
            maxSum = Math.max(curSum, maxSum);
        }
        return maxSum;
    }
}