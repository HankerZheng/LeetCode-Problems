// Given a binary tree, find the maximum path sum.

// For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

// For example:
// Given the below binary tree,

//        1
//       / \
//      2   3
// Return 6.




// Runtime:


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

    int max;
    
    public int maxPathSum(TreeNode root) {
        max = Integer.MIN_VALUE;
        maxSinglePath(root);
        return max;
    }

    private int maxSinglePath(TreeNode root) {
        if (root == null) return 0;
        int left = maxSinglePath(root.left);
        int right = maxSinglePath(root.right);
        int thisMax = Math.max(left + root.val, right + root.val);
        thisMax = Math.max(thisMax, root.val + left + right);
        max = Math.max(max, thisMax);
    }
}