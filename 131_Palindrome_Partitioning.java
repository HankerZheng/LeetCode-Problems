// Given a string s, partition s such that every substring of
// the partition is a palindrome.

// Return all possible palindrome partitioning of s.

// For example, given s = "aab",
// Return

// [
//   ["aa","b"],
//   ["a","a","b"]
// ]

// Runtime: 23ms

public class Solution {
    public List<List<String>> partition(String s) {
        Map<Integer, Boolean> memSearch = new HashMap<>();
        return helper(s, memSearch, s.length());
    }
    
    private List<List<String>> helper(String s, Map<Integer, Boolean> memSearch, int endIdx) {
        List<List<String>> res = new ArrayList<>();
        if (endIdx == 0) {
            res.add(new ArrayList<String>());
            return res;
        }
        
        for (int i = endIdx - 1; i >= 0; i --) {
            if (isPalindrome(s, memSearch, i, endIdx)) {
                String thisPalin = s.substring(i, endIdx);
                List<List<String>> preRes = helper(s, memSearch, i);
                for (List<String> elem: preRes) {
                    elem.add(thisPalin);
                    res.add(elem);
                }
            }
        }
        return res;
    }
    
    private boolean isPalindrome(String s, Map<Integer, Boolean> memSearch, int start, int end) {
        int curIdx = start * s.length() + end;
        if (memSearch.containsKey(curIdx)) {
            return memSearch.get(curIdx);
        }
        if (start + 1 == end) {
            memSearch.put(curIdx, true);
        } else if (start + 2 == end) {
            memSearch.put(curIdx, s.charAt(start) == s.charAt(end - 1));
        } else {
            memSearch.put(curIdx, s.charAt(start) == s.charAt(end - 1) && isPalindrome(s, memSearch, start + 1, end - 1));
        }
        return memSearch.get(curIdx);
    }
}