// There are two sorted arrays nums1 and nums2 of size m and n respectively.

// Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

// Example 1:
// nums1 = [1, 3]
// nums2 = [2]

// The median is 2.0
// Example 2:
// nums1 = [1, 2]
// nums2 = [3, 4]

// The median is (2 + 3)/2 = 2.5


public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int length = nums1.length + nums2.length;
        int leftRank = (length + 1) / 2; // Rank is 1-base index
        int rightRank = (length + 2) / 2; // Rank is 1-base index
        return getRank(nums1, 0, nums2, 0, leftRank) / 2.0
            + getRank(nums1, 0, nums2, 0, rightRank) / 2.0;
    }
    
    public int getRank(int[] nums1, int start1, int[] nums2, int start2, int rank){
        if (nums1.length - start1 > nums2.length - start2){
            return getRank(nums2, start2, nums1, start1, rank);
        }else if (start1 >= nums1.length){
            return nums2[start2 + rank - 1];
        }else if (rank == 1){
            return Math.min(nums1[start1], nums2[start2]);
        }
        
        int rank1 = Math.min(rank / 2, nums1.length - start1);
        int rank2 = rank - rank1;
        
        if(nums1[start1 + rank1 - 1] > nums2[start2 + rank2 - 1]){
            return getRank(nums1, start1, nums2, start2 + rank2, rank - rank2);
        }else if (nums1[start1 + rank1 - 1] == nums2[start2 + rank2 - 1]){
            return nums1[start1 + rank1 - 1];
        }else{
            return getRank(nums1, start1 + rank1, nums2, start2, rank - rank1);
        }
        
    }
}