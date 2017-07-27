// In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

// Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

// You need to output the sentence after the replacement.

// Example 1:
// Input: dict = ["cat", "bat", "rat"]
// sentence = "the cattle was rattled by the battery"
// Output: "the cat was rat by the bat"
// Note:
// The input will only have lower-case letters.
// 1 <= dict words number <= 1000
// 1 <= sentence words number <= 1000
// 1 <= root length <= 100
// 1 <= sentence words length <= 1000


// Trie Tree
// Runtime: 27 ms;

import java.util.*;

public class Solution {
    public String replaceWords(List<String> dict, String sentence) {
        TrieTree tt = new TrieTree();
        for (String root: dict) {
            tt.addWord(root);
        }
        String[] words = sentence.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < words.length; i ++) {
            String word = words[i];
            TreeNode resNode = tt.findPartial(word);
            if(resNode != null) {
                sb.append(resNode.wordEnd);
            } else {
                sb.append(word);
            }
            sb.append(" ");
        }
        return sb.toString().substring(0, sb.length() - 1);
    }
}


class TreeNode {
    char val;
    TreeNode[] child;
    String wordEnd;

    public TreeNode(char thisCh) {
        val = thisCh;
        child = new TreeNode[26];
    }
}

class TrieTree {

    TreeNode root;

    public TrieTree() {
        root = new TreeNode(' ');
    }

    public void addWord(String str) {
        TreeNode thisNode = root;
        for(int i = 0; i < str.length(); i++) {
            char thisChar = str.charAt(i);
            if(thisNode.child[thisChar - 'a'] == null ){
                thisNode.child[thisChar - 'a'] = new TreeNode(thisChar);
            }
            thisNode = thisNode.child[thisChar - 'a'];
        }
        thisNode.wordEnd = str;
    }

    public boolean findWord(String str){
        TreeNode thisNode = root;
        for(int i = 0; i < str.length() && thisNode != null; i++) {
            char thisChar = str.charAt(i);
            thisNode = thisNode.child[thisChar - 'a'];
        }
        return thisNode != null && (thisNode.wordEnd != null);
    }

    public boolean findPrefix(String str) {
        TreeNode thisNode = root;
        for(int i = 0; i < str.length() && thisNode != null; i++) {
            char thisChar = str.charAt(i);
            thisNode = thisNode.child[thisChar - 'a'];
        }
        return thisNode != null;
    }

    public TreeNode findPartial(String str) {
        TreeNode thisNode = root;
        for(int i = 0; i < str.length() && thisNode != null; i++) {
            if (thisNode.wordEnd != null) {
                return thisNode;
            }
            char thisChar = str.charAt(i);
            thisNode = thisNode.child[thisChar - 'a'];
        }
        return null;
    }
}