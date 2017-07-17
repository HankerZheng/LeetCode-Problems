# Given two numbers represented as strings, return multiplication of the numbers as a string.

# Note:
# The numbers can be arbitrarily large and are non-negative.
# Converting the input string to integer is NOT allowed.
# You should NOT use internal library such as BigInteger.
# Subscribe to see which companies asked this question

# Runtime: 464ms

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        res = []
        len1, len2 = len(num1), len(num2)
        carry = 0
        for i in xrange(len1+len2):
            thissum = 0
            for k in xrange(i+1):
                if k<len1 and i-k<len2:
                    thissum += int(num1[len1-k-1])*int(num2[len2-(i-k)-1])
            thissum+=carry
            carry = thissum/10
            res.insert(0, str(thissum%10))
        start = 0
        while res[start] == "0":
            start+=1
        return "".join(res[start:])

if __name__ == '__main__':
    sol = Solution()
    print sol.multiply("12","0")
    print sol.multiply("12213","2")
    print sol.multiply("12","1")
    print sol.multiply("12","121323")
    print sol.multiply("122313213213","12312321323213")
    print sol.multiply("408","5")