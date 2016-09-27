# Write a program to find the nth super ugly number.

# Super ugly numbers are positive numbers whose all prime factors are
# in the given prime list primes of size k. For example, 
# [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of
# the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.

# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question

# Key Points: The same as 264 Ugly Number II
#             This method is Heap implementation
#
#   However, this method would meet MLE, because when primes get
#   more and more, it would push more numbers into heap than we need
#   Also, we store a tuple rather than one ugly number
#
# Run Time: ** ms

from heapq import *

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        headers = [0 for x in primes]
        ugly = [(1,1)]
        val = 1
        for i in xrange(n):
            val, fact = heappop(ugly)
            for prime in primes:
                if prime >= fact:
                    heappush(ugly,(val*prime,prime))
        return val

if __name__ == "__main__":
    test = Solution()
    for n in xrange(1,12):
        ans = test.nthSuperUglyNumber(n, [2,3,5])
        print ans
