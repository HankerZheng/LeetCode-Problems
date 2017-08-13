// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// push(x) -- Push element x onto stack.
// pop() -- Removes the element on top of the stack.
// top() -- Get the top element.
// getMin() -- Retrieve the minimum element in the stack.


// Runtime: 134 ms

public class MinStack {
    
    Deque<Integer> normalStack;
    Deque<Integer> minStack;
    /** initialize your data structure here. */
    public MinStack() {
        normalStack = new LinkedList<>();
        minStack = new LinkedList<>();
    }
    
    public void push(int x) {
        normalStack.addLast(x);
        if (minStack.isEmpty() || minStack.getLast() >= x) {
            minStack.addLast(x);
        }
    }
    
    public void pop() {
        int delElem = normalStack.removeLast();
        if ( !minStack.isEmpty() && minStack.getLast() == delElem) {
            minStack.removeLast();
        }
    }
    
    public int top() {
        return normalStack.getLast();
    }
    
    public int getMin() {
        return minStack.getLast();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */