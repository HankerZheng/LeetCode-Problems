# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


# Runtime: 116 ms
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        self._min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._data.append(x)
        if not self._min_stack:
            self._min_stack.append(x)
        elif self._min_stack and x <= self._min_stack[-1]:
            self._min_stack.append(x) 

    def pop(self):
        """
        :rtype: void
        """
        if not self._data:
            return None
        res = self._data.pop(-1)
        if res == self._min_stack[-1]:
            self._min_stack.pop(-1)
        return res

    def top(self):
        """
        :rtype: int
        """
        if not self._data:
            return None
        return self._data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self._min_stack:
            return None
        return self._min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()