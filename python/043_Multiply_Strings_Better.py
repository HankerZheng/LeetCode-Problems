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
        for i, ch1 in enumerate(num1):
            for j, ch2 in enumerate(num2):
                if (i+j)>=len(res):
                    res.append(int(ch1)*int(ch2))
                else:
                    res[i+j] += int(ch1)*int(ch2)
        for i in xrange(len(res)-1,0,-1):
            res[i-1]+=res[i]/10
            res[i] = str(res[i]%10)
        res[0] = str(res[0])
        start = 0
        while res[start]=="0":
            start+=1
        return "".join(res[start:])




if __name__ == '__main__':
    sol = Solution()
    # print sol.multiply("12","0")
    # print sol.multiply("12213","2")
    # print sol.multiply("12","1")
    # print sol.multiply("12","121323")
    # print sol.multiply("122313213213","12312321323213")
    # print sol.multiply("408","5")
    # print sol.multiply("99","9")
    print sol.multiply("11","123")