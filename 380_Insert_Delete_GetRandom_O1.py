# Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
# Example:

# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();

# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);

# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);

# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);

# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();

# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);

# // 2 was already in the set, so return false.
# randomSet.insert(2);

# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();


import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data = []
        self._indexMapping = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self._indexMapping:
            return False
        self._data.append(val)
        self._indexMapping[val] = len(self._data) - 1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self._indexMapping:
            return False
        thisIndex = self._indexMapping[val]
        self._swap(thisIndex, len(self._data) - 1)
        self._removeLastElement()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        randomIndex = random.randrange(len(self._data))
        return self._data[randomIndex]
    
    def _swap(self, index1, index2):
        value1, value2 = self._data[index1], self._data[index2]
        self._indexMapping[value1] = index2
        self._indexMapping[value2] = index1
        self._data[index1] = value2
        self._data[index2] = value1
    
    def _removeLastElement(self):
        lastValue = self._data.pop(-1)
        self._indexMapping.pop(lastValue)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()