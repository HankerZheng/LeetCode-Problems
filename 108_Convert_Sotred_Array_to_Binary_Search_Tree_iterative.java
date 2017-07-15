// Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

// Seen this question in a real interview before?   Yes  

// Runtime: 1 ms

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Param {
    int start;
    int end;
    TreeNode node;
    Param(int start, int end, TreeNode node){
        this.start = start;
        this.end = end;
        this.node = node;
    }
}

public class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        int mid = getMidIdx(0, nums.length);
        TreeNode res = TereNode(nums[mid]);
        Stack<Param> stack = new Stack<>();
        stack.add(new Param(0, nums.length, res));
        while (!stack.isEmpty()) {
            Param param = stack.pop();
            int midl = getMidIdx(0, getMidIdx(param.start, param.end))
            thisNode.left = new TreeNode();
            thisNode.right = new TreeNode();
        }
        return res;
    }
}

