"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).
"""

# Key Point: Cuz time complexity should be within O(log M+N), we should
#            implement the algorithm by binary search.
#            Find median can be converted to find k-th smallest number.
#               index_short = min(len(short), )
#
# Special Case:
#            1) Two arrays separated ([1,2,3,4,5,6], [11,12,13,14,15])
#            2) Two arrays overlaped ([1,3,5,7,9,11,13], [2,4,6,8])
#            3) Equal numbers in arrays ([1,3,3,3,5,6], [2,3,3,3,3,4])
#            4) Empty array ([],[1,2,3]), ([1,2,3],[]), ([],[])
#
# Run time: 102 ms / 115ms / 139ms / 163 ms


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        leftRank = (length + 1) / 2
        rightRank = (length + 2) / 2
        return self.getRank(nums1, 0, nums2, 0, leftRank) / 2.0 + self.getRank(nums1, 0, nums2, 0, rightRank) / 2.0 

    def getRank(self, nums1, start1, nums2, start2, rank):
        if len(nums1) - start1 > len(nums2) - start2:
            return self.getRank(nums2, start2, nums1, start1, rank)
        elif len(nums1) - start1 <= 0:
            return nums2[start2 + rank - 1]
        elif rank == 1:
            return min(nums1[start1], nums2[start2])

        rank1 = min(rank / 2, len(nums1) - start1)
        rank2 = rank - rank1
        if nums1[start1 + rank1 - 1] > nums2[start2 + rank2 - 1]:
            return self.getRank(nums1, start1, nums2, start2 + rank2, rank - rank2)
        elif nums1[start1 + rank1 - 1] < nums2[start2 + rank2 - 1]:
            return self.getRank(nums1, start1 + rank1, nums2, start2, rank - rank1)
        else:
            return nums1[start1 + rank1 - 1]


if __name__ == '__main__':
    sol = Solution()
    # assert sol.findMedianSortedArrays([], [1,2,3,4,5]) == 3
    assert sol.findMedianSortedArrays([1], [2,3,4,5]) == 3
    assert sol.findMedianSortedArrays([1,2], [3,4,5]) == 3
    assert sol.findMedianSortedArrays([1,2,3], [4,5]) == 3
    assert sol.findMedianSortedArrays([1,2,3,4], [5]) == 3

    assert sol.findMedianSortedArrays([1,3], [2,4,5]) == 3
    assert sol.findMedianSortedArrays([1,4], [2,3,5]) == 3
    assert sol.findMedianSortedArrays([1,5], [2,3,4]) == 3

    assert sol.findMedianSortedArrays([2,3], [1,4,5]) == 3
    assert sol.findMedianSortedArrays([2,4], [1,3,5]) == 3
    assert sol.findMedianSortedArrays([2,5], [1,3,5]) == 3

    assert sol.findMedianSortedArrays([3,4], [1,2,5]) == 3
    assert sol.findMedianSortedArrays([3,5], [1,2,4]) == 3

    assert sol.findMedianSortedArrays([4,5], [1,2,3]) == 3
    assert sol.findMedianSortedArrays([1], [2,3,4,5]) == 3
    assert sol.findMedianSortedArrays([3], [1,2,4,5]) == 3

    assert sol.findMedianSortedArrays([1,2,3,4,5], [6,7,8,9,10]) == 5.5