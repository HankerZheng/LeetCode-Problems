# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

# For example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true

class TrieNode(object):
    def __init__(self, char, isWord):
        self._char = char
        self.isWord = isWord
        self.children = {}

    def insert(self, word):
        current = self
        for char in word:
            current.children[char] = current.children.get(char, TrieNode(char, False))
            current = current.children[char]
        current.isWord = True

    def findWord(self, word):
        if not word:
            return self.isWord

        current, idx = self, 0
        while idx < len(word):
            if word[idx] == ".":
                return any([child.findWord(word[idx+1:]) for child in current.children.values()])
            elif word[idx] in current.children:
                current = current.children[word[idx]]
                idx += 1
            else:
                return False
        return current.isWord


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._root = TrieNode("dummy", False)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self._root.insert(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._root.findWord(word)
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

if __name__ == '__main__':
    sol = WordDictionary()
    sol.addWord("test")
    sol.addWord("east")
    print sol.search("..st")