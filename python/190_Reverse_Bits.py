class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        this_num = n
        res = 0
        for i in xrange(32):
            res = (res<<1) ^ (this_num & 1)
            this_num = this_num >> 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.reverseBits(-1)