public class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) return s;
        StringBuilder[] lists = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            lists[i] = new StringBuilder();
        }
        int loopCount = (numRows - 1) * 2;
        for (int i = 0; i < s.length(); i++) {
            int curIdx = i % loopCount;
            int rowIdx = (curIdx < numRows) ? curIdx : (loopCount - curIdx);
            lists[rowIdx].append(s.charAt(i));
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numRows; i ++) {
            sb.append(lists[i].toString());
        }
        return sb.toString();
    }
}