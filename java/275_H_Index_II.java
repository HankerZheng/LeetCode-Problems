public class Solution {
    public int hIndex(int[] citations) {
        if (citations == null || citations.length == 0) return 0;
        if (citations[citations.length-1] == 0) return 0;
        if (citations[0] >= citations.length) return citations.length;
        
        int lo = 1, hi = citations.length - 1;
        while (lo <= hi){
            int h_index = lo + (hi - lo) / 2;
            boolean condition1 = citations[citations.length - h_index] >= h_index;
            if (!condition1){
                hi = h_index - 1;
                continue;
            }
            boolean condition2 = citations[citations.length - h_index - 1] <= h_index;
            if (!condition2){
                lo = h_index + 1;
                continue;
            }else{
                return h_index;
            }
            
        }
        return 0;
    }
}