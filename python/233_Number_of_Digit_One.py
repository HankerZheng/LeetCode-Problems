# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

# Runtime: 48 ms

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        count = 0
        l, c, r, power= n/10, n%10, 0, 1
        while c or l:
            if c == 0:
                count += l * power
            elif c == 1:
                count += (r+1) + l * power
            else:
                count += (l+1) * power
            c = l%10
            l /= 10
            power *= 10
            r = n%power
        return count

if __name__ == '__main__':
    sol = Solution()
    print sol.countDigitOne(104)