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

# Key Points: Recursion.
#             Search through STR by block which is the length of Keyword
#             Once the block is matched with kw in keywords, check whether
#             the rest of s is matched with the rest of keywords.
#
# Revision 1: In the original version of code, I got a TLE error. Because I define
#             recursion function as sub_check(s, words, used_words, kw_length),
#             where s == s[kw_length:].
#             In Python, once slice operation is in the right side of assignment,
#             Python interpreter would make copy of the original resouce, which
#             means that I unintentionally make an unacceptable number of copies of
#             the original string. That is the reason why I got TLE.
#
#             The code below is the revision of the original one. Instead of sending
#             the entire string to recursion function, I pass the index. Then, all the
#             following operation would be done on the original string without using
#             extended space.
#
# Revision 2: Instead of using IF-statement and kw_dict[kw] to judge whether the word
#             we inspect is in kw_dict.keys(), we should use kw_dict.get(kw, 0)
#             Also, when creating kw_dict in pre-process step, instead of using for-loop
#             initializing the dict by {... for ...} is much faster then for loop
#
# Recursion Depth:
#             When the input is 'aaaaaa....', ['a','a',a','a',...], my solution would
#             hit the maxium recursion depth.
#             In order to handle this, we should rearange words list.
#             Open a hashtalbe to replace the input list.
#                   hashtable[keyword] = num of occurances
#             Also, the recursion should be rewritten as LOOP form
#
# AAA problem:
#             Once input is 'aaaaaa....', ['a','a',a','a',...] type and result is [],
#             It would take unacceptable time to execute the program.
#             Therefore, when there is only one key in the kw_dict, jump out of loop
#             because there is only one possible contenation of kw.
#             NO NEED TO DO THIS(jump out of loop when there is only one key left),
#             because even there is only one key left, it is still a string compare.
#             There is no difference between comparing a long string with another long
#             string and compare several short strings with a long string.
#
# ABAB problem:
#             Once input is 'ababababab...', ['ab','ab',..., 'ba','ba',...] type.
#
# Time Complextiy:
#             Assume the length of string is N
#                    the num of keywords is M
#             This algorithm is of O(N*M) time complexity
#
# Special Testcase: 1) key words stay together
#                           ("acbdjscbsjcbadcbda", ["a","b","c","d"])
#                   2) key words are partly same
#                           ("abcdabcdabed", ["abcd", "bcda", "cdab", "dabc"])
#                           ("abcdabcdabed", ["abc", "bcd", "cda", "dab"])
#                   3) Repetition of Keywords
#                           ("wordgoodgoodgoodbestword", ["word","good","best","good"])
#
# Run time: 602 ms (best answer is 162 ms)


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def substring_check(s, s_index, words, kw_length, words_length):
            words_tmp = dict(words)
            for i in xrange(words_length):
                this_block = s[s_index : s_index+kw_length]
                if words_tmp.get(this_block, 0):
                    words_tmp[this_block] -= 1
                else:
                    return False
                s_index += kw_length
                if s_index > len(s):
                    return False
            return True
# Code below is for when there is only one keyword left in words_tmp
#            left_key = words_tmp.keys()[0]
#            this_block = left_key* words_tmp[left_key]
#            if this_block == s[s_index: s_index+words_tmp[left_key]*kw_length]:
#                return True
#            else:
#                return False

        # handle boundary condition
        if (not s) or (not words):
            return []
        kw_length, words_length, s_length = len(words[0]), len(words), len(s)
        if s_length < kw_length:
            return []

        # pre-process input list
        kw_dict = dict()
        for word in words:
            kw_dict[word] = kw_dict.get(word, 0) + 1

        # search through s by block
        res, cursor = list(), 0
        for cursor in xrange(s_length - kw_length*words_length + 1):
            this_block = s[cursor: cursor+kw_length]
            if substring_check(s, cursor, kw_dict, kw_length, words_length):
                res.append(cursor)

        return res



if __name__ == '__main__':
    sol = Solution()
    print sol.findSubstring("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab",
["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"])