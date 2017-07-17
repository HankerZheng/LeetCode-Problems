# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

# For example:

# Given "aacecaaa", return "aaacecaaa".

# Given "abcd", return "dcbabcd".

# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases. Thanks to @Freezen for additional test cases

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        prefixList = self.getPrefixList(s)
        # print prefixList
        addString = s[prefixList[-1]:][::-1]
        return addString + s
    
    def getPrefixList(self, s):
        revS = s + "#" + s[::-1]
        revIdx = 1
        idx = 0
        lps = [0] * len(revS)
        while revIdx < len(revS):
            while revIdx < len(revS) and revS[revIdx] == revS[idx]:
                lps[revIdx] = idx + 1
                revIdx += 1
                idx += 1
            if revIdx < len(revS) and idx != 0:
                idx = lps[idx - 1]
            else:
                revIdx += 1
        return lps
            
        