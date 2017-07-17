// Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

// Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

// For example, you may serialize the following tree

//     1
//    / \
//   2   3
//      / \
//     4   5
// as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
// Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

// Credits:
// Special thanks to @Louis1992 for adding this problem and creating all test cases.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null){
            return "";
        }
        
        Queue<TreeNode> queue = new LinkedList();
        queue.add(root);
        StringBuilder ans = new StringBuilder();
        
        while(! queue.isEmpty()){
            TreeNode thisNode = queue.remove();
            if (thisNode != null){
                ans.append(thisNode.val).append(",");
            }else{
                ans.append("N").append(",");
                continue;
            }
            queue.add(thisNode.left);
            queue.add(thisNode.right);
        }
        ans.setLength(ans.length() - 1);
        return ans.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == ""){
            return null;
        }
        
        String[] nodesInfo = data.split(",");
        TreeNode ans = new TreeNode(Integer.parseInt(nodesInfo[0]));
        Queue<TreeNode> queue = new LinkedList();
        queue.add(ans);
        int idx = 1;
        
        while (idx < nodesInfo.length){
            TreeNode parentNode = queue.remove();
            if (!nodesInfo[idx].equals("N")){
                // System.out.println(nodesInfo[idx]);
                TreeNode leftNode = new TreeNode(Integer.parseInt(nodesInfo[idx]));
                parentNode.left = leftNode;
                queue.add(leftNode);
            }
            idx ++;
            if (!nodesInfo[idx].equals("N")){
                // System.out.println(nodesInfo[idx]);
                TreeNode rightNode = new TreeNode(Integer.parseInt(nodesInfo[idx]));
                parentNode.right = rightNode;
                queue.add(rightNode);
            }
            idx ++;
        }
        return ans;
        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));