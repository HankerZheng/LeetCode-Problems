# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "*") -> true
# isMatch("aa", "a*") -> true
# isMatch("ab", "?*") -> true
# isMatch("aab", "c*a*b") -> false
# Subscribe to see which companies asked this question


# Key Points: Compare the pattern one by one.
#             Normal match is simple.
# 
#             [*CANNOT DOING THIS WAY FAR TOO SLOW*]
#             The main point of asterisk match is that
#             at begining, '*' matches 0 item, if the latter fails,
#             make '*' matches one more item.
# 
#             [*DP SOLUTION*]
#             dp[sp][pp] == dp[sp-1][pp-1] if (s[sp]==p[pp-1] or p[pp]=='?') and p[pp]!='*'
#             dp[sp][pp] == dp[sp][pp-1] || dp[sp-1][pp] if p[pp] == '*'
#             A '*' could match nothing, thst is dp[sp][pp] == dp[sp][pp-1]
#                      or match something, that is dp[sp][pp] == dp[sp-1][pp-1]||dp[sp-2][pp-1]||dp[sp-3][pp-1]||...||dp[0][pp-1]
#                                                             == dp[sp-1][pp]
# 
#             [*GREEDY*]
#             Divide the p string into several parts according to '*'
#             Match the parts with string s. For those parts in the middles and gets multiple matches, match the most former one.
#             That is,  'abcabcabcdef' and 'ab*ca*bc*f', the first 'ca' must match the first 'ca', the first 'bc' must match the
#             first 'bc'
# 
# Runtime: 144 ms

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        parts = [item for item in p.split('*') if item]
        if p[0]!='*':
            first_match()
        if p[-1]!='*'

if __name__ == '__main__':
    sol = Solution()
    print sol.isMatch('ab','*a')
    print sol.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb","b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a")