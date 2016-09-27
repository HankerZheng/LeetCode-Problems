# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

# Runtime: 92ms
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)>len(b):
            res = [int(ch) for ch in a]
            small = b
        else:
            res = [int(ch) for ch in b]
            small = a
        p = -1
        carry = 0
        while -p <= len(small):
            res[p] += int(small[p])+carry
            carry = 1 if res[p]>1 else 0
            res[p] = (res[p]-2) if carry else res[p]
            p-=1
        while -p<=len(res):
            res[p] += carry
            carry = 1 if res[p]>1 else 0
            res[p] = res[p]-2 if carry else res[p]
            p-=1
        if carry:
            res.insert(0,"1")
        return "".join([str(num) for num in res])

if __name__ == '__main__':
    sol = Solution()
    print sol.addBinary("111","1")



