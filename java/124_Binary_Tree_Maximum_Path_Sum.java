// Given a binary tree, find the maximum path sum.

// For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

// For example:
// Given the below binary tree,

//        1
//       / \
//      2   3
// Return 6.




// Runtime: 37ms


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
    HashMap<TreeNode, Integer> singlePath;
    HashMap<TreeNode, Integer> helperMap;
    
    public int maxPathSum(TreeNode root) {
        singlePath = new HashMap<>();
        helperMap = new HashMap<>();
        return helper(root);
    }
    
    private int helper(TreeNode root) {
        if (root == null) return Integer.MIN_VALUE;
        if (helperMap.containsKey(root)) return helperMap.get(root);
        int withRoot = Math.max(maxSinglePath(root), thisDoublePath(root));
        int fromLeft = helper(root.left);
        int fromRight = helper(root.right);
        int ans = Math.max(withRoot, Math.max(fromLeft, fromRight));
        helperMap.put(root, ans);
        return ans;
    }
    
    private int maxSinglePath(TreeNode root) {
        if (root == null) return 0;
        if (singlePath.containsKey(root)) return singlePath.get(root);
        int left = maxSinglePath(root.left);
        int right = maxSinglePath(root.right);
        int thisMax = Math.max(root.val + left, root.val + right);
        thisMax = Math.max(thisMax, root.val);
        singlePath.put(root, thisMax);
        return thisMax;
    }
    
    private int thisDoublePath(TreeNode root) {
        if (root == null) return 0;
        int left = maxSinglePath(root.left);
        int right = maxSinglePath(root.right);
        return Math.max(root.val, root.val + left + right);
    }
}