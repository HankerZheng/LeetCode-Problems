# Find the contiguous subarray within an array (containing at least one
# number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems

# Runtime: 79 ms

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_product = nums[0]
        old = [nums[0], nums[0]]
        for i,num in enumerate(nums):
            if i == 0:
                continue
            tmp1 = max(old[0]*num, old[1]*num, num)
            tmp2 = min(old[0]*num, old[1]*num, num)
            old = [tmp1, tmp2]
            max_product = max(old[0], old[1], max_product)
        return max_product

if __name__ == '__main__':
    sol = Solution()
    # print sol.maxProduct([1,-1, 1,-1])
    # print sol.maxProduct([])
    # print sol.maxProduct([2,3,-2,4])
    print sol.maxProduct([-4, -3, -2])
            