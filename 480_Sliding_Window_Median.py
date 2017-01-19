# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# Examples: 
# [2,3,4] , the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].

# Note: 
# You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.
class HeapNode(object):
    def __init__(self, val, cnt):
        self.val = val
        self.cnt = cnt

    def __str__(self):
        return "[%s, %d]" % (self.val, self.cnt)
    __repr__ = __str__

    def __cmp__(self, other):
        return self.val - other.val

class HashHeap(object):
    def __init__(self, arr):
        elemCnt = self._preProcess(arr)
        self._cap = len(arr)
        self._maxIdx = len(elemCnt) - 1
        self._data = [HeapNode(key, value) for key, value in elemCnt.items()]
        self._hashMap = {node.val: idx for idx, node in enumerate(self._data)}
        self._heapify()

    def _preProcess(self, arr):
        elemCnt = {}
        for elem in arr:
            elemCnt[elem] = elemCnt.get(elem, 0) + 1
        return elemCnt

    def _swap(self, idx1, idx2):
        elem1, elem2 = self._data[idx1], self._data[idx2]
        self._hashMap[elem1.val] = idx2
        self._hashMap[elem2.val] = idx1
        self._data[idx1], self._data[idx2] = elem2, elem1

    def _heapify(self):
        idx = self._maxIdx
        while idx > 0:
            parentIdx = (idx - 1) / 2
            if self._data[parentIdx] > self._data[idx]:
                self._swap(parentIdx, idx)
                self._siftDown(idx)
            idx -= 1

    def _siftDown(self, idx):
        def heapValid(idx):
            left, right = idx * 2 + 1, idx * 2 + 2
            if left > self._maxIdx: return True
            if right > self._maxIdx: return self._data[idx] <= self._data[left]
            return self._data[idx] <= self._data[left] and self._data[idx] <= self._data[right]
        def smallerChild(idx):
            left, right = idx * 2 + 1, idx * 2 + 2
            if left > self._maxIdx: return None
            if right > self._maxIdx: return left
            return left if self._data[left] < self._data[right] else right

        current = idx
        while not heapValid(current):
            child = smallerChild(current)
            self._swap(current, child)
            current = child

    def _siftUp(self, idx):
        current = idx
        parent = (current - 1) / 2
        while current > 0 and self._data[parent] > self._data[current]:
            self._swap(parent, current)
            current = parent
            parent = (current - 1) / 2

    def _removeLastNode(self):
        rmNode = self._data.pop(-1)
        self._cap -= 1
        self._maxIdx -= 1
        self._hashMap.pop(rmNode.val)

    def _removeByIdx(self, idx):
        thisNode = self._data[idx]
        retVal = thisNode.val
        if thisNode.cnt > 1:
            thisNode.cnt -= 1
            self._cap -= 1
        elif idx == self._maxIdx:
            # the node itself is the last node
            self._removeLastNode()
        else:
            self._swap(idx, self._maxIdx)
            self._removeLastNode()
            pidx = (idx - 1) / 2
            # check to see we should sift up or sift down
            if pidx >= 0 and self._data[pidx] > self._data[idx]:
                self._siftUp(idx)
            else:
                self._siftDown(idx)
        return retVal

    def heapPeep(self):
        if not self._data:
            return float("inf")
        return self._data[0].val

    def heapPop(self):
        return self._removeByIdx(0)

    def heapPush(self, elem):
        self._cap += 1
        if elem not in self._hashMap:
            self._maxIdx += 1
            self._data.append(HeapNode(elem, 1))
            self._hashMap[elem] = self._maxIdx
            self._siftUp(self._maxIdx)
        else:
            idx = self._hashMap[elem]
            self._data[idx].cnt += 1
        
    def heapRemove(self, elem):
        if elem not in self._hashMap:
            raise ValueError("Element to be removed is not in HashHeap!!!")
        idx = self._hashMap[elem]
        self._removeByIdx(idx)

    def __contains__(self, value):
        return value in self._hashMap
    def __str__(self):
        return "%s" % [elem.val for elem in self._data]



class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        def addToWindow(smallerHeap, largerHeap, num):
            # print smallerHeap, largerHeap, num
            if smallerHeap._cap < largerHeap._cap:
                if num < largerHeap.heapPeep():
                    smallerHeap.heapPush(-num)
                else:
                    largerHeap.heapPush(num)
                    smallerHeap.heapPush(-largerHeap.heapPop())
            else:
                if num > -smallerHeap.heapPeep():
                    largerHeap.heapPush(num)
                else:
                    smallerHeap.heapPush(-num)
                    largerHeap.heapPush(-smallerHeap.heapPop())
        
        def removeFromWindow(smallerHeap, largerHeap, num):
            # print smallerHeap, largerHeap, num
            if smallerHeap._cap > largerHeap._cap:
                if (-num) in smallerHeap:
                    smallerHeap.heapRemove(-num)
                else:
                    largerHeap.heapRemove(num)
                    largerHeap.heapPush(-smallerHeap.heapPop())
            else:
                if num in largerHeap:
                    largerHeap.heapRemove(num)
                else:
                    smallerHeap.heapRemove(-num)
                    smallerHeap.heapPush(-largerHeap.heapPop())
        
        def getMedian(smallerHeap, largerHeap):
            if smallerHeap._cap == largerHeap._cap:
                return largerHeap.heapPeep() / 2.0 + (-smallerHeap.heapPeep() / 2.0)
            elif smallerHeap._cap > largerHeap._cap:
                return float(-smallerHeap.heapPeep())
            return float(largerHeap.heapPeep())
                
            
        smallerHeap = HashHeap([])
        largerHeap = HashHeap([])
        ans = []
        for i in xrange(k):
            addToWindow(smallerHeap, largerHeap, nums[i])
        ans.append(getMedian(smallerHeap, largerHeap))
        delIdx = 0
        addIdx = k
        # print smallerHeap, largerHeap
        while addIdx < len(nums):
            addToWindow(smallerHeap, largerHeap, nums[addIdx])
            # print smallerHeap, largerHeap
            removeFromWindow(smallerHeap, largerHeap, nums[delIdx])
            # print smallerHeap, largerHeap
            ans.append(getMedian(smallerHeap, largerHeap))
            delIdx += 1
            addIdx += 1
        return ans

def bruteForce(nums, k):
    def getMedian(window):
        length = len(window)
        if length & 1:
            return float(window[(length - 1) / 2])
        else:
            return float(window[length/2] + window[length/2 - 1]) / 2
    import bisect
    ans = []
    window = nums[:k]
    window.sort()
    delIdx = 0
    addIdx = k
    ans.append(getMedian(window))
    while addIdx < len(nums):
        window.pop(window.index(nums[delIdx]))
        bisect.insort(window, nums[addIdx])
        ans.append(getMedian(window))
        addIdx += 1
        delIdx += 1
    return ans


if __name__ == '__main__':
    sol = Solution()
