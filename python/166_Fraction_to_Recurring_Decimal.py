# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# For example,

# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Show Hint 

# Runtime: 32 ms
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return "NaN"
        if numerator*denominator < 0:
            negative_flag = 1
        else:
            negative_flag = 0
        # do the integer part first
        this_numerator = abs(numerator)
        abs_denominator = abs(denominator)
        int_part = this_numerator / abs_denominator
        res = [str(int_part)]
        # do the decimal part
        posi = 2 # 0 is for int_part, 1 is for "."
        remainder_record = {}
        this_numerator = this_numerator % abs_denominator
        if this_numerator != 0:
            res.append('.')

        while this_numerator:
            # check whether this_numerator appears before
            if remainder_record.get(this_numerator, None) is None:
                # not appear, store its position
                remainder_record[this_numerator] = posi
            else:
                # does appear, finish the division, find the repeating part
                res.insert(remainder_record[this_numerator], "(")
                res.append(")")
                break
            # do the division
            this_numerator *= 10
            res.append(str(this_numerator/abs_denominator))
            this_numerator %= abs_denominator
            posi += 1

        res = "".join(res)
        if negative_flag:
            return "-"+res
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.fractionToDecimal(1,6)
