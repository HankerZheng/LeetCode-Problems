# Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

# Note:
# Both the string's length and k will not exceed 104.

# Example 1:

# Input:
# s = "ABAB", k = 2

# Output:
# 4

# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input:
# s = "AABABBA", k = 1

# Output:
# 4

# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        majorCnt = 0
        maxLength = 0
        windowDict = {}
        startIdx = 0
        for endIdx in xrange(len(s)):
            self.windowAdd(windowDict, s[endIdx])
            majorCnt = max(majorCnt, windowDict.get(s[endIdx], 0))
            while endIdx - startIdx - majorCnt + 1 > k:
                self.windowDelete(windowDict,s[startIdx])
                startIdx += 1
            maxLength = max(maxLength, endIdx - startIdx + 1)
        return maxLength
    
    def windowAdd(self, windowDict, character):
        windowDict[character] = windowDict.get(character, 0) + 1
        
    def windowDelete(self, windowDict, character):
        windowDict[character] -= 1
        