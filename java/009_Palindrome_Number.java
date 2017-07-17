// Determine whether an integer is a palindrome. Do this without extra space.

public class Solution {
    public boolean isPalindrome(int x) {
        int reversedNum = 0;
        int tmp = x;
        while (tmp > 0){
            reversedNum = reversedNum * 10 + tmp % 10;
            tmp /= 10;
        }
        return x == reversedNum;
        
    }
}