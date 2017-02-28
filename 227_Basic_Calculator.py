# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# You may assume that the given expression is always valid.

# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for elem in s.strip().split("+"):
            ans += self.handlePlus(elem)
        return ans
    
    def handlePlus(self, s):
        elems = s.strip().split("-")
        ans = self.handleTD(elems[0])
        for elem in elems[1:]:
            ans -= self.handleTD(elem)
        return ans
    
    def handleTD(self, s):
        index = 0
        # parse first Number
        while index < len(s) and (s[index].isdigit() or s[index].isspace()):
            index += 1
        ans = int(s[:index])
        operatorIdx = index
        while index < len(s):
            index = operatorIdx + 1
            while index < len(s) and (s[index].isdigit() or s[index].isspace()):
                index += 1
            if s[operatorIdx] == "/":
                ans /= int(s[operatorIdx+1:index])
            elif s[operatorIdx] == "*":
                ans *= int(s[operatorIdx+1:index])
            operatorIdx = index
        return ans
            