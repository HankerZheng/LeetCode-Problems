# 402. Remove K Digits   QuestionEditorial Solution  My Submissions
# Total Accepted: 7654
# Total Submissions: 29945
# Difficulty: Medium
# Contributors: Admin
# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
# Subscribe to see which companies asked this question


# NON-DECREASING STACK
#       To make the digit smallest, we have to make sure the digit in that num
#       is in NON-DECREASING order.
#       Therefore, we could use an NON-DECREASING stack to simulate the process
# 
#       Careful to handle leading zeros
#       Careful to handle when count < k


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        def appendNewDigit(stack, removeNum, idx):
            while stack and removeNum and stack[-1] > num[idx]:
                stack.pop(-1)
                removeNum -= 1
            stack.append(num[idx])
            return removeNum
            
        def removeLeadingZero(num):
            if not num:
                return "0"
            startIdx = 0
            while startIdx < len(num) - 1 and num[startIdx] == "0":
                startIdx += 1
            return num[startIdx:]
        
        idx = 0
        removeNum = k
        stack = []
        while idx < len(num):
            removeNum = appendNewDigit(stack, removeNum, idx)
            idx += 1
        ans = "".join(stack)
        length = len(ans)
        return removeLeadingZero(ans[:length - removeNum])
            