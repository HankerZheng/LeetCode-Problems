# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# For example,
# Given the following words in dictionary,

# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".

# Note:
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

from collections import defaultdict

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:return []
        # init the set and dict
        dependentPair = defaultdict(set)
        curBase = words[0]
        wordSet = set(curBase)
        # create the dependentPair
        for word in words[1:]:
            i = 0
            while i < len(word) and i < len(curBase) and curBase[i] == word[i]:
                wordSet.add(word[i])
                i += 1
            if i == len(word) and i < len(curBase):
                return ""
            if i < len(word) and i < len(curBase):
                dependentPair[curBase[i]].add(word[i])
                dependentPair[word[i]] = dependentPair.get(word[i], set())
            curBase = word
            while i < len(word):
                wordSet.add(word[i])
                i += 1
        # Topological Sort in dependentPair
        visited = set()
        ans = []
        while dependentPair:
            flag = 0
            for char, childSet in dependentPair.items():
                if childSet <= visited:
                    ans.insert(0, char)
                    dependentPair.pop(char)
                    visited.add(char)
                    flag = 1
                    break
            if not flag:    return ""
        ans += [char for char in wordSet - visited]
        return "".join(ans)
        