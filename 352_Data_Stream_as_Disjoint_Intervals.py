# Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
# Follow up:
# What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?


# LINKED LIST:
#       Use Linked List to update the data input.


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def searchTarget(self, target):
        """
        Return the ListNode that is smaller than target
        Given a linked list as ["dummy", [4,6], [9,12], [15, 40]],
        target = 1, return "dummy"
        target = 3, return "dummy"
        target = 7, reutrn [4,6]
        target = 10, return [9,12]
        target = 13, return [9,12]
        """
        tmp = self
        while tmp.next and tmp.next.val.start < target and tmp.next.val.end < target:
            tmp = tmp.next
        return tmp
        
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._intervals = ListNode("dummy")

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        def merge(firstNode):
            newNode = firstNode.next
            nextNode = newNode.next
            if nextNode is None and firstNode is self._intervals:
                # newNode is the only node available
                return
            if nextNode is None:
                if firstNode.val.end + 1== newNode.val.start:
                    firstNode.val.end = newNode.val.end
                    firstNode.next = None
                return
            if firstNode is self._intervals:
                if newNode.val.end + 1 == nextNode.val.start:
                    nextNode.val.start = newNode.val.start
                    firstNode.next = nextNode
                return
            # if all three nodes exist
            if firstNode.val.end + 1 == newNode.val.start and newNode.val.end + 1 == nextNode.val.start:
                # merge all three node
                firstNode.val.end = nextNode.val.end
                firstNode.next = nextNode.next
                return
            
            if firstNode.val.end + 1 == newNode.val.start:
                firstNode.val.end = newNode.val.end
                firstNode.next = nextNode
                return
            if newNode.val.end + 1 == nextNode.val.start:
                nextNode.val.start = newNode.val.start
                firstNode.next = nextNode
                return
        
        prevNode = self._intervals.searchTarget(val)
        if prevNode.next and prevNode.next.val.start <= val <= prevNode.next.val.end:
                return
        
        newNode = ListNode(Interval(val, val))
        tmp = prevNode.next
        prevNode.next = newNode
        newNode.next = tmp
        
        merge(prevNode)
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        tmp = self._intervals.next
        res = []
        while tmp:
            res.append(tmp.val)
            tmp = tmp.next
        return res
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()