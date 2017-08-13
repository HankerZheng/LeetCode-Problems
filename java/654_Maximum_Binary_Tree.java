// Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

// The root is the maximum number in the array.
// The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
// The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
// Construct the maximum tree by the given array and output the root node of this tree.

// Example 1:
// Input: [3,2,1,6,0,5]
// Output: return the tree root node representing the following tree:

//       6
//     /   \
//    3     5
//     \    / 
//      2  0   
//        \
//         1
// Note:
// The size of the given array will be in the range [1,1000].


// Runtime: 13 ms


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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return helper(nums, 0, nums.length);
    }
    
    TreeNode helper(int[] nums, int start, int end) {
        if (start == end) {
            return null;
        }
        int maxIdx = start;
        int maxVal = nums[start];
        for (int i = start; i < end; i++){
            if (maxVal < nums[i]) {
                maxVal = nums[i];
                maxIdx = i;
            }
        }
        TreeNode root = new TreeNode(maxVal);
        root.left = helper(nums, start, maxIdx);
        root.right = helper(nums, maxIdx + 1, end);
        return root;
    }
}