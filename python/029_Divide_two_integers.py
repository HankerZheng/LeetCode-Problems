"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

Subscribe to see which companies asked this question
"""

# Key Points: Binary Search.
#             Search start from the most significant bit of result.
#             Use '<<' in place of '*'.
#
# Special Test Case: 1) Sign of the number of input. (12/-1, -12/1, -12/-1)
#                    2) divisible and indivisible. (12/7, 12/4, 12/5)
#                    2) Answer exceed INT range. (-2147483648 / -1)
#
# Run time: 72 ms


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1

        sign_flag = 1
        if dividend < 0:
            sign_flag = -sign_flag
            dividend = -dividend
        if divisor < 0:
            sign_flag = -sign_flag
            divisor = -divisor

        res = 0
        dividend_tmp = dividend
        # Outer loop ends when dividend_tmp cannt be substracted
        while dividend_tmp >= divisor:
            compare = divisor
            res_tmp = 1
            # Inner loop ends when increasing compare is over than ...
            while dividend_tmp >= compare:
                compare = compare << 1
                res_tmp = res_tmp << 1
            dividend_tmp = dividend_tmp - (compare>>1)
            res = res + (res_tmp>>1)

        res = res if sign_flag > 0 else -res
        if res > 2147483647:
            return 2147483647
        elif res < (-2147483648):
            return -2147483648
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.divide(-2147483648,-1)