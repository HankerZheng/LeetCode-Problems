# The gray code is a binary numeral system where two
# successive values differ in only one bit.

# Given a non-negative integer n representing the total
# number of bits in the code, print the sequence of gray code.
# A gray code sequence must begin with 0.

# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# Note:
# For a given n, a gray code sequence is not uniquely defined.

# For example, [0,2,3,1] is also a valid gray code sequence according
# to the above definition.

# For now, the judge is able to judge based on one instance of gray
# code sequence. Sorry about that.

# Key Points: Backtracking
# Runtime 68/100ms

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def flip_low(ans, length, flag):
            if length == n:
                res.append(ans)
                return
            if flag:
                flip_low(ans*2,length+1, flag)
                flip_low(ans*2+1,length+1, not flag)
            else:
                flip_low(ans*2+1,length+1, not flag)
                flip_low(ans*2,length+1, flag)
        if n==0:
            return [0]
        res = []
        flip_low(0, 0, True)
        return res

    def grayCode_String(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def flip_low(ans, length, flag):
            if length == n:
                res.append(ans)
                return
            if flag:
                flip_low(ans+"0",length+1, flag)
                flip_low(ans+"1",length+1, not flag)
            else:
                flip_low(ans+"1",length+1, not flag)
                flip_low(ans+"0",length+1, flag)
        if n==0:
            return [0]
        res = []
        flip_low("", 0, True)
        return [int(ans, 2) for ans in res]

if __name__ == '__main__':
    sol = Solution()
    print sol.grayCode(0)
    print sol.grayCode(1)
    print sol.grayCode(2)
    print sol.grayCode(3)