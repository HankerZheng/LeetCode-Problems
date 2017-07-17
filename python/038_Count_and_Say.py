# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.


# Key Points: Stack
#             Store the same number into the stack and count
#
# Run time: 60 ms

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def getNext(current):
            count, flag, length = 0, current[0], len(current)
            ans = ""
            for char in current:
                if char == flag:
                    count += 1
                else:
                    ans+=str(count)+flag
                    flag = char
                    count = 1
            ans+=str(count)+flag
            return ans

        if n == 0:
            return []
        current = "1"
        for i in xrange(n-1):
            current = getNext(current)
        return current

if __name__ == '__main__':
    sol = Solution()
    print sol.countAndSay(50)