// Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

// For example,
// S = "ADOBECODEBANC"
// T = "ABC"
// Minimum window is "BANC".

// Note:
// If there is no such window in S that covers all characters in T, return the empty string "".

// If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.



// Runtime: 66 ms

public class Solution {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.equals("") || t.equals("")) return "";
        HashMap<Character, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < t.length(); i ++) {
            hashMap.put(t.charAt(i), hashMap.getOrDefault(t.charAt(i), 0) + 1);
        }
        int start = 0, end = 0;
        int ansStart = 0, ansLen = Integer.MAX_VALUE;
        while (end < s.length()) {
            while (end < s.length() && !containsAll(hashMap)) {
                Character thisChar = s.charAt(end++);
                if (hashMap.containsKey(thisChar)) {
                    hashMap.put(thisChar, hashMap.get(thisChar) - 1);
                }
            }
            while (start < end && containsAll(hashMap)) {
                if (end - start < ansLen) {
                    ansStart = start;
                    ansLen = end - start;
                }
                Character thisChar = s.charAt(start++);
                if (hashMap.containsKey(thisChar)) {
                    hashMap.put(thisChar, hashMap.get(thisChar) + 1);
                }
            }
        }
        return ansLen == Integer.MAX_VALUE ? "" : s.substring(ansStart, ansStart + ansLen);
    }
    
    private boolean containsAll(HashMap<Character, Integer> hashMap) {
        for (Character key: hashMap.keySet()) {
            if (hashMap.get(key) > 0) return false;
        }
        return true;
    }
}