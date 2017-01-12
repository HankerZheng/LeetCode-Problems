class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def charAt(idx):
            # return the virtual char at idx
            return "#" if idx&1 else s[idx/2]
            
        def checkPalindrome(midIdx):
            delta = 1
            while midIdx - delta >= 0 and charAt(midIdx - delta) == charAt(midIdx + delta):
                delta += 1
            return midIdx - delta == -1
        
        # assume the mid point the palindrome is the middle char in s
        if len(s) <= 1:
            return s
        
        midIdx = len(s) - 1
        while not checkPalindrome(midIdx):
            midIdx -= 1
        add = len(s) - midIdx - 1
        return s if add == 0 else s[-add:][::-1] + s