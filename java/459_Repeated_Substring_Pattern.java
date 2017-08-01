// Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

// Example 1:
// Input: "abab"

// Output: True

// Explanation: It's the substring "ab" twice.
// Example 2:
// Input: "aba"

// Output: False
// Example 3:
// Input: "abcabcabcabc"

// Output: True

// Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


// Runtime: 23 ms

public class Solution {
    public boolean repeatedSubstringPattern(String s) {
        int length = s.length();
        for (int i = 2; i <= s.length(); i ++) {
            if (length % i != 0) continue;
            int sublength = length / i;
            int start = sublength;
            int count = 0;
            String standard = s.substring(0, sublength);
            while (start < s.length()) {
                String thisStr = s.substring(start, start + sublength);
                if (thisStr.equals(standard)){
                    count ++;
                } else {break;}
                start += sublength;
            }
            if (count == i - 1) { return true; }
        }
        return false;
        
    }
}