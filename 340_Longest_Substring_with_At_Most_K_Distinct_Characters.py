# Given a string, find the length of the longest substring T that contains at most k distinct characters.

# For example, Given s = “eceba” and k = 2,

# T is "ece" which its length is 3.

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        tobeRemove = 0
        window = {}
        for i, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if len(window) <= k:
                ans = max(ans, i - tobeRemove + 1)
            while tobeRemove < len(s) and len(window) > k:
                window[s[tobeRemove]] -= 1
                if window[s[tobeRemove]] == 0:
                    window.pop(s[tobeRemove])
                tobeRemove += 1
        return ans
