# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.


# Runtime: 244ms

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = {}
        res = []
        for string in strs:
            tag = "".join(sorted(string))
            tmp = table.get(tag, list())
            tmp.append(string)
            table[tag] = tmp
        for tag in table.keys():
            res.append(table[tag])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print sol.groupAnagrams(["eat"])
    print sol.groupAnagrams([])
