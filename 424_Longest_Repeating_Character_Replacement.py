class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def check_window(diction, k):
            majority = 0
            length = 0
            for k,v in diction.items():
                majority = max(majority, v)
                length += v
            diff = length - majority
            print majority, length, diff, k, diff<=k
            return diff <= k

        char_set = "QWERTYUIOPASDFGHJKLZXCVBNM"
        window = {char: 0 for char in char_set}
        start, end = 0, 0
        ans = 0
        while end < len(s):
            add_char = s[end]
            window[add_char] += 1
            if check_window(window, k):
                end += 1
            else:
                while start < end and not check_window(window, k):
                    del_char = s[start]
                    window[del_char] -= 1
                    start += 1
            ans = max(ans, end - start)
            
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.characterReplacement('AABABBA', 1)