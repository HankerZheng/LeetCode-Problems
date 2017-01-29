# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".

# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".

# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

from collections import deque, Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def updateWindow(idx):
            windowInfo[s[idx]] = windowInfo.get(s[idx], 0) + 1
            windowIdx.append(idx)
            firstChar = s[windowIdx[0]]
            while windowInfo[firstChar] > targetInfo[firstChar]:
                popChar = s[windowIdx.popleft()]
                windowInfo[popChar] -= 1
                firstChar = s[windowIdx[0]]
            
        def checkComplete():
            if len(targetInfo) != len(windowInfo):
                return False
            for key in targetInfo:
                if targetInfo[key] > windowInfo.get(key, 0):
                    return False
            return True
            
        ans = s + t
        targetInfo = Counter(t)
        windowInfo = dict()
        windowIdx = deque()
        for i, char in enumerate(s):
            if char not in targetInfo:
                continue
            updateWindow(i)
            if checkComplete() and len(ans) > windowIdx[-1] - windowIdx[0] + 1:
                ans = s[windowIdx[0]: windowIdx[-1]+1]
        return ans if len(ans) <= len(s) else ""
            