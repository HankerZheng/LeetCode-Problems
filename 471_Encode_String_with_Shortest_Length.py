# Given a non-empty string, encode the string such that its encoded length is the shortest.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

# Note:
# k will be a positive integer and encoded string will not be empty or have extra space.
# You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
# If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
# Example 1:

# Input: "aaa"
# Output: "aaa"
# Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
# Example 2:

# Input: "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
# Example 3:

# Input: "aaaaaaaaaa"
# Output: "10[a]"
# Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
# Example 4:

# Input: "aabcaabcd"
# Output: "2[aabc]d"
# Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
# Example 5:

# Input: "abbbabbbcabbbabbbc"
# Output: "2[2[abbb]c]"
# Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".

class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dp[i,j] represent the best encode of str[i:j+1] representing by word and count
        # dp[i,j] = MIN {dp[i,k] + dp[k+1, j]}
        def convert(word, count):
            if count > 1 and count + len(word) >= 5:
                return str(count) + "[" + word + "]"
            else:
                return word * count

        def calculateLength(word, count):
            if count > 1 and count + len(word) >= 5:
                return len(str(count)) + len(word) + 2
            else:
                return len(word) * count


        def combine(word1, word2, cnt1, cnt2):
            if word1 == word2:
                return word1, cnt1 + cnt2
            else:
                return convert(word1, cnt1) + convert(word2, cnt2), 1

        def onlyOneChar(start, end):
            thisChar = s[start]
            cnt = 1
            for idx in xrange(start, end + 1):
                if s[idx] != thisChar:
                    return False
                history[(start, idx)] = thisChar, cnt
                cnt += 1
            return True
            
        def findBestEncode(start, end):
            if (start, end) in history:
                return history[(start, end)]
            # if there only one word in this substring, terminate early
            if onlyOneChar(start, end):
                return s[start], end - start + 1
            # normal recursion
            minLength = end - start + 1
            wordAns = s[start:end+1]
            cntAns = 1
            for midIdx in xrange(start, end):
                word1, cnt1 = findBestEncode(start, midIdx)
                word2, cnt2 = findBestEncode(midIdx + 1, end)
                wordRes, cntRes = combine(word1, word2, cnt1, cnt2)
                thisLength = calculateLength(wordRes, cntRes)
                if thisLength <= minLength and len(wordRes) < len(wordAns):
                    minLength = thisLength
                    wordAns = wordRes
                    cntAns = cntRes
            history[(start, end)] = (wordAns, cntAns)
            return wordAns, cntAns

        history = {}
        word, count = findBestEncode(0, len(s) - 1)
        return convert(word, count)

if __name__ == '__main__':
    sol = Solution()
    print sol.encode("leecccccccccccccccccoccccccccccccccccccccccccccccccccccccccccccccccccccccccoccccceeeeeeeeecccccccccccccccccccde")
    # print sol.encode("aabcaabcd")