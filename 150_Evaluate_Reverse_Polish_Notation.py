# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
# Subscribe to see which companies asked this question

# Runtime: 56ms

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operator_set = "+-*/"
        stack = []
        for token in tokens:
            if token in operator_set:
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                if token == '+':
                    stack.append(num1+num2)
                elif token == '-':
                    stack.append(num1-num2)
                elif token == '*':
                    stack.append(num1*num2)
                elif token == '/':
                    stack.append(int(float(num1)/num2))
            else:
                stack.append(int(token))
        return stack[-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])