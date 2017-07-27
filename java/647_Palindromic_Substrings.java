// Given a string, your task is to count how many palindromic substrings in this string.

// The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

// Example 1:
// Input: "abc"
// Output: 3
// Explanation: Three palindromic strings: "a", "b", "c".
// Example 2:
// Input: "aaa"
// Output: 6
// Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
// Note:
// The input string length won't exceed 1000.


public class Solution {
    public int countSubstrings(String s) {
        if (s == null || s.length() == 0) { return 0;}
        int res = 0;
        boolean[][] dp = new boolean[s.length()][s.length()];
        for(int i = 0; i < s.length(); i++) {
            for(int j = 0; (i + j) < s.length(); j ++) {
                int start = j, end = start + i, delta = i;
                if (delta == 0) {
                    dp[start][start + delta] = true;
                }
                else if (delta == 1) {
                    dp[start][end] = s.charAt(start) == s.charAt(end);
                }
                else{
                    dp[start][end] = dp[start + 1][end - 1] && s.charAt(start) == s.charAt(end);
                }
                res += (dp[start][end] ? 1 : 0);
            }
        }
        return res;
    }
}