class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        def update(dct, word, count):
            for char in word:
                dct[char] -= count
                dct[char] == 0 and dct.pop(char)

        num_set = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        dct = {}
        for char in s:
            dct[char] = dct.get(char, 0) + 1
        res = []
        sol_seq = [('z', 0), ('w', 2), ('g', 8), ('u', 4), ('h', 3), ('x', 6), ('f', 5), ('s', 7), ('i', 9), ('n', 1)]
        for char, num in sol_seq:
            if char in dct:
                res += [str(num) * dct[char]]
                update(dct, num_set[num], dct[char])
        res.sort()
        return "".join(res)
        

if __name__ == '__main__':
    sol = Solution()
    print sol.originalDigits("fviefuro")