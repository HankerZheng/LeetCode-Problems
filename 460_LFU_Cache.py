# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LFUCache cache = new LFUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
class ListNode(object):
    
    def __init__(self, key, value, freq):
        self.key = key
        self.value = value
        self.freq = freq
        self.next = self
        self.prev = self
    
    def deleteAfter(self):
        myChild = self.next
        self.next = myChild.next
        myChild.next.prev = self
        return myChild
    
    def insertBefore(self, newNode):
        myParent = self.prev
        myParent.next = newNode
        newNode.next = self
        newNode.prev = myParent
        self.prev = newNode

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._keyMap = {}
        self._freqMap = {}
        self._lowestFreq = 0
        self._cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self._keyMap:
            thisNode = self._keyMap[key]
            self.incrementFreq(thisNode)
            return thisNode.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self._cap == 0:
            return
        if key in self._keyMap:
            thisNode = self._keyMap[key]
            thisNode.value = value
            self.incrementFreq(thisNode)
            return

        if len(self._keyMap) >= self._cap:
            victimList = self._freqMap[self._lowestFreq]
            victimNode = victimList.deleteAfter()
            self._keyMap.pop(victimNode.key)
        self._lowestFreq = 1
        newNode = ListNode(key, value, 1)
        self._freqMap[1] = self._freqMap.get(1, ListNode("dummy", "dummy", 1))
        self._freqMap[1].insertBefore(newNode)
        self._keyMap[key] = newNode
    
    def incrementFreq(self, thisNode):
        # get thisNode out of the old list
        oldFreq = thisNode.freq
        thisNode.prev.deleteAfter()
        thisNode.freq += 1
        # insert thisNode into the new list
        newFreq = thisNode.freq
        self._freqMap[newFreq] = self._freqMap.get(newFreq, ListNode("dummy", "dummy", newFreq))
        self._freqMap[newFreq].insertBefore(thisNode)
        # update lowest freq
        if self._freqMap[self._lowestFreq].next == self._freqMap[self._lowestFreq]:
            self._lowestFreq += 1
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)