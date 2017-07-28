// You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

// Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

// Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

// Example 1:
// Input: [[1,2], [2,3], [3,4]]
// Output: 2
// Explanation: The longest chain is [1,2] -> [3,4]
// Note:
// The number of given pairs will be in the range [1, 1000].

// Naive Solution, O(nlogn)
// Runtime: 105 ms

public class Solution {
    public int findLongestChain(int[][] pairs) {
        if (pairs == null || pairs.length == 0) return 0;
        Arrays.sort(pairs, (e1, e2) -> e1[1] - e2[1]);
        int curEnd = pairs[0][1];
        int idx = 0;
        int curStack = 0;
        while (idx < pairs.length) {
            curEnd = pairs[idx++][1];
            curStack += 1;
            while (idx < pairs.length && pairs[idx][0] <= curEnd){
                idx ++;
            }
        }
        return curStack;
    }
}