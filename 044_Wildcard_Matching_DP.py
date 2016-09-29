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
#             If there is an '*' match, match recursively
# Runtime: 144 ms

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # length of the string
        sl, pl = len(s), len(p)
        # pointer of two string
        sp, pp = 0, 0
        # last normal match, including '?' match
        last_s, last_p = 0,-1
        while sp < sl:
            if pp<pl and (s[sp] == p[pp] or p[pp]=='?') and p[pp]!='*':
                # normal match or '?' match
                sp+=1
                pp+=1
            elif pp<pl and p[pp] == '*':
                # encounter '*', set last to last normal match
                # This condition would make pp skip all the '*' flag
                last_s = sp
                last_p = pp
                pp+=1
            elif last_p >= 0:
                # In the middle of '*' match
                sp = last_s + 1
                last_s +=1
                pp = last_p
            else:
                return False
        # string s has run out
        # check whether the remainder of string p is only '*'
        while pp<pl and p[pp]=='*':
            pp+=1
        return pp == pl

if __name__ == '__main__':
    sol = Solution()
    print sol.isMatch('a','aa')
    print sol.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb","b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a")