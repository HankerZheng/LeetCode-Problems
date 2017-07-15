// Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

// Seen this question in a real interview before?   Yes  

// Runtime: 1 ms

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return helper(nums, 0, nums.length);
    }
    
    private TreeNode helper(int[] nums, int start, int end) {
        if (start == end) return null;
        int mid = (start >> 1) + (end >> 1);
        TreeNode res = new TreeNode(nums[mid]);
        res.left = helper(nums, start, mid);
        res.right = helper(nums, mid + 1, end);
        return res;
    }
}

