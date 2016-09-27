'''Given n, how many structurally unique BST's (binary search trees) that
store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# Key Points: Dynamic Programming.
#               n = 1, there are 1 different BST
#               n = 2, there are 2 different BSTs
#               n = 3, there are 5 different BSTs. 5 = 2+2+1
#               n = 4, there are 14 different BSTs. 14 = 5+5+2+2
#               n = 5, there are 42 different BSTs. 42 = 14+14+5+5+2*2
#               ...  Let take n = 5 for example
#             When n == 5, there are 5 different roots.
#               1) root = 1. Left subtree is none, right subtree is the same
#                  situation as when n = 4. It counts for 14
#               2) root = 2. Left subtree is the same as when n = 1, while 
#                  right subtree is the same as when n = 3.
#                  It counts for 1*5
#               3) root = 3. Left subtree is the same as when n = 2, while
#                  right subtree is the same as when n = 2.
#                  It counts for 2*2
#               4) root = 4. Same as 2). It counts for 5
#               5) root = 5. Same as 1). It counts for 14
#             Thus, totoally is 28 + 10 + 4 = 42
#

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        dp_matrix = [1,1,2]
        for i in xrange(3, n+1):
            ans = 0
            for j in xrange(i):
                ans += dp_matrix[j]*dp_matrix[i-j-1]
            dp_matrix.append(ans)
        return dp_matrix[n]

if __name__ == "__main__":
    sol = Solution()
    for i in xrange(15):
        print sol.numTrees(i)