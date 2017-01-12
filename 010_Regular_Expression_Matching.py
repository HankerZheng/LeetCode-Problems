# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") => false
# isMatch("aa","aa") => true
# isMatch("aaa","aa") => false
# isMatch("aa", "a*") => true
# isMatch("aa", ".*") => true
# isMatch("ab", ".*") => true
# isMatch("aab", "c*a*b") => true
# Subscribe to see which companies asked this question



# Key Points: Dynamic Programming
# 
# dp[i][j] - first i characters in s matches with the first j characters in p
# Initialization:
#       dp[0][0] = True  -  empty string matches with empty string
#       dp[0][j] = j&1 and dp[0][j-1] and p[j] == '*'  -  ".*x*c*" matches with empty string
#       dp[i][0] = False  -  empty string p match with nothing
# Iteration:
#       if p[i] == '.':     dp[i+1][j+1] = dp[i][j]
#     elif p[i] == '*':     dp[i+1][j+1] = dp[i+1][j-1] or                     (zero match)
#                                          dp[i][j+1] and s[i] == s[i-1]       (one or more match)
#                 else:     dp[i+1][j+1] = dp[i][j] and (s[i] == p[j])

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lenS = len(s)
        lenP = len(p)
        dp = [[False for j in xrange(lenP+1)] for i in xrange(2)]
        
        for i in xrange(lenS+1):
            for j in xrange(lenP+1):
                if i == 0 and j == 0:
                    # empty string can matches with empty pattern
                    dp[i&1][j] = True
                elif i == 0:
                    # empty string matches with pattern "a*b*c*...."
                    dp[i&1][j] = (j&1==0) and p[j-1] == "*" and dp[i&1][j-2]
                elif j == 0:
                    # non-empty string doesn't match with an empty pattern
                    dp[i&1][j] = False
                elif p[j-1] == "*":
                    # current pattern is "*"
                    # if "*" matches zero
                    matchZero = dp[i&1][j-2]
                    # if "*" matches something
                    matchSomething = dp[(i-1)&1][j] and (s[i-1] == p[j-2] or p[j-2] == ".")
                    dp[i&1][j] = matchZero or matchSomething
                else:
                    dp[i&1][j] = dp[(i-1)&1][j-1] and (s[i-1] == p[j-1] or p[j-1] == ".")
                    
        return dp[i&1][-1]

    def isMatch_noSpaceOptimization(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in xrange(len(p)+1)] for __ in xrange(len(s)+1) ]
        dp[0][0] = True
        for j, ch_p in enumerate(p):
            dp[0][j+1] = (j&1 != 0) and dp[0][j-1] and (p[j] == '*')
        for i, ch_s in enumerate(s):
            for j, ch_p in enumerate(p):
                if ch_p == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif ch_p == '*':
                    if j != 0:
                        dp[i+1][j+1] = dp[i+1][j-1] or (dp[i][j+1] and (s[i] == p[j-1] or p[j-1] == '.'))
                else:
                    dp[i+1][j+1] = dp[i][j] and (s[i] == p[j])
        # for line in dp:
        #     print line
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    # print sol.isMatch('abc', 'a*c*b*d*c*')
    print sol.isMatch('aaa', '.*')
