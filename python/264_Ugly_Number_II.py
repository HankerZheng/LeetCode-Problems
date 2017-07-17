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
#             Maintain 3 sorted list.
#
# Run time: 448 ms 


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 5:
            return n
        l2, l3, l5 = [3,4,5], [2,3,4,5], [2,3,4,5]
        for index in xrange(6, n+1): 
            next = min(l2[0]*2, l3[0]*3, l5[0]*5)
            while l2[0]*2 <= next:
                l2.pop(0)
            l2.append(next)
            while l3[0]*3 <= next:
                l3.pop(0)
            l3.append(next)
            while l5[0]*5 <= next:
                l5.pop(0)
            l5.append(next)
        return next

if __name__ == "__main__":
    test = Solution()
    for testcase in xrange(1,20):
        ans = test.nthUglyNumber(testcase)
        print ans
    # print test.nthUglyNumber(10)