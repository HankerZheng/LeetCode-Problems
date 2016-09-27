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
#            4) Empty array ([],[1,2,3]), ([1,2,3],[]), ([],[])
#
# Run time: 163 ms


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def find_k_kp1_smallest(nums1, nums2, k):
            nums1.append(None)
            nums2.append(None)
            if k == 0:
                return (nums1[0], nums2[0]) if nums2[0] else (nums2[0], nums1[0])

            index, small = [0,0], [0,0]
            for i in xrange(k+1):
                if nums1[index[0]] is None:
                    return nums2[index[1]+k-i-1], nums2[index[1]+k-i]
                elif nums2[index[1]] is None:
                    return nums1[index[0]+k-i-1], nums1[index[0]+k-i]
                else:
                    if nums1[index[0]] < nums2[index[1]]:
                        small[0], small[1] = i+1, nums1[index[0]]
                        index[0] += 1
                    else:                    
                        small[0], small[1] = i+1, nums2[index[1]]
                        index[1] += 1

                if small[0] == k:
                    kth = small[1]
                elif small[0] == k+1:
                    kp1th = small[1]
            return kth, kp1th

        length_1 = len(nums1)
        length_2 = len(nums2)
        if not length_2 and not length_1:
            return []
        if (length_1 + length_2) & 1:
            return find_k_kp1_smallest(nums1, nums2, (length_1+length_2)/2)[1]
        else:
            (med1,med2) = find_k_kp1_smallest(nums1, nums2, (length_1+length_2)/2)
            return (med1+med2)/2.0

if __name__ == '__main__':
    sol = Solution()
    print sol.findMedianSortedArrays([13,14,15],[])