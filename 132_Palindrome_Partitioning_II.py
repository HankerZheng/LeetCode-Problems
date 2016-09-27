# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

# Subscribe to see which companies asked this question

# Key Point: dp[i][j] - the min cut for string[i:j+1]
#            for every new char in the string, 
# 
# Runtime: 872 ms

class Solution(object):

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        # create the dp matrix which is a upper triangle matrix
        dp = [[0 for _ in s[i:]] for i,__ in enumerate(s)]
        # init the matrix
        for i,_ in enumerate(s):
            dp[i][0] = 1
            if i != len(s)-1:
                dp[i][1] = 1 if s[i] == s[i+1] else 0
        # build the dp matrix,
        # dp[i][j] means that s[i:i+j+1] is a palindrome string
        for j in xrange(2, len(s)):
            i = 0
            while i+j < len(s):
                if dp[i+1][j-2] == 1 and s[i] == s[i+j]:
                    dp[i][j] = 1
                i+=1
        # dpp[i] represents that the number of patirions for string[:i+1]
        dpp = [0] * len(s)
        for i,_ in enumerate(s):
            if i == 0:
                dpp[i] = 1
            else:
                this_min = 1+dpp[i-1]
                line = 0
                while line<=i:
                    if dp[line][i-line] == 1:
                        this_min = min(this_min, dpp[line-1]+1)
                    line+=1
                dpp[i] = this_min
        return dpp[-1]-1





    def minCut_ON3(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        dp = [[1 for __ in s] for _ in s]
        for k in xrange(1, len(s)):
            i = 0
            while i+k<len(s):
                if k == 1:
                    dp[i][i+k] = 1 if s[i]==s[i+k] else 2
                else:
                    if s[i] == s[i+k] and dp[i+1][i+k-1]==1:
                        cross_match = 1
                    else:
                        cross_match = dp[i+1][i+k-1]+2
                    normal_match = cross_match
                    for j in xrange(1, k+1):
                        normal_match = min(normal_match, dp[i][i+k-j]+dp[i+k-j+1][i+k])
                    dp[i][i+k] = min(cross_match, normal_match)
                i+=1
        return dp[0][-1]-1

if __name__ == '__main__':
    sol = Solution()
    print sol.minCut("") #-1
    print sol.minCut("1") #0
    print sol.minCut("121") #0
    print sol.minCut("123") #2
    print sol.minCut("1213") #1
    print sol.minCut("aab") #1
    print sol.minCut("abcb") #1
    print sol.minCut("cbbbcc") #1
    print sol.minCut("1bc1") #3
    print sol.minCut("abadcd") #1