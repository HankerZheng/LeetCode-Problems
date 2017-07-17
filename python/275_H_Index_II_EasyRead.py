class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        if citations[0] >= len(citations):
            return len(citations)
        if citations[-1] == 0:
            return 0

        paperNum = len(citations)
        lo = 1
        hi = paperNum - 1
        while lo <= hi:
            hIdx = (lo + hi) / 2
            # condition1:  h of his/her N papers have at least h citations each
            condition1 = citations[paperNum - hIdx] >= hIdx
            # conditions2: the other N - h papers have no more than h citations each.
            condition2 = citations[paperNum - hIdx - 1] <= hIdx
            if not condition1:
                hi = hIdx - 1
            elif not condition2:
                lo = hIdx + 1
            else:
                return hIdx
        raise ValueError("Input Array is not in Accending order!!")

if __name__ == '__main__':
    sol = Solution()
    print sol.hIndex([1,2,3,4,5,6,7])