# Implement a data structure supporting the following operations:

# Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
# Challenge: Perform all these in O(1) time complexity.

from collections import defaultdict

class Bucket(object):
    def __init__(self, rank):
        self.rank = rank
        self.keySet = set()
        self.prev = None
        self.next = None

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._keyValMap = defaultdict(int)
        self._valKeyMap = {}
        self._dummyHead = Bucket(0)
        self._dummyTail = Bucket(0)

        self._valKeyMap[0] = self._dummyHead
        self._dummyHead.next = self._dummyTail
        self._dummyTail.prev = self._dummyHead

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        # handle keyValMap
        self._keyValMap[key] += 1
        curVal = self._keyValMap[key]
        # handle valKeyMap
        self._addKeyToBucket(curVal, key)
        if curVal != 1:
            self._deleteKeyFromBucket(curVal - 1, key)
        

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self._keyValMap:
            return
        # handle keyValMap
        self._keyValMap[key] -= 1
        curVal = self._keyValMap[key]
        if curVal == 0:
            self._keyValMap.pop(key)
        # handle valKeyMap
        if curVal != 0:
            self._addKeyToBucket(curVal, key)
        self._deleteKeyFromBucket(curVal + 1, key)
        
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        maxBucket = self._dummyTail.prev
        if maxBucket.rank == 0:
            return ""
        return iter(maxBucket.keySet).next()

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        minBucket = self._dummyHead.next
        if minBucket.rank == 0:
            return ""
        return iter(minBucket.keySet).next()

    def _addKeyToBucket(self, value, key):
        # if the Bucket doesnt exist, create the bucket first
        if value not in self._valKeyMap:
            newBucket = Bucket(value)
            newBucket.rank = value
            self._valKeyMap[value] = newBucket
            prevBucket = self._valKeyMap.get(value - 1, None)
            nextBucket = self._valKeyMap.get(value + 1, None)
            if prevBucket:
                newBucket.next = prevBucket.next
                newBucket.prev = prevBucket
                prevBucket.next = newBucket
                newBucket.next.prev = newBucket
            else:
                newBucket.next = nextBucket
                newBucket.prev = nextBucket.prev
                nextBucket.prev = newBucket
                newBucket.prev.next = newBucket
        self._valKeyMap[value].keySet.add(key)

    def _deleteKeyFromBucket(self, value, key):
        deleteBucket = self._valKeyMap[value]
        deleteBucket.keySet.remove(key)
        if len(deleteBucket.keySet) == 0:
            # handle valKeyMap
            self._valKeyMap.pop(value)
            # handle the linked List
            deleteBucket.prev.next = deleteBucket.next
            deleteBucket.next.prev = deleteBucket.prev

# if __name__ == '__main__':
#     myds = AllOne()
#     print myds.getMaxKey()
#     print myds.getMinKey()
#     myds.inc("inc")
#     print myds.getMaxKey()
#     print myds.getMinKey()


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()