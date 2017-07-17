# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
# so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.
class TrieNode(object):
    def __init__(self, char, isWord):
        self.char = char
        self.isWord = isWord
        self.children = {}

    def insert(self, word, index):
        current = self
        for char in word:
            current.children[char] = current.children.get(char, TrieNode(char, -1))
            current = current.children[char]
        current.isWord = index

    def findPrefix(self, prefix):
        current = self
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return None
        return current

    def getWords(self):
        # return (word, index) pairs
        if self.isWord != -1:
            yield "", self.isWord
        queue = [([], childNode) for childNode in self.children.values()]
        while queue:
            charList, thisNode  = queue.pop(0)
            newCharList = charList + [thisNode.char]
            if thisNode.isWord != -1:
                yield "".join(newCharList), thisNode.isWord
            if thisNode.children:
                queue += [(newCharList, childNode) for childNode in thisNode.children.values()]


    def checkPalindrome(self):
        for word, index in self.getWords():
            if word == word[::-1]:
                yield index




class Solution(object):
    def palindromePairs_TrieTree(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        trieTree = TrieNode("dummy", -1)
        reverTreiTree = TrieNode("dummy", -1)
        reverseWords = [word[::-1] for word in words]
        res = set()
        for i in xrange(len(words)):
            trieTree.insert(words[i], i)
            reverTreiTree.insert(reverseWords[i], i)

        for i in xrange(len(words)):
            nodeji = trieTree.findPrefix(reverseWords[i])
            nodeij = reverTreiTree.findPrefix(words[i])
            if nodeij:
                res |= {(i, j) for j in nodeij.checkPalindrome() if j != i}
            if nodeji:
                res |= {(j, i) for j in nodeji.checkPalindrome() if i != j}

        return list(res)



    def palindromePairs_BruteForce(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def checkPalindrome(toCheck):
            start, end = 0, len(toCheck) - 1
            while start < end:
                if toCheck[start] == toCheck[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True


        res = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                elif checkPalindrome(words[i] + words[j]):
                    res.append([i,j])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.palindromePairs(["a","abc","aba",""])