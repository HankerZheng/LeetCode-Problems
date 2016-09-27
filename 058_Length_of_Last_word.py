# Given a string s consists of upper/lower-case alphabets and
# empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example, 
# Given s = "Hello World",
# return 5.

# Runtime: 56ms

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last, pointer = len(s)-1, len(s)-1
        while last>=0 and s[last] == " ":
            last -=1
            pointer-=1
        while pointer>=0 and s[pointer] !=" ":
            pointer -=1
        return last - pointer

if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLastWord("  ")
    print sol.lengthOfLastWord("ab  ")
    print sol.lengthOfLastWord(" ab ")
    print sol.lengthOfLastWord(" aa ab ")
    print sol.lengthOfLastWord(" aa ab")
