// Design a Phone Directory which supports the following operations:

// get: Provide a number which is not assigned to anyone.
// check: Check if a number is available or not.
// release: Recycle or release a number.


// array is much faster than hashSet in this case because the number here is one integer

// Runtime: 346 ms

public class PhoneDirectory {
    
    Deque<Integer> unused;
    boolean[] used;

    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    public PhoneDirectory(int maxNumbers) {
        used = new boolean[maxNumbers];
        unused = new LinkedList<Integer>();
        for (int i = 0; i < maxNumbers; i ++) {
            unused.addLast(i);
        }
    }
    
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    public int get() {
        if (unused.size() == 0) return -1;
        int retNum = unused.removeFirst();
        used[retNum] = true;
        return retNum;
    }
    
    /** Check if a number is available or not. */
    public boolean check(int number) {
        return !used[number];
    }
    
    /** Recycle or release a number. */
    public void release(int number) {
        if (used[number]) {
            used[number] = false;
            unused.addLast(number);
        }
    }
}

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj.get();
 * boolean param_2 = obj.check(number);
 * obj.release(number);
 */