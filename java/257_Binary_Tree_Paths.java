// Given a binary tree, return all root-to-leaf paths.

// For example, given the following binary tree:

//    1
//  /   \
// 2     3
//  \
//   5
// All root-to-leaf paths are:

// ["1->2->5", "1->3"]




// Runtime: 16 ms

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
    public List<String> binaryTreePaths(TreeNode root) {
        if (root == null) return new ArrayList<String>();
        List<String> left = binaryTreePaths(root.left);
        List<String> right = binaryTreePaths(root.right);
        List<String> ans = left;
        ans.addAll(right);
        if (ans.size() == 0){
            ans.add(root.val + "");
        } else {
            for (int i = 0; i < ans.size(); i ++) {
                ans.set(i, root.val + "->" + ans.get(i));
            }
        }
        return ans;
    }
}