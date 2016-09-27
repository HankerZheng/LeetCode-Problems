# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

# Subscribe to see which companies asked this question

# Runtime: 
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        fifo = []
        used = {}
        for i,ch in enumerate(s):
            used[ch]=used.get(ch,0)+1
            if used[ch] == 1:
                fifo.append(i)
        for i in fifo:
            if used[s[i]]==1:
                return i
        return -1

if __name__ == '__main__':
    sol = Solution()
    print sol.firstUniqChar("")
    print sol.firstUniqChar("a")
    print sol.firstUniqChar("ab")
    print sol.firstUniqChar("aab")
    print sol.firstUniqChar("aabba")
    print sol.firstUniqChar("bab")
    print sol.firstUniqChar("bacba")
    print sol.firstUniqChar("bacbda")