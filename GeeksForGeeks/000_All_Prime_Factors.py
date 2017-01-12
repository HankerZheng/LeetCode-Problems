# Given a positive integer n, return a list of all the prime factor of n

class Solution(object):
    def primeFactors(self, n):
        if n <= 1:
            return []

        res = []
        # find all 2 prime factors
        while n & 1 == 0:
            res.append(2)
            n = n >> 1

        i = 3
        while i*i <= n:
            while n % i == 0:
                res.append(i)
                n = n/i
            i += 2
        if n > 1:
            res.append(n)
        return res


if __name__ == '__main__':
    sol = Solution()
    # print sol.primeFactors(120305129385292131) # 4.5 s
    for i in xrange(10000, 14320, 140):
        print sol.primeFactors(i)

# 102395633 - prime number    0.1s
# 660617 - prime number
# 14405693 - prime number    0.1s
# 0x7fffffff = 2147483647 - prime number    0.1s
# 818402240716273L - prime number
# 1475080053538669 = 102395633 * 14405693    2.5s