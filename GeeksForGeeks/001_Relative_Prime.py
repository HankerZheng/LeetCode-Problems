# Given a positive integer `n`, return the count of all number that 
# is smaller than `n` and relatively prime to `n`.
# 
# `a` is relatively prime to `b`, means GCD(a, b) = 1

class Solution(object):
    def relativePrimeCount(self, n):
        def findPrimeFactor(n):
            if n & 1 == 0:
                yield 2
                while n & 1 == 0:
                    n = n >> 1
            i = 3
            while i* i <= n:
                if n % i == 0:
                    yield i
                    while n % i == 0:
                        n = n / i
                i += 2
            if n > 1:
                yield n
            return

        if n <= 0: return -1
        if n == 1: return 0
        res = n - 1
        for primeFactor in findPrimeFactor(n):
            res -= res / primeFactor
        return res

    def relativePrimeCount_BruteForce(self, n):
        def gcd(a, b):
            while a and b:
                smaller, larger = min(a,b), max(a,b)
                a, b = smaller, larger % smaller
            return max(a,b)

        if n <= 0:
            return -1
        res = 0
        for i in xrange(1, n):
            if gcd(i, n) == 1:
                res += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    for i in xrange(1000):
        assert sol.relativePrimeCount_BruteForce(i) == sol.relativePrimeCount(i)
    # print sol.relativePrimeCount(6)
    # print sol.relativePrimeCount_BruteForce(6)

