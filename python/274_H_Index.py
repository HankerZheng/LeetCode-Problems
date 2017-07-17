

# Show Hint 
class Solution(object):
    def hIndex_extraSpace(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        counts = [0 for i in xrange(len(citations)+1)]
        for i, num in enumerate(citations):
            if num > len(citations):
                counts[-1] += 1
            else:
                counts[num] += 1
        mysum = 0
        for i in xrange(len(citations), 0, -1):
            mysum += counts[i]
            if mysum >= i:
                return i
        return 0
            


    def hIndex_partition(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        def partition(start, end):
            if start > end:
                return len(citations) - start
            pivot = citations[start]
            i_s, i_e = start, end
            while i_s < i_e:
                while i_s < i_e and citations[i_e] >= pivot:
                    i_e -= 1
                citations[i_s] = citations[i_e]
                while i_s < i_e and citations[i_s] <= pivot:
                    i_s += 1
                citations[i_e] = citations[i_s]
            citations[i_s] = pivot
            # there are (%length% - %i_s%) papers got at least %pivot% citations
            if pivot == (len(citations) - i_s):
                return pivot
            elif pivot > (len(citations) - i_s):
                return partition(start, i_s-1)
            else:
                return partition(i_s+1, end)

        if not citations:
            return 0
        return partition(0, len(citations)-1)

    def hIndex_nlogn(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort()
        ans = 0
        length = len(citations)
        for i in xrange(length+1):
            if i == 0:
                if citations[-1] == 0:
                    return 0
            else:
                if citations[-i] >= i:
                    ans = i
                else:
                    break
        return ans

if __name__ == '__main__':
     sol = Solution()
     print sol.hIndex([3, 0, 6, 1, 5])
     print sol.hIndex([0,0,0,0])
     print sol.hIndex([9,9,9,9,9,9])
     print sol.hIndex([1])
     print sol.hIndex([10])