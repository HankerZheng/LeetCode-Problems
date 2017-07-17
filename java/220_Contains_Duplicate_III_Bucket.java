public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (nums.length == 0 || t < 0)  return false;
        int rmIdx = 0;
        Map<Integer, Integer> buckets = new HashMap();
        for (int i = 0; i < nums.length; i ++){
            int toAdd = nums[i];
            int bucketNum = getBucketNum(toAdd, t+1);
            if (buckets.containsKey(bucketNum))    return true;
            if (buckets.containsKey(bucketNum+1) && (long) buckets.get(bucketNum+1) - toAdd <= t){
                return true;
            }if (buckets.containsKey(bucketNum-1) && (long) toAdd - buckets.get(bucketNum-1) <= t){
                return true;
            }
            buckets.put(bucketNum, toAdd);
            if (buckets.size() > k){
                buckets.remove(nums[rmIdx++] / (t + 1));
            }
        }
        return false;
    }
    public int getBucketNum(int num, int base){
        return num >= 0 ? num / base: (num+1) / base - 1;
    }
}