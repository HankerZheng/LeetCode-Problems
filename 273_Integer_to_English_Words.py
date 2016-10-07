# Convert a non-negative integer to its english words representation.
# Given input is guaranteed to be less than 231 - 1.

# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Show Hint 


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def threeDigits(num):
            ans = []
            if num >= 100:
                ans.append(English[num/100])
                ans.append(English[100])
            this_num = num % 100
            if this_num <= 20:
                ans.append(English[this_num])
            elif this_num % 10:
                ans.append(English[this_num - this_num % 10])
                ans.append(English[this_num % 10])
            else:
                ans.append(English[this_num])
            if len(ans) > 1 and ans[-1] == "Zero":
                ans.pop(-1)
            return ans
        
        English = { 0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
                    6: "Six", 7: "Seven",8: "Eight", 9: "Nine", 10: "Ten",
                    11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
                    15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
                    19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
                    60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "Hundred"}
        if num == 0:
            return "Zero"
        ans = []
        if num / 1000000000:
            ans += threeDigits(num/1000000000)
            ans.append("Billion")
        num -= num /1000000000 * 1000000000
        if num / 1000000:
            ans += threeDigits(num/1000000)
            ans.append("Million")
        num -= num /1000000 * 1000000
        if num / 1000:
            ans += threeDigits(num/1000)
            ans.append("Thousand")
        num -= num / 1000 * 1000
        if num:
            ans += threeDigits(num)
        return " ".join(ans)

if __name__ == '__main__':
    sol = Solution()
    # for i in xrange(12):
    #     import random
    #     test = random.randrange(0, 1000000000)
    #     print test, sol.numberToWords(test)
    # print 100000000, sol.numberToWords(100000000)
    # print 100010000, sol.numberToWords(100010000)
    # print 100000100, sol.numberToWords(100000100)
    print 2116421957, sol.numberToWords(2116421957)

