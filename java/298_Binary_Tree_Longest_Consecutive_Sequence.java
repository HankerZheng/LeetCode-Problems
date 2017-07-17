// Given a binary tree, find the length of the longest consecutive sequence path.

// The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

// For example,
//    1
//     \
//      3
//     / \
//    2   4
//         \
//          5
// Longest consecutive sequence path is 3-4-5, so return 3.
//    2
//     \
//      3
//     / 
//    2    
//   / 
//  1
// Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
// Show Company Tags
// Show Tags
// Show Similar Problems


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
    public int longestConsecutive(TreeNode root) {
        return dfs(root)[1];
    }
    public int[] dfs(TreeNode curNode){
        if (curNode == null){
            return new int[] {0,0};
        }
        // given a node representing a binary tree
        // return the length longestConsective of that tree
        int[] leftSubTree = dfs(curNode.left);
        int[] rightSubTree = dfs(curNode.right);
        int globalMaxLength = Math.max(leftSubTree[1], rightSubTree[1]);
        int localMaxLength = 1;
        if (curNode.left != null && curNode.val + 1 == curNode.left.val){
            localMaxLength = Math.max(localMaxLength, 1 + leftSubTree[0]);
        }
        if (curNode.right != null && curNode.val + 1 == curNode.right.val){
            localMaxLength = Math.max(localMaxLength, 1 + rightSubTree[0]);
        }
        int[] retArray = new int[2];
        retArray[0] = localMaxLength;
        retArray[1] = Math.max(globalMaxLength, localMaxLength);
        return retArray;
    }
}