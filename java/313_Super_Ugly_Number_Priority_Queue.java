// Write a program to find the nth super ugly number.

// Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

// Note:
// (1) 1 is a super ugly number for any given primes.
// (2) The given numbers in primes are in ascending order.
// (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
// (4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.



// Runtime: 212 ms

public class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        Arrays.sort(primes);
        PriorityQueue<Node> pq = new PriorityQueue<>((e1, e2) -> (e1.val >= e2.val) ? 1: -1 );
        pq.offer(new Node(1, 0));
        long ans = 0;
        for (int i = 0; i < n; i++) {
            Node thisNode = pq.poll();
            ans = thisNode.val;
            for (int j = thisNode.prev; j < primes.length; j++) {
                pq.offer(new Node(thisNode.val * primes[j], j));
            }
        }
        return (int) ans;
    }
    
    class Node{
        public long val;
        public int prev;
        public Node(long val, int prev) {
            this.val = val;
            this.prev = prev;
        }
    }
}