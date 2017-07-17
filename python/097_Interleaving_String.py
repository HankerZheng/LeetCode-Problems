# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",

# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.

# Subscribe to see which companies asked this question

# Key Points: DP, subproblem - first i-th of s1 and first j-th of s2
#             match the first (i+j+1)-th of s3
#             dp[i][j] == dp[i-1][j] if s3[i+j+1]==s1[i]
#                      == dp[i][j-1] if s3[i+j+1]==s2[i]
# Runtime: 96 ms

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1:
            return s2==s3
        if not s2:
            return s1==s3
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False for _ in s2]
        old_dp = dp
        for i, ch1 in enumerate(s1):
            for j, ch2 in enumerate(s2):
                if i == 0 and j == 0:
                    dp[j] = True if ch1+ch2==s3[:2] or ch2+ch1==s3[:2] else False
                elif i == 0 :
                    dp[j] = (dp[j-1] if ch2==s3[i+j+1] else False) or (s2[:j+1]==s3[:j+1] if ch1[i]==s3[i+j+1] else False)
                elif j == 0 :
                    dp[j] = (old_dp[j] if ch1==s3[i+j+1] else False) or (s1[:i+1]==s3[:i+1] if ch2[j]==s3[i+j+1] else False)
                else:
                    dp[j] = (dp[j-1] if ch2==s3[i+j+1] else False) or (old_dp[j] if ch1==s3[i+j+1] else False)
            old_dp = dp
        return old_dp[-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
    print sol.isInterleave('', '', '')
    print sol.isInterleave('a', 'b', 'ab')
    print sol.isInterleave('a', 'b', 'aba')