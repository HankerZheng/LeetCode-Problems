public class Solution {

    String leftP = "([{";
    String rightP = ")]}";

    public boolean isValid(String s) {
        if (rightP.indexOf(s.charAt(0)) != -1) return false;
        Deque<Character> stack = new LinkedList<>();
        for (int i = 0; i < s.length(); i++) {
            char thisChar = s.charAt(i);
            if (leftP.indexOf(thisChar) != -1) { stack.addLast(thisChar);}
            else if (!stack.isEmpty()){
                char prevP = stack.removeLast();
                if (leftP.indexOf(prevP) != leftP.indexOf(thisChar)) return false;
            } else {
                return false;
            }
        }
        return stack.size() == 0;
    }
}