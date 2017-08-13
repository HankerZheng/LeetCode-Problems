// Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

// get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
// put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

// Follow up:
// Could you do both operations in O(1) time complexity?

// Example:

// LRUCache cache = new LRUCache( 2 /* capacity */ );

// cache.put(1, 1);
// cache.put(2, 2);
// cache.get(1);       // returns 1
// cache.put(3, 3);    // evicts key 2
// cache.get(2);       // returns -1 (not found)
// cache.put(4, 4);    // evicts key 1
// cache.get(1);       // returns -1 (not found)
// cache.get(3);       // returns 3
// cache.get(4);       // returns 4


// Runtime: 138 ms


public class LRUCache {
    
    private ListNode head; // point to the dummy node, whose next node is LRU
    private ListNode tail; // point to the MRU node
    private Map<Integer, ListNode> cache;
    private int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.head = new ListNode(-1, -1);
        this.tail = this.head;
    }
    
    public int get(int key) {
        int res = -1;
        if (cache.containsKey(key)) {
            ListNode thisNode = cache.get(key);
            res = thisNode.val;
            updateNode(thisNode.key, thisNode.val);
        }
        return res;
    }
    
    public void put(int key, int val) {
        if (cache.containsKey(key)) {
            updateNode(key, val);
        } else if (cache.size() < capacity) {
            addNode(key, val);
        } else {
            removeNode();
            addNode(key, val);
        }
    }
    
    private void updateNode(int key, int val) {
        ListNode thisNode = cache.get(key);
        thisNode.val = val;
        // If current node is already MRU, just return
        if (thisNode.next == null) return;
        // Remove thisNode from the list
        ListNode nextNode = thisNode.next;
        thisNode.key = nextNode.key;
        thisNode.val = nextNode.val;
        thisNode.next = nextNode.next;
        cache.put(thisNode.key, thisNode);
        if (nextNode == this.tail) {
            this.tail = thisNode;
        }
        // Move nextNode to the tail of the list
        nextNode.key = key;
        nextNode.val = val;
        nextNode.next = null;
        this.tail.next = nextNode;
        this.tail = nextNode;
        cache.put(key, nextNode);
    }
    
    private void removeNode() {
        ListNode rmNode = head.next;
        head.next = rmNode.next;
        cache.remove(rmNode.key);
    }
    
    private void addNode(int key, int val) {
        ListNode newNode = new ListNode(key, val);
        this.tail.next = newNode;
        this.tail = newNode;
        cache.put(key, newNode);
    }
    
}

class ListNode {
    public ListNode next;
    public int key;
    public int val;
    public ListNode(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */