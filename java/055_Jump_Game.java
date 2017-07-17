// # Given an array of non-negative integers, you are initially
// # positioned at the first index of the array.

// # Each element in the array represents your maximum jump length
// # at that position.

// # Determine if you are able to reach the last index.

// # For example:
// # A = [2,3,1,1,4], return true.

// # A = [3,2,1,0,4], return false.

// # Subscribe to see which companies asked this question

// # Show Tags


public class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length == 0) return false;
        int maxReach = 0;
        int curPos = 0;
        while (curPos < nums.length && curPos <= maxReach){
            maxReach = Math.max(maxReach, curPos + nums[curPos]);
            curPos += 1;
        }
        return maxReach >= nums.length - 1;
    }
}