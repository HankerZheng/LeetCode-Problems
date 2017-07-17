# Given a string s and a dictionary of words dict, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

# Subscribe to see which companies asked this question


# Runtime: 59 ms


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        matchPoint = {0}
        visited = set()
        while matchPoint:
            thisMatchPoint = matchPoint.pop()
            visited.add(thisMatchPoint)
            for word in wordDict:
                endPoint =  thisMatchPoint + len(word)
                if endPoint <= len(s) and word == s[thisMatchPoint: endPoint] and endPoint not in visited:
                    if endPoint == len(s):
                        return True
                    matchPoint.add(endPoint)
        return False

    def wordBreak_LengthOptimized(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        lengthSet = set([len(word) for word in wordDict])
        wordSet = set(wordDict)
        matchPoint = {0}
        
        while matchPoint:
            startPoint = matchPoint.pop()
            for length in lengthSet:
                endPoint = startPoint + length
                thisString = s[startPoint: endPoint]
                if thisString in wordSet:
                    matchPoint.add(endPoint)
                    if endPoint == len(s):
                        return True
        return False