# Given two words word1 and word2, find the minimum number of steps
# required to convert word1 to word2. (each operation is counted as 1 step.)

# You have the following 3 operations permitted on a word:

# a) Insert a character
# b) Delete a character
# c) Replace a character

# Key Points: DP - http://fisherlei.blogspot.com/2012/12/leetcode-edit-distance.html
#             if it takes dp[i][j] to convert somestr1c to somestr2d, then
#             dp[i-1][j-1] -- convert somestr1 to somestr2
#             dp[i][j-1]   -- convert somestr1c to somestr2
#             dp[i-1][j]   -- convert somestr1 to somestr2c
#          1) use replace -- dp[i-1][j-1] + 1
#          2) use add     -- dp[i][j-1] + 1
#          3) use delete  -- dp[i-1][j] + 1
#          
# Runtime: 308ms

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        elif not word2:
            return len(word1)

        col, row = len(word2), len(word1)
        dp = [[0 for x in word2] for y in word1]
        for i in xrange(row):
            for j in xrange(col):
                if i==0 and j==0:
                    dp[i][j] = 0 if word1[i] == word2[j] else 1
                elif i == 0:
                    dp[i][j] = j if word1[i] in word2[:j+1] else j+1
                elif j == 0:
                    dp[i][j] = i if word2[j] in word1[:i+1] else i+1
                else:
                    if word1[i] == word2[j]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j-1]+1, dp[i][j-1]+1, dp[i-1][j]+1)
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.minDistance('intention','execution')
