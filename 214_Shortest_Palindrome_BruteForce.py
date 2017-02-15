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
        length = len(s)
        left, right = (length-1) / 2,  length / 2
        flag = right - left
        while left >= 0:
            if self.checkPalindrome(s, left, right):
                addString = s[right + left + 1:][::-1]
                return addString + s
            left -= (1 - flag)
            right -= flag
            flag = right - left
        return s[::-1] + s
    
    def checkPalindrome(self, s, left, right):
        while left >= 0:
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                return False
        return True