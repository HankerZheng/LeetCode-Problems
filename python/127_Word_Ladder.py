# Given two words (beginWord and endWord), and a dictionary's word list, 
# find the length of shortest transformation sequence from beginWord to endWord,
# such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.

# Runtime: 606 / 295 ms

class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        char_set = "qwertyuiopasdfghjklzxcvbnm"
        length = 2
        queue = [beginWord]
        next_queue = []
        while queue:
            this_word = queue.pop(0)
            possible_words = [this_word[:i] + ch + this_word[i+1:] for i in xrange(len(this_word)) for ch in char_set]
            for word in possible_words:
                if word == endWord:
                    return length
                if word in wordList:
                    next_queue.append(word)
                    wordList -= set([word])
            if not queue:
                queue = next_queue
                next_queue = []
                length += 1
        return 0


    def ladderLength_BFS(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d


        def bfs(beginWord, endWord):
            queue = [beginWord]
            next_queue = []
            visited = set()
            length = 0
            while queue:
                this_word = queue.pop(0)
                if this_word == endWord:
                    return length + 1
                for i in xrange(len(this_word)):
                    s = this_word[:i] + "_" + this_word[i+1:]
                    for neighbor in neighbor_dict[s]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            next_queue.append(neighbor)
                if not queue:
                    queue = next_queue
                    next_queue = []
                    length += 1
            return 0


        neighbor_dict = construct_dict(wordList | set([beginWord, endWord]))
        return bfs(beginWord, endWord)


if __name__ == '__main__':
    sol = Solution()
    # print sol.ladderLength('hit', 'cog', set(["hot","dot","dog","lot","log"]))
    print sol.ladderLength("cater","mangy",set(["kinds","taney","mangy","pimps","belly","liter","cooks","finny","buddy","hewer","roves","lusts","toots","fully","acorn","junes","araby","visas","pyres","siren","limps","paved","marla","tulsa","foxes","purls","stats","bidet","milky","payee","horny","tanks","mints","cindy","forms","files","fucks","dolts","welts","dykes","riced","rebel","gulfs","bully","meets","tidal","surer","gecko","noyes","rents","aaron","rafts","roils","sower","dicey","sties","jamal","bases","locus","gusts","briar","gills","filly","mixes","fjord","aggie","tails","funks","freon","roods","links","natal","melds","abide","hardy","lands","unpin","loges","weest","rices","dicks","gyros","hands","quoit","hater","rings","loxed","weeds","coeds","handy","boxer","jamar","cokes","earls","tings","haley","tangy","hinds","cater","mores","lloyd","bayes","slice","taker","piped","doses","sides","gorge","sorta","gavel","lanes","wrote","haney","monet","mikes","bared","pelts","fails","curry","waken","jaded","halos","welds","danes","assad","waded","agree","bents","comet","train","crags","fifes","rared","noons","scums","steep","haler","waxen","carey","gamay","larry","diver","honer","mandy","poxed","coded","waned","sades","clair","fared","hangs","sully","tiled","stoic","docks","cloth"]))
    print sol.ladderLength_BFS("cater","mangy",set(["kinds","taney","mangy","pimps","belly","liter","cooks","finny","buddy","hewer","roves","lusts","toots","fully","acorn","junes","araby","visas","pyres","siren","limps","paved","marla","tulsa","foxes","purls","stats","bidet","milky","payee","horny","tanks","mints","cindy","forms","files","fucks","dolts","welts","dykes","riced","rebel","gulfs","bully","meets","tidal","surer","gecko","noyes","rents","aaron","rafts","roils","sower","dicey","sties","jamal","bases","locus","gusts","briar","gills","filly","mixes","fjord","aggie","tails","funks","freon","roods","links","natal","melds","abide","hardy","lands","unpin","loges","weest","rices","dicks","gyros","hands","quoit","hater","rings","loxed","weeds","coeds","handy","boxer","jamar","cokes","earls","tings","haley","tangy","hinds","cater","mores","lloyd","bayes","slice","taker","piped","doses","sides","gorge","sorta","gavel","lanes","wrote","haney","monet","mikes","bared","pelts","fails","curry","waken","jaded","halos","welds","danes","assad","waded","agree","bents","comet","train","crags","fifes","rared","noons","scums","steep","haler","waxen","carey","gamay","larry","diver","honer","mandy","poxed","coded","waned","sades","clair","fared","hangs","sully","tiled","stoic","docks","cloth"]))