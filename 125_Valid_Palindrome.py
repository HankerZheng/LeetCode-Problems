# Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.

# Subscribe to see which companies asked this question

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s)-1
        while start<end:
            if not 'A'<=s[start]<='Z' and not 'a'<=s[start]<='z' and not '0'<=s[start]<='9':
                start+=1
            elif not 'A'<=s[end]<='Z' and not 'a'<=s[end]<='z' and not '0'<=s[end]<='9':
                end-=1
            else:
                start_ch = s[start].lower()
                end_ch = s[end].lower()
                if start_ch == end_ch:
                    start+=1
                    end-=1
                else:
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.isPalindrome("`l;`` 1o1 ??;l`")