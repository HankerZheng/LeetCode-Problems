// Given an input string, reverse the string word by word.

// For example,
// Given s = "the sky is blue",
// return "blue is sky the".

// Update (2015-02-12):
// For C programmers: Try to solve it in-place in O(1) space.

public class Solution {
    public String reverseWords(String s) {
        int start = 0, end = s.length() - 1;
        StringBuffer sb = new StringBuffer();
        String[] strings = s.trim().split("\\s+");
        if (strings == null || strings.length == 0){return "";}
        int index = strings.length - 1;
        while (index >= 0){
            sb.append(strings[index--]);
            sb.append(" ");
        }
        return sb.toString().substring(0, sb.length() - 1);
    }
}