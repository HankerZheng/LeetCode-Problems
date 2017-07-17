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

# Key Points: Sliding Windows
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
        :type worhttps://leetcode.com/problems/random-one-question/ds: List[str]
        :rtype: List[int]
        """
        def search_in(i, k):
            start, end = i, i
            we_expect = dict(dct)
            while end + k - 1 < len(s):
                new_string = s[end: end + k]
                if new_string in we_expect:
                    # add new_string into the window
                    if we_expect[new_string] == 1:
                        we_expect.pop(new_string)
                    else:
                        we_expect[new_string] -= 1
                    if not we_expect:
                        # we_expect is empty, we find one ans!!
                        res.append(start)
                    end += k
                elif new_string in dct:
                    # new_string is still a word but not we expect
                    # free a old_string
                    we_expect[ s[start:start+k]] = 1
                    start += k
                else:
                    # new_string is junk
                    we_expect = dict(dct)
                    start = end = end + k
                    
        if not words:
            return []
        if not words[0]:
            return range(len(s))
        
        dct = {}
        for word in words:
            dct[word] = dct.get(word, 0) + 1
        res = []
        k = len(words[0])
        for i in xrange(k):
            search_in(i, k)
        return res


if __name__ == '__main__':
    sol = Solution()
    sol.findSubstring("xbarfoothefoobarman", ["foo", "bar", "the"])