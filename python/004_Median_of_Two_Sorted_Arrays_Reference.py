"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).
"""

# Key Point: Cuz time complexity should be within O(log M+N), we should
#            implement the algorithm by binary search.
#            Find median can be converted to find k-th smallest number.
#
# Special Case:
#            1) Two arrays separated ([1,2,3,4,5,6], [11,12,13,14,15])
#            2) Two arrays overlaped ([1,3,5,7,9,11,13], [2,4,6,8])
#            3) Equal numbers in arrays ([1,3,3,3,5,6], [2,3,3,3,3,4])
#
# Run time: 163 ms


class Solution(object):
    def helper(self, nums1, nums2, target):
        """
        return the target-th smallest num of nums1 and nums2
        target = 0 means to return smallest num

        In the for-loop, target is used as count
        """
        start1 = 0
        start2 = 0
        while(1):
            # if one lists overflow, then result is in the other list
            if start1 >= len(nums1):
                return nums2[target+start2]
            elif start2 >= len(nums2):
                return nums1[target+start1]

            if target ==0:
                return min(nums2[start2], nums1[start1])
            # move two pointers target//2 steps forward
            p1 = min((target-1)//2 + start1, len(nums1)-1)
            p2 = min((target-1)//2 + start2, len(nums2)-1)
            v1 = nums1[p1]
            v2 = nums2[p2]
            # THE larger one must be larger than or equal to (start+target/2)-th
            # smallest number in nums1 and nums2. THE smaller one must be smaller than
            # or equal to (start+target)-th smallest number.
            #
            #                       +--= (start+target/2)-th smallest
            #      smaller =--+     |       +--= larger one
            #                 |     |       |
            #  +--------------+-----+-------+-------------+  <- combined nums
            #
            print v1, v2, target
            if v1 <= v2:
                target = target-(p1-start1+1)
                start1= p1+1
            else:
                target = target-(p2-start2+1)
                start2 = p2+1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.l1 = len(nums1)
        self.l2 = len(nums2)
        l1 = self.l1
        l2 = self.l2
        if (l1+l2) & 1:
            return self.helper(nums1,nums2,(l1+l2)//2)
        else:
            r = self.helper(nums1,nums2,(l1+l2)//2) 
            l = self.helper(nums1,nums2,(l1+l2)//2 -1)
            return (l+r) *1.0/2;

if __name__ == "__main__":
    sol = Solution()
    print sol.helper([0,2,4,5,6,7,11,13],[1,3,8,9,10,12,14,15,16], 10)