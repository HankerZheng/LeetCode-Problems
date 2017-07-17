// Given n pairs of parentheses, write a function to generate
// all combinations of well-formed parentheses.

// For example, given n = 3, a solution set is:

// [
//   "((()))",
//   "(()())",
//   "(())()",
//   "()(())",
//   "()()()"
// ]

// Runtime: 5ms


public class Solution {
    
    public List<String> generateParenthesis(int n) {
        
        if ( n == 0) {
            return new ArrayList<String>();
        }
        String rightParen = new String(new char[n]).replace("\0", ")");
        List<String> res = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        helper(rightParen, res, sb, n, n);
        return res;
    }
    
    private void helper(String rightParen, List<String> res, StringBuilder sb, int left, int right) {

        if (left == 0 && right >= 1) {
            res.add(sb.toString() + rightParen.substring(0, right));
            return;
        }
        // add left
        sb.append("(");
        helper(rightParen, res, sb, left - 1, right);
        sb.deleteCharAt(sb.length() - 1);
        if (right > left){
            // add right
            sb.append(")");
            helper(rightParen, res, sb, left, right - 1);
            sb.deleteCharAt(sb.length() - 1);            
        }
    }
}