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
# Key Points: The new number must be 2/3/5 times one smaller ugly number.
#             Instead of maintaining 3 sorted list, keep track of 3 pointers
#
# Run time: 264 ms 

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 5:
            return n
        ugly = [1,2,3,4,5]
        l2, l3, l5 = 2, 1, 1
        for index in xrange(6, n+1): 
            next = min(ugly[l2]*2, ugly[l3]*3, ugly[l5]*5)
            ugly.append(next)
            while ugly[l2]*2 <= next:
                l2+=1
            while ugly[l3]*3 <= next:
                l3+=1
            while ugly[l5]*5 <= next:
                l5+=1
        return next

if __name__ == "__main__":
    test = Solution()
    for testcase in xrange(1,20):
        ans = test.nthUglyNumber(testcase)
        print ans
    # print test.nthUglyNumber(10)