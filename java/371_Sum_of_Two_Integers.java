// Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

// Example:
// Given a = 1 and b = 2, return 3.

// Credits:
// Special thanks to @fujiaozhu for adding this problem and creating all test cases.



// Runtime: 0 ms


public class Solution {
    public int getSum(int a, int b) {
        int carry = 0;
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            int mask = 1 << i;
            int bit1 = a & mask;
            int bit2 = b & mask;
            ans |= (bit1 ^ bit2 ^ carry);
            carry = (bit1 & bit2) | (bit2 & carry) | (bit1 & carry);
            carry = carry << 1;
        }
        return ans;
    }
}