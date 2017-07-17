// Given a string, find the length of the longest substring without repeating characters.

// Examples:

// Given "abcabcbb", the answer is "abc", which the length is 3.

// Given "bbbbb", the answer is "b", with the length of 1.

// Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> window = new HashSet();
        int startIdx = 0, endIdx = 0;
        int maxLength = 0;
        for (; endIdx < s.length(); endIdx ++){
            char thisChar = s.charAt(endIdx);
            while (window.contains(thisChar)){
                window.remove(s.charAt(startIdx));
                startIdx ++;
            }
            window.add(thisChar);
            maxLength = Math.max(maxLength, endIdx - startIdx + 1);
        }
        return maxLength;
        
    }
}