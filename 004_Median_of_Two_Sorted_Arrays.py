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
# Run time: 115ms / 139ms / 163 ms


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def binary_search(nums1, nums2, rank):
            # print nums1, nums2, rank
            # rank == 1, return the smallest element
            if not nums1:
                return nums2[rank-1]
            if not nums2:
                return nums1[rank-1]
            if rank == 1:
                return min(nums1[0], nums2[0])
            longer = nums1 if len(nums1)>=len(nums2) else nums2
            shorter = nums1 if len(nums1)<len(nums2) else nums2
            rank_s = min(len(shorter), rank/2)
            # the key idea of this algorithm is this 
            # rank_l + rank_s should always be rank
            # then we could always drop the smaller element
            # because the largest rank of the smaller element could
            # only be (rank - 1) !
            rank_l = rank - rank_s
            if longer[rank_l-1] == shorter[rank_s-1]:
                return longer[rank_l-1]
            elif longer[rank_l-1] < shorter[rank_s-1]:
                # kick the smaller num out of our search range
                return binary_search(longer[rank_l:], shorter[:rank_s], rank-rank_l)
            else:
                # kick the smaller num out of our search range
                return binary_search(shorter[rank_s:], longer[:rank_l], rank-rank_s)

            
        length = len(nums1) + len(nums2)
        if length & 1:
            ranks = [length/2 + 1]
        else:
            ranks = [length/2, length/2+1]
        for i,rank in enumerate(ranks):
            if i == 0:
                res = binary_search(nums1, nums2, rank)
            else:
                res = (res + binary_search(nums1, nums2, rank))/2.0
        return res

if __name__ == '__main__':
    sol = Solution()
    assert sol.findMedianSortedArrays([], [1,2,3,4,5]) == 3
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