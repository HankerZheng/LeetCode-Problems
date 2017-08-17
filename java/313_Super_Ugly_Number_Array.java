// Write a program to find the nth super ugly number.

// Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

// Note:
// (1) 1 is a super ugly number for any given primes.
// (2) The given numbers in primes are in ascending order.
// (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
// (4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.




// Runtime: 21 ms
// Thought: the new ugly number is generated by multiplying the prime with another
//          already generated ugly number. Therefore, we could maintain an index array
//          to store the index of the already-generated ugly numbers for each prime

public class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        if (n == 1) return 1;
        int[] ansArr = new int[n];
        int[] indexes = new int[primes.length];
        ansArr[0] = 1;
        for (int i = 1; i < n; i++) {
            ansArr[i] = getMin(primes, indexes, ansArr, ansArr[i-1]);
        }
        return ansArr[n-1];
    }
    
    private int getMin(int[] primes, int[] indexes, int[] ansArr, int cur) {
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < primes.length; i ++) {
            while (primes[i] * ansArr[indexes[i]] <= cur) {
                indexes[i] ++;
            }
            res = Math.min(res, primes[i] * ansArr[indexes[i]]);
        }
        return res;
    }
}
    