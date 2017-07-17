# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        mapping = {char: i+1 for i,char in enumerate(char_set)}
        ans = 0
        for ch in s:
            ans = ans*26 + mapping[ch]
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.titleToNumber("AAA")
