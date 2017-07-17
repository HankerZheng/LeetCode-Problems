# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

# Example 1:

# Input:
# s = "aaabb", k = 3

# Output:
# 3

# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input:
# s = "ababbc", k = 2

# Output:
# 5

# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
# Subscribe to see which companies asked this question

# DIVIDE AND CONQUER:
#       Split the string according to `notReach` characters
#       Then solve the sub-problem


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def checkMap(hashmap):
            ans = set()
            for key, v in hashmap.items():
                if v != 0 and v < k:
                    ans.add(key)
            return ans
        def helper(start, end):
            # return the ans of s[start:end]
            if start == end:
                return 0
            hashmap = {}
            for i in xrange(start, end):
                hashmap[s[i]] = hashmap.get(s[i], 0) + 1
            notReach = checkMap(hashmap)
            if not notReach:
                return end - start
            ans = 0
            curStart = start
            for i in xrange(start, end):
                if s[i] in notReach:
                    ans = max(ans, helper(curStart, i))
                    curStart = i + 1
            return max(ans, helper(curStart, end))

        return helper(0, len(s))
            
if __name__ == '__main__':
    sol = Solution()
    print sol.longestSubstring("bbaaacbd", 3)