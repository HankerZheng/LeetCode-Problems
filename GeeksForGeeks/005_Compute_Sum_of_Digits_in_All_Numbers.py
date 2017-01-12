# Reference: http://www.geeksforgeeks.org/count-sum-of-digits-in-numbers-from-1-to-n/

# Given a number x, find sum of digits in all numbers from 1 to n.
# Examples:
# 
# Input: n = 5
# Output: Sum of digits in numbers from 1 to 5 = 15
# 
# Input: n = 12
# Output: Sum of digits in numbers from 1 to 12 = 51
# 
# Input: n = 328
# Output: Sum of digits in numbers from 1 to 328 = 3241

# My Thoughts:
#   f(999) = f(9) * 100 * 3 = 300 * f(9)
#   f(10^k - 1) = f(9) * 10^(k-1) * k = k*10^(k-1)*45
#   f(32768) = f(30000) + 3 * 2768 + f(2768)
#            = f(9999) * 3 + 3 + 3 * 2768 + f(2768)
#            = 4*1000*45 * 3 + 3 + 3 * 2768 + f(2768)

def sumOfDigits(n):
    def powerOf10minus1(k):
        """
        return the ans for 10**k - 1
        when k == 1, return the answer of 9 = 10**1 - 1
        when k == 2, return the answer of 99 == 10**2 - 1
        """
        return k * (10 ** (k - 1)) * 45

    def getFirstDigit(n):
        """
        return the firstDigit, the remainder, and digit Cnt
        
        >>> getFirstDigit(12)
        (1, 2, 2)
        >>> getFirstDigit(234)
        (2, 34, 3)
        """
        cnt = 1
        multiple = 1
        while n >= 10 * multiple:
            cnt += 1
            multiple *= 10
        firstDigit, rem = divmod(n, 10 ** (cnt - 1))
        return firstDigit, rem, cnt

    def helper(n):
        if n < 10:
            # the input has only one digit
            return (1 + n) * n / 2
        firstDigit, rem, cnt = getFirstDigit(n)
        if 10**cnt == n + 1:
            # input is in the form of all 9's (9, 99, 999, 9999, ...)
            return powerOf10minus1(cnt)
        delta = firstDigit * powerOf10minus1(cnt - 1)
        delta += helper(firstDigit - 1) * (10**(cnt-1)) 
        delta += firstDigit * (rem + 1)
        return delta + helper(rem)

    return helper(n)


def sumOfDigits_Naive(n):
    def digitSum(i):
        thisSum = 0
        while i:
            i, digit = divmod(i, 10)
            thisSum += digit
        return thisSum

    prev = 0
    for i in xrange(1, n + 1):
        ans = prev + digitSum(i)
        prev = ans
    return ans

if __name__ == '__main__':
    import random
    for i in xrange(25):
        i = random.randint(100, 400)
        ans = sumOfDigits(i)
        print "f(%d) =" % i, ans, ans == sumOfDigits_Naive(i)