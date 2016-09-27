# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key
# if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. 
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.

# Runtime: 196/460 ms

# Implemented by Double Linked List and Hashtable
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = self
        self.prev = self
    def append_before(self, node):
        tmp = self.prev
        self.prev = node
        node.prev = tmp
        tmp.next = node
        node.next = self
    def append_after(self, node):
        tmp = self.next
        self.next = node
        node.next = tmp
        tmp.prev = node
        node.prev = self
    def delete_before(self):
        if self.prev == self:
            raise ValueError("only one node")
        tmp = self.prev.prev
        tmp.next = self
        self.prev = tmp
    def delete_after(self):
        if self.next == self:
            raise ValueError("only one node")
        tmp = self.next.next
        tmp.prev = self
        self.next = tmp

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.c_size = 0
        self.history = ListNode('dummy')
        self.hashtable = {}
        self._data = {}   

    def _update_history(self, key):
        if self.hashtable.get(key, None) is None:
            # this key is not in the hashtable
            # create the node and append to history
            this_node = ListNode(key)
            self.hashtable[key] = this_node
            self.history.append_before(this_node)
        else:
            # this key is already in the hashtable
            # delete the old node from history and then append it
            this_node = self.hashtable[key]
            this_node.next.delete_before()
            self.history.append_before(this_node)

    def get(self, key):
        """
        :rtype: int
        """
        if self._data.get(key, None) is None:
            return -1
        else:
            self._update_history(key)
        return self._data.get(key)
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing 
        """
        if self._data.get(key,-1) == -1:
            # the key doesn't exist, we need to add new data
            if self.c_size == self.capacity:
                # the cache is full, need to delete one node
                tobeDelete = self.history.next
                self.history.delete_after()
                self.hashtable.pop(tobeDelete.val)
                self._data.pop(tobeDelete.val)
            else:
                # update the size counter
                self.c_size += 1
            # add new data
            self._update_history(key)
            self._data[key] = value
        else:
            # update old value
            self._update_history(key)
            self._data[key] = value




# Implement by List
class LRUCache_On_List_sol(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.c_size = 0
        self.history = []
        self._data = {}
        

    def get(self, key):
        """
        :rtype: int
        """
        if self._data.get(key, None) is None:
            return -1
        else:
            self.history.remove(key)
            self.history.append(key)
        return self._data.get(key)
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self._data.get(key,-1) == -1:
            if self.c_size == self.capacity:
                # first delete the LRU data
                delkey = self.history.pop(0)
                self._data.pop(delkey)
                # then add new data
                self._data[key] = value
                self.history.append(key)

            else:
                # add new data
                self.c_size += 1
                self.history.append(key)
                self._data[key] = value
        else:
            # update old value
            self._data[key] = value
            self.history.remove(key)
            self.history.append(key)