# Given two sorted integer arrays nums1 and nums2,
# merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size
#     that is greater or equal to m + n) to hold additional
# elements from nums2. The number of elements initialized in
# nums1 and nums2 are m and n respectively.

# Runtime: 60 ms
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        posi = len(nums1)-1
        p1, p2 = m-1, n-1
        while p1>=0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[posi]=nums1[p1]
                p1-=1
                posi-=1
            else:
                nums1[posi]=nums2[p2]
                p2-=1
                posi-=1
        if p2>=0:
            nums1[:p2+1] = nums2[:p2+1]



if __name__ == '__main__':
    sol = Solution()
    nums1 = [2,2,4,0,0]
    sol.merge(nums1,3,[1,3],2)
    print nums1