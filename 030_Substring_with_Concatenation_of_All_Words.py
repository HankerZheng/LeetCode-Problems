"""
You are given a string, s, and a list of words, words, that are
all of the same length. Find all starting indices of substring(s)
in s that is a concatenation of each word in words exactly once and

without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

Subscribe to see which companies asked this question
"""

# Key Points: Keep update 2 hashtables.
#                (Keyword -> posi of str)
#             Search through STR by block which is the length of Keyword
#             Then, the problem has been converted into that to find 
#             arithmetic sequence with common difference as the length of KW
#             
#
# Special Testcase: 1) key words stay together
#                           ("acbdjscbsjcbadcbda", ["a","b","c","d"])
#                   2) key words are partly same
#                           ("abcdabcdabed", ["abcd", "bcda", "cdab", "dabc"])
#                           ("abcdabcdabed", ["abc", "bcd", "cda", "dab"])
#
# Run time:


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def check_end(input_dict):
            for value in input_dict.values():
                if value < 0:
                    return 1
            return 0

        if (not s) or (not words):
            return []

        kw_length = len(words[0])
        if len(s) < kw_length:
            return []
        # initialize hashtable
        hashtable = dict()
        for word in words:
            hashtable[word] = list()
        # search through s by block
        cursor = 0
        while (cursor+kw_length-1) < len(s):
            this_block = s[cursor: cursor+kw_length]
            if this_block in words:
                hashtable[this_block].append(cursor)
            cursor += 1



if __name__ == '__main__':
    sol = Solution()
    sol.findSubstring("xbarfoothefoobarman", ["foo", "bar", "the"])