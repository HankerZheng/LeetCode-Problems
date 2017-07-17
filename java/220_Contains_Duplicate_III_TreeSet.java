// Given an array of integers, find out whether there are two distinct indices i and j in the 
// array such that the absolute difference between nums[i] and nums[j] is at most t and the 
// absolute difference between i and j is at most k.

public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Integer> mySet = new TreeSet();
        int rmIdx = 0;
        for (int i = 0;i < nums.length; i ++) {
            int toAdd = nums[i];
            Integer lo = mySet.floor(toAdd);
            Integer hi = mySet.ceiling(toAdd);
            if (lo!=null && (long)toAdd - lo <= t){
                return true;
            }if (hi!=null && (long) hi - toAdd <= t){
                return true;
            }
            mySet.add(toAdd);
            if (mySet.size() > k){
                mySet.remove(nums[rmIdx++]);
            }
        }
        return false;
    }
}