# Given a set of words (without duplicates), find all word squares you can build from them.

# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 <= k < max(numRows, numColumns).

# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

# b a l l
# a r e a
# l e a d
# l a d y
# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:

# Input:
# ["area","lead","wall","lady","ball"]

# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]

# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Example 2:

# Input:
# ["abat","baba","atan","atal"]

# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]

# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Show Company Tags
# Show Tags
# Show Similar Problems

class TrieTree(object):
    def __init__(self, val, isWord=False):
        self.val = val
        self.children = {}
        self.isWord = isWord

    def insertWord(self, word):
        thisNode = self
        for char in word:
            if char in thisNode.children:
                thisNode = thisNode.children[char]
            else:
                thisNode.children[char] = TrieTree(char)
                thisNode = thisNode.children[char]
        thisNode.isWord = True

    def findWord(self, word):
        thisNode = self
        for char in word:
            if char in thisNode.children:
                thisNode = thisNode.children[char]
            else:
                return False
        return thisNode.isWord

    def findPrefix(self, prefix):
        """
        return None if `prefix` doesn't exist
        return the node if prefix exist
        """
        thisNode = self
        for char in prefix:
            if char in thisNode.children:
                thisNode = thisNode.children[char]
            else:
                return None
        return thisNode

    def findAllPrefix(self, prefix):
        """
        return all the words in the tree has the prefix
        """
        thisNode = self.findPrefix(prefix)
        if not thisNode:
            return []
        ans = []
        for word in thisNode.findAllWords():
            ans.append(prefix + word)
        return ans

    def findAllWords(self):
        """
        return all the words of the node `self`
        the Char in `self` is not included
        """
        def helper(node, ans):
            if not node:
                return
            for char in node.children:
                newNode = node.children[char]
                if newNode.isWord:
                    res.append("".join(ans + [newNode.val]))
                helper(newNode, ans + [newNode.val])

        res = []
        helper(self, [])
        return res 


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        def checkFirst(word):
            for char in word:
                if char not in firstHash:
                    return False
            return True

        def helper(ans, length):
            if length == len(words[0]):
                res.append(ans)
                return
            prefix = "".join([word[length] for word in ans])
            for word in rootNode.findAllPrefix(prefix):
                helper(ans + [word], length + 1)

        if not words or not words[0]: return []
        rootNode = TrieTree("dummy")
        firstHash = set()
        for word in words:
            firstHash.add(word[0])
            rootNode.insertWord(word)
        res = []
        for word in words:
            if checkFirst(word):
                helper([word], 1)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.wordSquares(["abat","baba","atan","atal"])