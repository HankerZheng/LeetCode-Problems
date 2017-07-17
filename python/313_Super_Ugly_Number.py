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
#             This method is Dynamic Programming implementation
#
# Run Time: 1324 ms

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        headers = [0 for x in primes]
        ugly = [1]
        next = 1
        for i in xrange(n-1):
            next = min([ugly[headers[index]]*primes[index] for index in xrange(len(headers))])
            ugly.append(next)
            for index in xrange(len(headers)):
                # the most time-consuming work
                if primes[index]*ugly[headers[index]] <= next:
                    headers[index]+=1
        return next

if __name__ == "__main__":
    test = Solution()
    for n in xrange(1,40):
        ans = test.nthSuperUglyNumber(n, [2,23,57,97])
        print ans
