# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.

# Note that 1 is typically treated as an ugly number.
# 1 2 3 4 5
# 6
# 8 9 10 12 15
# 16 18 20 24 25  27 30 32 36 40
# 45 48 50 54 60  64 72 75 80 81
# 90 96 100 108 120 125 128 135
#
#
# Key Points: The new number must be 2/3/4 times one smaller ugly number.
#             Instead of maintaining 3 sorted list, keep track of 3 pointers
#
# Run time: 332 ms 

from heapq import *

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 5:
            return n
        heap = [(2,2), (3,3), (5,5)]
        for i in xrange(1,n):
            val, fact = heappop(heap)
            heappush(heap, (val*5, 5))
            if fact <= 2:
                heappush(heap, (val*2, 2))
            if fact <=3:
                heappush(heap, (val*3, 3))
            print heap
        return val

if __name__ == "__main__":
    test = Solution()
    for testcase in xrange(1,20):
        ans = test.nthUglyNumber(testcase)
        print ans
    # print test.nthUglyNumber(100)