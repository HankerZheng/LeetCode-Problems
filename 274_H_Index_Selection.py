class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        def partition(nums, start, end):
            pivot = nums[start]
            left = start
            right = end
            while left < right:
                while left < right and nums[right] <= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] >= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            return left
                
        if not citations:
            return 0
        lo = 0
        hi = len(citations) - 1
        while lo <= hi:
            index = partition(citations, lo, hi)
            # condition:  h of his/her N papers have at least h citations each
            if citations[index] >= index+1:
                lo = index + 1
            else:
                hi = index - 1
        return hi + 1

if __name__ == '__main__':
    sol = Solution()
    print sol.hIndex([1,2,3,4,5,6,7])
    print sol.hIndex([1,2,3,4,5,6])
    print sol.hIndex([5,2,3,21,3,2,14,23,4,2,3,12,4,5,6,3])
    print sol.hIndex([00,0,0,0,0,0,0])
    print sol.hIndex([195,241,1592,59219,592,42])