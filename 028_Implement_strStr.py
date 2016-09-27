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
# Run time: 74 ms

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # boundary condition
        if needle == "":
            return 0
        if haystack == "":
            return -1
        # initialize pointers and flag
        p_haystack, p_needle, start_compare = 0, 0, 0
        # loop while pointers are within their range
        while p_haystack < len(haystack) and p_needle < len(needle):
            if haystack[p_haystack] == needle[p_needle]:
            # if detected equal, run into compare mode
            # move both pointers forward
                if not start_compare:
                    start_compare = 1
                    p_tmp = p_haystack
                p_needle += 1
                p_haystack += 1
            else:
            # if not equal, run back to search mode(reset flag)
                if start_compare:
                    p_needle = 0
                    start_compare = 0
                    p_haystack = p_tmp + 1
                else:
                    p_haystack = p_haystack + 1
                    
        if p_needle == len(needle):
            return p_haystack - p_needle
        else:
            return -1




    def strStr_re(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if haystack == "":
            return -1
        import re
        res = re.split(needle, haystack)[0]
        res = len(res)
        if res == len(haystack):
            return -1
        else:
            return res

