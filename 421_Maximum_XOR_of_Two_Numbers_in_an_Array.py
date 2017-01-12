# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

# Could you do this in O(n) runtime?

# Example:

# Input: [3, 10, 5, 25, 2, 8]

# Output: 28

# Explanation: The maximum result is 5 ^ 25 = 28.
# Subscribe to see which companies asked this question


class Solution(object):
    def __init__(self):
        self.count = 0
    def maxXOR(self, nums):
        def take_apart(arr, index):
            mask = 1 << index
            arr0, arr1 = [], []
            for num in arr:
                if num & mask:
                    arr1.append(num)
                else:
                    arr0.append(num)
            return arr0, arr1

        def helper(nums0, nums1, index):
            # self.count += 1
            # print nums0, nums1, index
            if index == 0:
                if nums0 and nums1:
                    return nums0[0]^nums1[0]
                else:
                    return 0
            if not nums0 and not nums1:
                return 
            elif not nums0 or not nums1:
                this_arr = nums1 if nums1 else nums0
                arr0, arr1 = take_apart(this_arr, index - 1)
                return helper(arr0, arr1, index - 1)

            nums00, nums01 = take_apart(nums0, index - 1)
            nums10, nums11 = take_apart(nums1, index - 1)
            if nums00 and nums11 or nums10 and nums01:
                ans = max(helper(nums00, nums11, index - 1), helper(nums10, nums01, index - 1))
            else:
                ans = max(helper(nums00, nums10, index - 1), helper(nums01, nums11, index - 1))
            return ans


        if len(nums) <= 1:
            return 0
        max_num = max(nums)
        if max_num == 0:
            return 0
        return helper(nums, [], 31)

    def test_func(self, nums):
        ans = 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:]):
                ans = max(ans, a^b)
        return ans

if __name__ == '__main__':
    import random
    sol = Solution()
    for i in xrange(10):
        arr = []
        sol.count = 0
        for j in xrange(512):
            arr.append(random.randrange(1, 0x7fffffff))
        assert sol.maxXOR(arr) == sol.test_func(arr)
    # print sol.maxXOR([4, 8, 4, 5, 1])
    # print sol.test_func([4, 8, 4, 5, 1])