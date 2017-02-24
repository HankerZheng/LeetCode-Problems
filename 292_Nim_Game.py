"""
If there is 0 stones left, I lost.
If there is 1 - 3 stones left, I win.

dp[i] - if there is i stones on the table, would the first picker be the winner?
dp[i] = any([not dp[i-1], not dp[i-2], not dp[i-3]])
"""
class Solution(object):
    def canWinNim_On(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:  return False
        if 1 <= n <=3: return True
        dp = [False] * 3
        dp[1] = dp[2] = True
        for numStone in xrange(3, n + 1):
            # not a || not b || not c = not( a and b and c)
            dp[numStone % 3] = not all(dp)
        return dp[n % 3]

    def canWinNim_O1(self, n):
        return bool(n & 3)
        

if __name__ == '__main__':
    sol = Solution()
    for i in xrange(40):
        print i, sol.canWinNim_On(i)