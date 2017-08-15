// Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

// Example:

// Input: "babad"

// Output: "bab"

// Note: "aba" is also a valid answer.
// Example:

// Input: "cbbd"

// Output: "bb"



// Runtime: 119 ms

public class Solution {
    public String longestPalindrome(String s) {
        int length = s.length();
        boolean[][] subPalin = new boolean[length][length];
        int maxLength = 1;
        int startIdx = 0;
        
        for (int i = 0; i < length; i++){
            subPalin[i][i] = true;
            if (i+1 < length && s.charAt(i) == s.charAt(i+1)){
                subPalin[i][i+1] = true;
                maxLength = 2;
                startIdx = i;
            }
        }
        for (int delta = 2; delta < length; delta ++){
            for (int i = 0; i + delta < length; i++){
                int j = i + delta;
                subPalin[i][j] = subPalin[i+1][j-1] && s.charAt(i) == s.charAt(j);
                if (subPalin[i][j]){
                    maxLength = delta + 1;
                    startIdx = i;
                }
            }
        }
        return s.substring(startIdx, startIdx + maxLength);
    }
}