# Given a string which contains only lowercase letters,
# remove duplicate letters so that every letter appear once and only once.
# You must make sure your result is the smallest in lexicographical order among all possible results.

# Example:
# Given "bcabc"
# Return "abc"

# Given "cbacdcbc"
# Return "acdb"

# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPopOut(char):
            if not stack:
                return False
            lastChar = stack[-1]
            if hashMap[lastChar] > 0 and lastChar > char:
                return True
            return False

        def updateHashMap(char):
            hashMap[char] -= 1

        hashMap = {}
        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1
        ansStack = []
        for curChar in s:
            while isPopOut(curChar):
                ansStack.pop(-1)
            if curChar not in ansStack:
                ansStack.append(curChar)
            updateHashMap(curChar)
        return "".join(ansStack)