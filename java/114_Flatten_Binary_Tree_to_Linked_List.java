// Given a binary tree, flatten it to a linked list in-place.

// For example,
// Given

//          1
//         / \
//        2   5
//       / \   \
//      3   4   6
// The flattened tree should look like:
//    1
//     \
//      2
//       \
//        3
//         \
//          4
//           \
//            5
//             \
//              6




// Runtime: 1 ms
// The helper function would return the last node of the flatten linked list

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
    public void flatten(TreeNode root) {
        helper(root);
    }
    // return the last node of the flatten list
    private TreeNode helper(TreeNode root) {
        if (root == null)  return null;
        TreeNode leftNode = root.left;
        TreeNode rightNode = root.right;
        TreeNode leftList = helper(leftNode);
        TreeNode rightList = helper(rightNode);
        
        TreeNode tmp = root;
        if (leftList != null) {
            tmp.right = leftNode;
            tmp.left = null;
            tmp = leftList;
        }
        if (rightList != null) {
            tmp.right = rightNode;
            tmp.left = null;
            tmp = rightList;
        }
        tmp.left = null;
        tmp.right = null;
        return tmp;
    }
}