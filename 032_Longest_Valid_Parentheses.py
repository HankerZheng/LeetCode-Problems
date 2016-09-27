# Difficulty: Hard
# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
# 
# For "(()", the longest valid parentheses substring is "()",
# which has length = 2.
# 
# Another example is ")()())", where the longest valid parentheses
# substring is "()()", which has length = 4.


# Key Points: DP, Stack
#             When meet a left parenthese, push current length into stack.
#             When meet a right parenthese, pop one length from stack and add
#             2 to that length.
#             If current length larger than max-length, update max-lenght             
#
# Run Time: 76 ms

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_length, max_length = 0, 0
        stack=[]
        for para in s:
            if para == "(":
                stack.append(c_length)
                c_length = 0
            else:
                if stack:
                    c_length += (2+stack.pop(-1))
                    if c_length > max_length:
                        max_length = c_length
                else:
                    # clear c_length if it is a single right paranthese
                    c_length = 0
        return max_length

if __name__ =="__main__":
    test = Solution()
    query = [
        "((((((", #0
        "", #0
        "(((()(((", #2
        "(())()(()", #6
        "))))()()((()()()()(", #8
        ")()())()()(" #4
    ]
    for q in query:
        ans = test.longestValidParentheses(q)
        print ans


