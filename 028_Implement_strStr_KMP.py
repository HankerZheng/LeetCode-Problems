class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def preProcess(needle):
            prefixList = [0] * len(needle)
            needleIdx = 0
            prefixIdx = 1
            while prefixIdx < len(needle):
                while prefixIdx < len(needle) and needle[prefixIdx] == needle[needleIdx]:
                    prefixList[prefixIdx] = needleIdx + 1
                    needleIdx += 1
                    prefixIdx += 1
                if needleIdx != 0:
                    needleIdx = prefixList[needleIdx-1]
                else:
                    prefixIdx += 1
            return prefixList

        if not needle and not haystack:
            return 0
        elif not needle:
            return 0
        prefixList = preProcess(needle)
        needlePos = haystackPos = 0
        while haystackPos < len(haystack):
            if haystack[haystackPos] == needle[needlePos]:
                haystackPos += 1
                needlePos += 1
            elif needlePos != 0:
                needlePos = prefixList[needlePos-1]
            elif needlePos == 0:
                haystackPos += 1
            if needlePos == len(needle):
                return haystackPos - len(needle)
        return -1

# if __name__ == '__main__':
#     sol = Solution()
#     print sol.strStr("googlegoogle", "gle")
#     print sol.strStr("mississippi", "issip")
#     print sol.strStr("baaabbaabaaabaaaabaababba", "aabaaaaba")