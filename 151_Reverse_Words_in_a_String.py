# Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.

# click to show clarification.

# Subscribe to see which companies asked this question

# Runtime: 32ms
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        oops = s.split()
        return " ".join(oops[::-1])

if __name__ == '__main__':
    sol = Solution()
    print sol.reverseWords("as a man")