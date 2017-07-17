# The set [1,2,3,...,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.

# Runtime: 60ms

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def helper(nums, k, loop):
            if not nums:
                return
            thisK, newK = divmod(k, loop)
            # print nums, k, loop, thisK, newK
            res.append(nums.pop(thisK))
            helper(nums, newK, loop / max(1, len(nums)))

        res = []
        loop = 1
        for i in xrange(1, n+1):
            loop *= i
        helper([x+1 for x in xrange(n)], (k-1) % loop, loop/n)
        return "".join([str(num) for num in res])

if __name__ == '__main__':
    sol = Solution()
    print sol.getPermutation(2,1)
    print sol.getPermutation(2,4)
    print sol.getPermutation(5,1)
    print sol.getPermutation(5,0)
    print sol.getPermutation(5,3)