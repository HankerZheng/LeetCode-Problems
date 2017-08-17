// Write a function to find the longest common prefix string amongst an array of strings.



// Runtime: 12 ms

public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        char[] commonPrefix = strs[0].toCharArray();
        int endIdx = commonPrefix.length;
        for (int i = 1; i < strs.length; i++) {
            endIdx = getCommonPrefix(strs[i], commonPrefix, endIdx);
        }
        return strs[0].substring(0, endIdx);
    }
    
    private int getCommonPrefix(String s1, char[] chars, int end) {
        int i = 0;
        while (i < s1.length() && i < end) {
            if (s1.charAt(i) != chars[i]) break;
            i ++;
        }
        return i;
    }
}