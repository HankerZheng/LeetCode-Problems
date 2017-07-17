# Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.
# Example:

# Input:
# n: 13   k: 2

# Output:
# 10

# Explanation:
# The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
# Subscribe to see which companies asked this question


class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        prefix = 1
        rank = k - 1
        while rank > 0:
            count = 0
            interval = [prefix, prefix + 1]
            while interval[0] <= n:
                count += min(n+1, interval[1]) - interval[0]
                print "[%d, %d], count = %d, rank = %d" % (interval[0], interval[1], count, rank)
                interval = [interval[0] * 10, interval[1] * 10]
            
            print "[%d, %d], count = %d, rank = %d" % (interval[0], interval[1], count, rank)
            if rank >= count:
                prefix += 1
                rank -= count
            else:
                prefix *= 10
                rank -= 1
        return prefix

if __name__ == '__main__':
    sol = Solution()
    print sol.findKthNumber(2450, 2321)