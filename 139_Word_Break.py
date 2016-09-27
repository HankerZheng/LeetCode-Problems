# Given a string s and a dictionary of words dict, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

# Subscribe to see which companies asked this question


# Runtime: 59 ms

class TrieNode(object):
    def __init__(self, value):
        self.value = value
        self._data = {}
        self.isWord = False
    def __getitem__(self, key):
        return self._data.get(key, None)
    def __setitem__(self, key, value):
        self._data[key] = value

class TrieTree(object):
    def __init__(self):
        self.root = TrieNode('dummy')
    def insert(self, word):
        def node_insert(node, ch):
            if node[ch] is not None:
                return node[ch]
            node[ch] = TrieNode(ch)
            return node[ch]
        this_node = self.root
        for ch in word:
            this_node = node_insert(this_node, ch)
        this_node.isWord = True

class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [0] * len(s)
        for i,char in enumerate(s):
            for word in wordDict:
                length = len(word)
                if i >= length-1 and s[i-length+1:i+1]==word and (dp[i-length] == 1 or i-length+1 == 0):
                    dp[i] = 1
                    break
        return bool(dp[-1])
    def wordBreak_DFS_TRIETREE_TLE(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        def helper(index, node):
            """
            s[index] is the char to be checked this time
            node's children may store s[index]
            """
            # if index == len(s):
            #     return node.isWord
            # if node[s[index]] is None:
            #     # no child named s[index]
            #     return False
            # else:
            #     # there is a child named s[index]
            #     this_node = node[s[index]] 
            #     if this_node.isWord:
            #         # if this is also the end of a word
            #         return helper(index+1, mytree.root) or helper(index+1, this_node)
            #     else:
            #         return helper(index+1, this_node)
            queue = [(index, node)]
            while queue:
                i, this_node = queue.pop(0)
                if i == len(s):
                    if this_node.isWord:
                        return True
                    else:
                        continue
                if this_node[s[i]] is None:
                    continue
                else:
                    queue.append((i+1, this_node[s[i]]))
                    if this_node[s[i]].isWord:
                        queue.append((i+1, mytree.root))
            return False
        mytree = TrieTree()
        for word in wordDict:
            mytree.insert(word)
        return helper(0, mytree.root)

if __name__ == '__main__':
    sol = Solution()
    print sol.wordBreak("abcade", ["abc","ade"])
    print sol.wordBreak("aaaaaaa", ["aaaa","aa"])