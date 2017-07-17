// Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

// According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

//         _______3______
//        /              \
//     ___5__          ___1__
//    /      \        /      \
//    6      _2       0       8
//          /  \
//          7   4
// For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.



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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode dummy = new TreeNode(-1);
        dummy.left = root;
        Stack<TreeNode> traverseStack = new Stack<>();
        Stack<TreeNode> ancesterStack = new Stack<>();
        traverseStack.add(root);
        ancesterStack.add(dummy);
        int foundFlag = 0;
        int pos = 0;
        
        while (foundFlag != 1 && !traverseStack.isEmpty()) {
            TreeNode thisNode = traverseStack.pop();
            TreeNode ancester = ancesterStack.peek();
            // update the ancesterStack
            while(ancester.left != thisNode && ancester.right != thisNode) {
                ancesterStack.pop();
                ancester = ancesterStack.peek();
            }
            ancesterStack.push(thisNode);
            if (thisNode == p || thisNode == q) {
                foundFlag += 1;
                pos = ancesterStack.size();
            }
            if (thisNode.right != null) traverseStack.push(thisNode.right);
            if (thisNode.left != null) traverseStack.push(thisNode.left);
        }
        System.out.println(ancesterStack);
        
        while (foundFlag != 2 && !traverseStack.isEmpty()) {
            TreeNode thisNode = traverseStack.pop();
            TreeNode ancester = ancesterStack.peek();
            // update the ancesterStack
            while(ancester.left != thisNode && ancester.right != thisNode) {
                ancesterStack.pop();
                ancester = ancesterStack.peek();
            }
            pos = Math.min(pos, ancesterStack.size());
            ancesterStack.push(thisNode);
            if (thisNode == p || thisNode == q) {
                foundFlag += 1;
            }
            if (thisNode.right != null) traverseStack.push(thisNode.right);
            if (thisNode.left != null) traverseStack.push(thisNode.left);            
        }
        if (foundFlag != 2) {
            return null;
        }
        while (ancesterStack.size() > pos) {
            ancesterStack.pop();
        }
        return ancesterStack.peek();
    }
}