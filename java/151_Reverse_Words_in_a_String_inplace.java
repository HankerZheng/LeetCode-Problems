// Given an input string, reverse the string word by word.

// For example,
// Given s = "the sky is blue",
// return "blue is sky the".




// Runtime: 18ms


public class Solution {
    public String reverseWords(String s) {
        int start = 0, end = s.length() - 1;
        // handling blanck spaces at head and tail
        while (start < s.length() && s.charAt(start) == ' ') {
            start ++;
        }
        while (start < end && s.charAt(end) == ' ') {
            end --;
        }
        if (start > end) return "";
        // initial the char array
        char[] charArr = new char[end - start + 2];
        int cur = 0, i = start;
        while (i <= end) {
            while (i <= end && s.charAt(i) != ' ') {
                charArr[cur] = s.charAt(i);
                cur ++;
                i ++;
            }
            while (i <= end && s.charAt(i) == ' ') i ++;
            charArr[cur++] = ' ';
        }
        // reverse the char arr
        reverseCharArr(charArr);
        i = 0;
        while (i < charArr.length) {
            // skip the blank spaces
            while (charArr[i] == ' ') i++;
            i = reverseWord(charArr, i);
        }
        i = 0;
        while (i < charArr.length && charArr[i] == 0) i++;
        return (new String(charArr)).substring(i + 1);
        // return "";
    }
    
    
    private void reverseCharArr(char[] charArr) {
        int start = 0, end = charArr.length - 1;
        while (start < end) {
            char tmp = charArr[start];
            charArr[start] = charArr[end];
            charArr[end] = tmp;
            start ++;
            end --;
        }
    }
    
    private int reverseWord(char[] charArr, int startIdx) {
        int i = startIdx;
        while (i < charArr.length && charArr[i] != ' ') {
            i ++;
        }
        int retVal = i;
        int start = startIdx, end = retVal - 1;
        while (start < end) {
            char tmp = charArr[start];
            charArr[start] = charArr[end];
            charArr[end] = tmp;
            start ++;
            end --;
        }
        return retVal;
    }
}