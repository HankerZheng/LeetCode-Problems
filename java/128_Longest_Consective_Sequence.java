// Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

// For example,
// Given [100, 4, 200, 1, 3, 2],
// The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

// Your algorithm should run in O(n) complexity.

class UnionFind{
    public int length;
    public int[] data;
    
    public UnionFind(int givenLength){
        length = givenLength;
        data = new int[length];
        for (int i= 0; i < length; i ++){
            data[i] = -1;
        }
    }
    public int find(int a){
        if (a > length) throw new ArrayIndexOutOfBoundsException();
        Queue <Integer> childQueue = new LinkedList();
        int curIdx = a;
        while (data[curIdx] >= 0){
            childQueue.add(curIdx);
            curIdx = data[curIdx];
        }
        while (!childQueue.isEmpty()){
            int thisNode = childQueue.remove();
            data[thisNode] = curIdx;
        }
        return curIdx;
        
    }
    public void union(int a, int b){
        if ( a > length || b > length) throw new ArrayIndexOutOfBoundsException();
        int parenta = find(a);
        int parentb = find(b);
        if (parenta == parentb){
            return;
        }
        else if (data[parenta] < data[parentb]){
            data[parenta] += data[parentb];
            data[parentb] = parenta;
        }else{
            data[parentb] += data[parenta];
            data[parenta] = parentb;
        }
    }
}
public class Solution {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> indexMap = new HashMap();
        UnionFind theUF = new UnionFind(nums.length);
        for(int i = 0; i < nums.length; i ++ ){
            int thisNum = nums[i];
            if (indexMap.containsKey(thisNum)){
                continue;
            }
            if (thisNum != Integer.MIN_VALUE && indexMap.containsKey(thisNum - 1)){
                theUF.union(i, indexMap.get(thisNum-1));
            }
            if (thisNum != Integer.MAX_VALUE && indexMap.containsKey(thisNum + 1)){
                theUF.union(i, indexMap.get(thisNum+1));
            }
            indexMap.put(thisNum, i);
        }
        int longest = 0;
        for (int unionLength: theUF.data){
            longest = Math.max(longest, -unionLength);
        }
        return longest;
    }
}