# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.

# Key Points: Maintain one minheap and one self.maxheap.
#             The minheap keep the half large number, while
#             the maxheap keep the half small number.
#
# Run Time: 328 ms

from heapq import *
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        min_len, max_len = len(self.minheap), len(self.maxheap)
        if (min_len+max_len)==0:
            heappush(self.minheap, num)
            return

        if min_len == max_len:
            if num > -self.maxheap[0]:
                heappush(self.minheap, num)
            else:
                heappush(self.maxheap, -num)
        elif min_len > max_len:
            # higher priority to add to max_len(smaller data)
            if num > self.minheap[0]:
                data = heapreplace(self.minheap, num)
                heappush(self.maxheap, -data)
            else:
                heappush(self.maxheap, -num)
        else:
            # higher priority to add to min_len(larger data)
            if num > -self.maxheap[0]:
                heappush(self.minheap, num)
            else:
                data = -heapreplace(self.maxheap, -num)
                heappush(self.minheap, data)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        min_len, max_len = len(self.minheap), len(self.maxheap)
        if min_len == max_len:
            return (self.minheap[0]-self.maxheap[0])/2.0
        elif min_len > max_len:
            return self.minheap[0]
        else:
            return -self.maxheap[0]

        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

if __name__ == "__main__":
    mf = MedianFinder()
    for x in xrange(2,10):
        mf.addNum(x)
        print mf.findMedian()