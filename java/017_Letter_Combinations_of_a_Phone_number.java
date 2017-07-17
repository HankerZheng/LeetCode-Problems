// Given a digit string, return all possible letter combinations
// that the number could represent.

// A mapping of digit to letters (just like on the
// telephone buttons) is given below.

// Input:Digit string "23"
// Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
// Note:
// Although the above answer is in lexicographical order, your answer could be in any order you want.

// Runtime: 4ms
// Corner Case: input with invalid buttongs is not considered.

public class Solution {
    public List<String> letterCombinations(String digits) {
        if ("".equals(digits)){
            return new ArrayList<String>();
        }
        Map<Character, String> keyBoard = new HashMap<>();
        keyBoard.put('2', "abc");
        keyBoard.put('3', "def");
        keyBoard.put('4', "ghi");
        keyBoard.put('5', "jkl");
        keyBoard.put('6', "mno");
        keyBoard.put('7', "pqrs");
        keyBoard.put('8', "tuv");
        keyBoard.put('9', "wxyz");
        List<String> res = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        
        helper(digits, keyBoard, res, sb, 0);
        return res;
    }
    
    private void helper(String digits, Map<Character, String> keyBoard, List<String> res, StringBuilder sb, int pos) {
        if (pos == digits.length()) {
            res.add(sb.toString());
            return;
        }
        String candidate = keyBoard.getOrDefault(digits.charAt(pos), "");
        for(int i = 0; i < candidate.length(); i++) {
            sb.append(candidate.charAt(i));
            helper(digits, keyBoard, res, sb, pos + 1);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}