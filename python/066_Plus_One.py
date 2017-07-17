# Given a non-negative number represented as an array of digits,
# plus one to the number.

# The digits are stored such that the most significant digit is at
# the head of the list.

# Subscribe to see which companies asked this question

# Key Points: Same as Multiply Strings
# Runtime: 68 ms

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = list(digits)
        res[-1] +=1
        for i in xrange(len(digits)-1, 0, -1):
            if res[i]>9:
                res[i] %= 10
                res[i-1] +=1
            else:
                break
        if res[0] >9:
            res[0] %= 10
            res.insert(0, 1)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.plusOne([9])