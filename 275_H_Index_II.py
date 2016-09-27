# Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

class Solution(object):
    def hIndex(self, citations):
        start, end = 0, len(citations)-1
        while start <= end:
            mid = (start + end)/2
            if len(citations) - mid < citations[mid]:
                # h is too small, increase h
                # len(citations) - end + 1 is a potential answer
                end = mid - 1
            elif len(citations) - mid == citations[mid]:
                return len(citations) - mid
            else:
                # h is too large, decrease h
                start = mid + 1
        return len(citations) - start

    def hIndex_recursive(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        def binary_search(start, end):
            if start > end:
                return len(citations) - start
            i_s, i_e = start, end
            while i_s <= i_e:
                mid = (i_s + i_e) / 2
                if len(citations) - mid > citations[mid]:
                    return binary_search(mid + 1, end)
                elif len(citations) - mid < citations[mid]:
                    return binary_search(start, mid - 1)
                else:
                    return citations[mid]

        if not citations:
            return 0
        return binary_search(0, len(citations) - 1)

if __name__ == '__main__':
    sol = Solution()
    print sol.hIndex([])
    print sol.hIndex([0])
    print sol.hIndex([0,0])
    print sol.hIndex([0,1,2,3,4,5])
    print sol.hIndex([0,0,2,3,5])
    print sol.hIndex_recursive([])
    print sol.hIndex_recursive([0])
    print sol.hIndex_recursive([0,0])
    print sol.hIndex_recursive([0,1,2,3,4,5])
    print sol.hIndex_recursive([0,0,2,3,5])