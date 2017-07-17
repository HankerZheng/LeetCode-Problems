// Given two strings s and t, write a function to determine if t is an anagram of s.

// For example,
// s = "anagram", t = "nagaram", return true.
// s = "rat", t = "car", return false.

// Note:
// You may assume the string contains only lowercase alphabets.

// Follow up:
// What if the inputs contain unicode characters? How would you adapt your solution to such case?

// Show Company Tags
// Show Tags
// Show Similar Problems


public class Solution {
    public boolean isAnagram(String s, String t) {
        int[] srcChar = new int[26];
        if (s.length() != t.length()){
            return false;
        }
        for(int i = 0; i < s.length(); i++){
            srcChar[s.charAt(i) - 'a'] ++;
        }
        for(int i = 0; i < t.length(); i++){
            if (--srcChar[t.charAt(i) - 'a'] < 0){
                return false;
            }
        }
        return true;
    }
}