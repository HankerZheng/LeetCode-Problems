import java.util.*;

class Bucket{
    public int rank;
    public Set <String> keySet;
    public Bucket next;
    public Bucket prev;
    public Bucket(int cnt){
        rank = cnt;
        keySet = new HashSet();
        next = null;
        prev = null;
    }
}

public class AllOne {
    /** Initialize your data structure here. */
    private Map <String, Integer> keyValMap;
    private Map <Integer, Bucket> valKeyMap;
    private Bucket dummyHead;
    private Bucket dummyTail;

    public AllOne() {
        keyValMap = new HashMap();
        valKeyMap = new HashMap();
        dummyHead = new Bucket(0);
        dummyTail = new Bucket(0);
        dummyHead.next = dummyTail;
        dummyTail.prev = dummyHead;
        valKeyMap.put(0, dummyHead);
    }
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    public void inc(String key) {
        // update keyValMap
        keyValMap.put(key, keyValMap.getOrDefault(key, 0) + 1);
        int curVal = keyValMap.get(key);
        // update valKeyMap,  delete should after add
        addToBucket(key, curVal);
        if (curVal != 1){
            deleteFromBucket(key, curVal - 1);
        }
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    public void dec(String key) {
        // update keyValMap
        if (! keyValMap.containsKey(key)){
            return;
        }
        keyValMap.put(key, keyValMap.get(key) - 1);
        int curVal = keyValMap.get(key);
        if (curVal == 0){
            keyValMap.remove(key);
        }
        // update valKeyMap, delete should after add
        if (curVal != 0){
            addToBucket(key, curVal);
        }
        deleteFromBucket(key, curVal + 1);
    }
    
    /** Returns one of the keys with maximal value. */
    public String getMinKey() {
        Bucket minBucket = dummyHead.next;
        if (minBucket.rank == 0){
            return "";
        }
        return minBucket.keySet.iterator().next();
    }
    
    /** Returns one of the keys with Minimal value. */
    public String getMaxKey() {
        Bucket maxBucket = dummyTail.prev;
        if (maxBucket.rank == 0){
            return "";
        }
        return maxBucket.keySet.iterator().next();        
    }

    private void deleteFromBucket(String key, int value){
        Bucket delBucket = valKeyMap.get(value);
        delBucket.keySet.remove(key);
        if (delBucket.keySet.size() == 0){
            delBucket.prev.next = delBucket.next;
            delBucket.next.prev = delBucket.prev;
            valKeyMap.remove(value);
        }
    }

    private void addToBucket(String key, int value){
        if(!valKeyMap.containsKey(value)){
            Bucket prevBucket = valKeyMap.get(value - 1);
            Bucket nextBucket = valKeyMap.get(value + 1);
            Bucket newBucket = new Bucket(value);
            valKeyMap.put(value, newBucket);
            if (prevBucket == null){
                // insert the new bucket before nextBucket
                newBucket.prev = nextBucket.prev;
                newBucket.next = nextBucket;
                nextBucket.prev = newBucket;
                newBucket.prev.next = newBucket;
            }else{
                // insert the new bucket after prevBucket
                newBucket.prev = prevBucket;
                newBucket.next = prevBucket.next;
                prevBucket.next = newBucket;
                newBucket.next.prev = newBucket;
            }
        }
        valKeyMap.get(value).keySet.add(key);
    }

    // public static void main(String[] args) {
    //     AllOne myds = new AllOne();
    //     myds.inc("a");
    //     myds.inc("b");
    //     myds.inc("b");
    //     myds.inc("b");
    //     myds.inc("b");
    //     myds.inc("b");
    //     myds.dec("c");
    //     myds.dec("b");
    //     // myds.dec("b");
    //     System.out.println(myds.getMaxKey() + " == b");
    //     System.out.println(myds.getMinKey() + " == a");

    // }

}
/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * String param_3 = obj.getMaxKey();
 * String param_4 = obj.getMinKey();
 */