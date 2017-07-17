# Given an encoded string, return it's decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square
# brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid;
# No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain
# any digits and that digits are only for those repeat numbers, k.
# For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# Subscribe to see which companies asked this question


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(start, end):
            if start == end:
                return []
            ans = []
            i = start
            para_stack = 0
            this_start = 0
            digits = ""
            while i < end:
                if para_stack == 0 and s[i].isalpha():
                    ans.append(s[i])
                elif para_stack == 0 and s[i].isdigit():
                    digits += s[i]
                elif s[i] == "[":
                    if para_stack == 0:
                        this_start = i
                    para_stack += 1
                elif s[i] == "]":
                    para_stack -= 1
                    if para_stack == 0:
                        return ans + int(digits)*helper(this_start+1, i) + helper(i+1, end)
                i += 1
            return ans
        return "".join(helper(0, len(s)))

if __name__ == '__main__':
    sol = Solution()
    print sol.decodeString("ww10[cd]")
    print sol.decodeString("3[a]2[bc]")
