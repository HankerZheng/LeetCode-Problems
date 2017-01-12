# Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

# Examples: 
# "123", 6 -> ["1+2+3", "1*2*3"] 
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []
# Credits:
# Special thanks to @davidtan1890 for adding this problem and creating all test cases.

# Show Company Tags
# Show Tags
# Show Similar Problems


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def backtracking(firstNumber, startIndex, target, curAns, positive):
            if startIndex == len(num):
                if target == firstNumber:
                    ans.append("".join(curAns))
                return

            maxIdx = len(num)
            if num[startIndex] == "0":
                maxIdx = startIndex + 1

            for idx in xrange(startIndex, maxIdx):
                newFirst = num[startIndex:idx+1]
                # if we add "*"
                thisFirst = int(firstNumber) * int(newFirst)
                backtracking(thisFirst, idx + 1, target, curAns + ["*", newFirst], positive)

                if positive:
                    # if we add "-"
                    backtracking(int(newFirst), idx + 1, firstNumber - target, curAns + ["-", newFirst], not positive)
                    # if we add "+"
                    backtracking(int(newFirst), idx + 1, target - firstNumber, curAns + ["+", newFirst], positive)
                else:
                    # if we add "-"
                    backtracking(int(newFirst), idx + 1, firstNumber - target, curAns + ["+", newFirst], not positive)
                    # if we add "+"
                    backtracking(int(newFirst), idx + 1, target - firstNumber, curAns + ["-", newFirst], positive)



        if not num: return []
        ans = []
        maxIdx = len(num)
        if num[0] == "0":
            maxIdx = 1
        for idx in xrange(maxIdx):
            backtracking(int(num[:idx+1]), idx+1, target, [num[:idx+1]], True)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.addOperators("00", 0)