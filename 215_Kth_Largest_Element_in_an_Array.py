"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 <= k <= array's length.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
"""

#
# Key Points: Heap. Maintain a heap with size k.
#
# Run time: 68 ms

from heapq import *

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Time complexity: average O(n)
        """
        def selection(start, end, k):
            print start, end, k
            # termination condition
            if end - start < 5:
                lst = nums[start:end + 1]
                lst.sort(reverse=True)
                return lst[k - 1]
            # recursive body
            pivot = median3(start, end)
            left, right = start, end
            while left < right:
                while left < right and nums[right] <= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] >= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            rank = left - start + 1
            if rank == k:
                return nums[left]
            elif rank < k:
                return selection(left + 1, end, k - rank)
            else:
                return selection(start, left - 1, k)
        
        def median3(start, end):
            mid = (start + end) /2
            lst = [nums[start], nums[mid], nums[end]]
            lst.sort()
            nums[start], nums[mid], nums[end] = lst[1], lst[2], lst[0]
            return nums[start]
        
        return selection(0, len(nums) - 1, k)

    def findKthLargest_heap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Time Complexity: O(k) + O(k logk)
        """
        if nums is None:
            return None

        if k==1:
            return max(nums)
        if k==len(nums):
            return min(nums)

        heap = nums[:k]
        heapify(heap)
        for item in nums[k:]:
            if item > heap[0]:
                heapreplace(heap, item)
        return heap[0]

if __name__ == '__main__':
    sol = Solution()
    print sol.findKthLargest([7,6,5,4,3,2], 2)