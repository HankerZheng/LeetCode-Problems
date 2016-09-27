# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?

# Subscribe to see which companies asked this question

# Runtime: 64ms

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        old_ans = [1,1]
        row = 1
        while row < rowIndex:
            old_ans = [1] + [old_ans[i]+old_ans[i+1] for i in xrange(len(old_ans)-1)] + [1]
            row+=1
        return old_ans

if __name__ == '__main__':
    sol = Solution()
    print sol.getRow(1)
    print sol.getRow(2)
    print sol.getRow(3)
    print sol.getRow(4)
    print sol.getRow(5)
    print sol.getRow(6)