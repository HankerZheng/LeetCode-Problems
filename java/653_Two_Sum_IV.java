
// Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

// Example 1:
// Input: 
//     5
//    / \
//   3   6
//  / \   \
// 2   4   7

// Target = 9

// Output: True
// Example 2:
// Input: 
//     5
//    / \
//   3   6
//  / \   \
// 2   4   7

// Target = 28

// Output: False


// Runtime: 37 ms


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
    public boolean findTarget(TreeNode root, int k) {
        HashSet<Integer> hashSet = new HashSet();
        // traverse the tree;
        Deque<TreeNode> stack = new LinkedList<>();
        stack.addLast(root);
        while (!stack.isEmpty()) {
            TreeNode thisNode = stack.removeLast();
            if (hashSet.contains(k - thisNode.val)){
                return true;
            } else {
                hashSet.add(thisNode.val);
            }
            if (thisNode.left != null) stack.addLast(thisNode.left);
            if (thisNode.right != null) stack.addLast(thisNode.right);
        }
        return false;
    }
}