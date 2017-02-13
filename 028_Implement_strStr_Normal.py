"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Subscribe to see which companies asked this question
"""

# Key Points: Can be implementd by re module. But run time is 180 ms
#             Use two pointer, one terverses needle, the other terverses
#             haystack. Once the first element is detected equal, run in
#             compare mode(set falg). If p_needle reaches the end, FOUND,
#             else, end compare mode and make p_haystack to the next element
#             to the one which we start compare.
#
# Run time: 74 / 63 ms

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def compareSeg(haystackIdx):
            length = len(needle)
            if haystackIdx + length > len(haystack):
                return False
            return haystack[haystackIdx: haystackIdx+length] == needle
        
        if needle == "":
            return 0
        elif haystack == "":
            return 0 if needle == "" else -1
        needleIdx = 0
        for i in xrange(len(haystack)):
            if haystack[i] == needle[0]:
                if compareSeg(i):
                    return i
        return -1
        