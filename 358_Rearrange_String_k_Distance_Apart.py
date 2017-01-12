# Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance k from each other.

# All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

# Example 1:
# str = "aabbcc", k = 3

# Result: "abcabc"

# The same letters are at least distance 3 from each other.
# Example 2:
# str = "aaabc", k = 3 

# Answer: ""

# It is not possible to rearrange the string.
# Example 3:
# str = "aaadbbcc", k = 2

# Answer: "abacabcd"

# Another possible answer is: "abcabcda"

# The same letters are at least distance 2 from each other.


import heapq
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        def findMaxAvail(window, hashmap):
            maxCnt = 0
            ans = ""
            for char, count in hashmap.items():
                if char not in window and count > maxCnt:
                    maxCnt = count
                    ans = char
            return ans
        
        if len(str) <= 1:   return str
        if k == 0:  return str
        hashmap = {}
        for char in str:
            hashmap[char] = hashmap.get(char, 0) + 1
        if k > len(hashmap):
            return ""
        ans = []
        window = set()
        toDel = 0
        while hashmap:
            if len(window) == k:
                window.remove(ans[toDel])
                toDel += 1
            thisChar = findMaxAvail(window, hashmap)
            if not thisChar:
                return ""
            ans.append(thisChar)
            window.add(thisChar)
            hashmap[thisChar] -= 1
            hashmap[thisChar] == 0 and hashmap.pop(thisChar)
        return "".join(ans)