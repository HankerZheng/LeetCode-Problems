# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Subscribe to see which companies asked this question

# Runtime: 122 ms


# Improvement: if there is only alpha character and it is case sensitive, we could use a 32-bit integer
#              instead of the hashset. Each bit in the integer represent one character in use or not.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashtable = set()
        ans = 0
        fast, low = 0, 0
        while fast < len(s):
            while low < fast and s[fast] in hashtable:
                hashtable.remove(s[low])
                low += 1
            while fast < len(s) and s[fast] not in hashtable:
                hashtable.add(s[fast])
                fast += 1
            ans = max(ans, fast-low)
        return ans

if __name__ == '__main__':
    sol = Solution()
    assert sol.lengthOfLongestSubstring('aabbc') == 2
    assert sol.lengthOfLongestSubstring('') == 0
    assert sol.lengthOfLongestSubstring('aaaaa') == 1
    assert sol.lengthOfLongestSubstring('abvcvsde') == 5