// Given preorder and inorder traversal of a tree, construct the binary tree.

// Note:
// You may assume that duplicates do not exist in the tree.



// Runtime: 5 ms

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
    
    int[] preorder;
    int[] inorder;
    HashMap<Integer, Integer> indexHash;
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        indexHash = new HashMap<>();
        for (int i = 0; i < inorder.length; i ++) {
            indexHash.put(inorder[i], i);
        }
        return createNode(0, preorder.length, 0, inorder.length);
    }
    // endIdx is not included
    private TreeNode createNode(int pstart, int pend, int istart, int iend) {
        if (pstart == pend) return null;
        TreeNode root = new TreeNode(preorder[pstart]);
        int idx = indexHash.get(root.val);
        int length = idx - istart;
        root.left = createNode(pstart + 1, pstart + 1 + length, istart, idx);
        root.right = createNode(pstart + 1 + length, pend, idx + 1, iend);
        return root;
    }
}