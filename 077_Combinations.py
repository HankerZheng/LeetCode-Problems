# Given two integers n and k, return all possible
# combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Subscribe to see which companies asked this question


# Runtime: 384ms
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(ans,used, k, maxnum):
            if k==0:
                res.append(ans)
                return
            if maxnum+k>=n+1:
                return
            for num in xrange(maxnum,n):
                if not used[num+1]:
                    used[num+1]=1
                    helper(ans+[num+1], used, k-1, num)
                    used[num+1]=0
        res = []
        used = {(i+1):0 for i in xrange(n)}
        helper([],used, k, 0)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.combine(5,2)
    print sol.combine(1,1)
    print sol.combine(16,12)
