// Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

// For example:
// Given the below binary tree and sum = 22,
//               5
//              / \
//             4   8
//            /   / \
//           11  13  4
//          /  \      \
//         7    2      1
// return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.



// Runtime: 4 ms

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
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) return false;
        Deque<Integer> sumStack = new LinkedList<>();
        Deque<TreeNode> nodeStack = new LinkedList<>();
        sumStack.addLast(root.val);
        nodeStack.addLast(root);
        while (!nodeStack.isEmpty()) {
            int curSum = sumStack.removeLast();
            TreeNode thisNode = nodeStack.removeLast();
            if (thisNode.left == null && thisNode.right == null && curSum == sum) return true;
            if (thisNode.left != null) {
                sumStack.addLast(curSum + thisNode.left.val);
                nodeStack.addLast(thisNode.left);
            }
            if (thisNode.right != null) {
                sumStack.addLast(curSum + thisNode.right.val);
                nodeStack.addLast(thisNode.right);
            }
        }
        return false;
        
    }
}