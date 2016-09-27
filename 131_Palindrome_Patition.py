# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return

# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
# Subscribe to see which companies asked this question


# Runtime: 164 ms

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def helper(ans, line):
            if line == len(s):
                res.append(ans)
                return
            for i, value in enumerate(dp[line]):
                if value == 1:
                    helper(ans+[s[line:line+i+1]], line+i+1)

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
        # backtracking the res
        res = []
        helper([], 0)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.partition("abcacb")