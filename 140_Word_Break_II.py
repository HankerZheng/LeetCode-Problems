# Given a string s and a dictionary of words dict, add spaces in s to
# construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].


# Runtime: 112 ms
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def helper(i, ans):
            if i == len(s):
                res.append(" ".join(ans))
            for word in wordDict:
                length = len(word)
                if (i+length) <= len(s) and s[i:i+length] == word and dp[i+length-1]:
                    helper(i+length, ans+[word])
        res = []
        dp = [0] * len(s)
        for i,char in enumerate(s):
            for word in wordDict:
                length = len(word)
                if i >= length-1 and s[i-length+1:i+1]==word and (dp[i-length] == 1 or i-length+1 == 0):
                    dp[i] = 1
                    break
        if dp[-1] == 0:
            return []
        helper(0, [])
        return res

if __name__ == '__main__':
    sol = Solution()