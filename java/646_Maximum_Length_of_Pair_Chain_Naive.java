// You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

// Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

// Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

// Example 1:
// Input: [[1,2], [2,3], [3,4]]
// Output: 2
// Explanation: The longest chain is [1,2] -> [3,4]
// Note:
// The number of given pairs will be in the range [1, 1000].

// Naive Solution, O(n2)
// Runtime: 178 ms

public class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs,
            (e1, e2) -> {
                if(e1[0] == e2[0]){ return e1[1] - e2[1];}
                return e1[0] - e2[0];
        });
        int[] dp = new int[pairs.length];
        int res = 0;
        for (int i = 0; i < dp.length; i ++) {
            for (int j = 0; j < i; j++) {
                if (pairs[j][1] < pairs[i][0]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            res = Math.max(res, dp[i]);
        }
        return res + 1;
    }
}