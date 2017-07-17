# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

# [show hint]

# Related problem: Reverse Words in a String II

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def gcd(a, b):
            while a and b:
                a = a % b
                b = b % a if a != 0 else b
            return max(a, b)

        def one_round_swap(starter, stride):
            tmp = nums[starter]
            index = starter
            next = (index - stride) % len(nums)
            while next != starter:
                nums[index] = nums[next]
                index = next
                next = (index - stride) % len(nums)
            nums[index] = tmp

        if not nums:
            return
        k = k % len(nums)
        iter_count = gcd(len(nums), k)
        starter = len(nums) - 1
        for _ in xrange(iter_count):
            one_round_swap(starter, k)
            starter -= 1

if __name__ == '__main__':
    sol = Solution()
    array = range(1, 7)
    sol.rotate(array, 1)
    print array