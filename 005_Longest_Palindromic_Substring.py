# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000, and there
# exists one unique longest palindromic substring.


# Key Points: DP, dp[i][j] represents whether string[i:j+1] is Palindorme
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        start, end = 0,0
        dp = [[False for _ in s] for __ in s]
        for k in xrange(len(s)):
            i = 0
            flag = 0
            miss = 0
            while i+k<len(s):
                if k == 0:
                    dp[i][i+k]=True
                elif k == 1:
                    dp[i][i+k] = s[i]==s[i+k]
                else:
                    dp[i][i+k] = dp[i+1][i+k-1] if s[i]==s[i+k] else False
                if dp[i][i+k]:
                    start, end = i, i+k
                    flag = 1
                i+=1
            if flag == 0:
                miss +=1
            if miss ==2:
                break


        return s[start:end+1]

if __name__ == '__main__':
    sol = Solution()
    print sol.longestPalindrome("12")
