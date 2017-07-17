// Given an integer n, return the number of trailing zeroes in n!.

// Note: Your solution should be in logarithmic time complexity.

// Credits:
// Special thanks to @ts for adding this problem and creating all test cases.

// Show Company Tags
// Show Tags
// Show Similar Problems


public class Solution {
    public int trailingZeroes(int n) {
        int count = 0;
        long factor = 5;
        while (factor <= n){
            count += n / factor;
            factor *= 5;
        }
        return count;
    }
}