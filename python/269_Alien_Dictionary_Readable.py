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

from collections import defaultdict, deque

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return []
        directedGraph = self.getGraph(words)
        sortRes = self.topologicalSort(directedGraph)
        if len(sortRes) == len(directedGraph):
            return "".join(sortRes)
        return ""
    
    def getGraph(self, words):
        prevWord = words[0]
        charSet = {char for char in prevWord}
        directedGraph = defaultdict(set)
        for thisWord in words[1:]:
            smaller, larger = self.getOrder(prevWord, thisWord)
            if not smaller and not larger:
                return {}
            elif smaller != larger:
                directedGraph[smaller].add(larger)
            for char in thisWord:
                charSet.add(char)
            prevWord = thisWord
        for char in charSet:
            if char not in directedGraph:
                directedGraph[char] = directedGraph.get(char, set())
        return directedGraph
    
    def topologicalSort(self, directedGraph):
        degreeDict = {}
        for src, dests in directedGraph.items():
            degreeDict[src] = degreeDict.get(src, 0)
            for dest in dests:
                degreeDict[dest] = degreeDict.get(dest, 0) + 1
        zeroDegree = deque([node for node in degreeDict if degreeDict[node]==0])
            
        sortRes = []
        while zeroDegree:
            thisNode = zeroDegree.popleft()
            sortRes.append(thisNode)
            for nei in directedGraph[thisNode]:
                degreeDict[nei] -= 1
                if degreeDict[nei] == 0:
                    zeroDegree.append(nei)
        return sortRes
    
    def getOrder(self, word1, word2):
        minLength = min(len(word1), len(word2))
        index = 0
        while index < minLength and word1[index] == word2[index]:
            index += 1
        if index == minLength and index < len(word1):
            return "", ""
        elif index == minLength:
            return word1[0], word2[0]
        return word1[index], word2[index]
        