# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self._data = nestedList
        self._cursor = [0]
        self._length = [len(nestedList)]
        self._next = None
        
    # @return {int} the next element in the iteration
    def next(self):
        return self._next
    def get_next(self):
        # get the data
        this_data = self._data
        for index in self._cursor:
            if isinstance(this_data, list):
                this_data = this_data[index]
            else:
                this_data = this_data.getList()[index]
        while this_data.getList():
            # if this_data is a list
            self._cursor.append(0)
            self._length.append(len(this_data.getList()))
            this_data = this_data.getList()[0]
        # update cursor
        while self._cursor and self._cursor[-1] == self._length[-1] - 1:
            self._cursor.pop(-1)
            self._length.pop(-1)
        if self._cursor:
            self._cursor[-1] += 1
        else:
            self._cursor = [-1]

        self._next = this_data.getInteger()
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        if not self._data or self._cursor == [-1]:
            return False

        self.get_next()
        while self._next is None:
            if not self._data or self._cursor == [-1]:
                return False
            self.get_next()
        return True



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# if __name__ == '__main__':
#     sol = NestedIterator([1,2,[3,4,5,[4,6],6],7])
#     while sol.hasNext():
#         print sol.next()
#     sol = NestedIterator([[[[[0]]]]])
#     while sol.hasNext():
#         print sol.next()