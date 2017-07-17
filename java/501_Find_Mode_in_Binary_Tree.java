// Given a binary tree with duplicates. You have to find all the mode(s) in given binary tree.

// For example:
// Given binary tree [1,null,2,2],
//    1
//     \
//      2
//     /
//    2
// return [2].

// Note: If a tree has more than one mode, you can return them in any order.

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
    public int[] findMode(TreeNode root) {
        Map<Integer, Integer> visited = new HashMap();
        int maxOccurance = 1;
        Queue<TreeNode> queue = new LinkedList();
        queue.add(root);
        while (! queue.isEmpty()){
            TreeNode thisNode = queue.remove();
            int thisOccurance = visited.getOrDefault(thisNode.val, 0) + 1;
            visited.put(thisNode.val, thisOccurance);
            maxOccurance = Math.max(maxOccurance, thisOccurance);
            if (thisNode.left != null){
                queue.add(thisNode.left);
            }
            if(thisNode.right != null){
                queue.add(thisNode.right);
            }
        }
        
        List<Integer> ansList = new ArrayList();
        for (Integer nodeVal: visited.keySet()){
            if (visited.get(nodeVal) == maxOccurance){
                ansList.add(nodeVal);
            }
        }
        
        int[] ansArray = new int[ansList.size()];
        for(int i = 0; i<ansList.size(); i ++){
            ansArray[i] = ansList.get(i);
        }
        return ansArray;
    }
}