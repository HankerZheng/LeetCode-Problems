// Given a binary tree, determine if it is height-balanced.

// For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


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
    public boolean isBalanced(TreeNode root) {
        return getNodeInfo(root)[0] == 1;
    }
    public int[] getNodeInfo(TreeNode node) {
        int[] retValue = {1, -1};
        if (node == null){
            return retValue;
        }
        
        int[] leftInfo = getNodeInfo(node.left);
        int[] rightInfo = getNodeInfo(node.right);

        if ((leftInfo[0] == 1)&& (rightInfo[0]==1)&&( Math.abs(leftInfo[1] - rightInfo[1]) <= 1)){
            retValue[1] = Math.max(rightInfo[1], leftInfo[1]) + 1;
        }else{
            retValue[0] = 0;
        }
        return retValue;
    }
}