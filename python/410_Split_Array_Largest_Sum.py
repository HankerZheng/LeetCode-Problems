# 410. Split Array Largest Sum   QuestionEditorial Solution  My Submissions
# Total Accepted: 3347 Total Submissions: 11509 Difficulty: Hard Contributors: Admin
# Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

# Note:
# Given m satisfies the following constraint: 1 <= m <= length(nums) <= 14,000.

# Examples:

# Input:
# nums = [7,2,5,10,8]
# m = 2

# Output:
# 18

# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.


# BINARY SEARCH:
#       The time complexity to check whether an ans is valid is O(n)
#       Therefore, we can binary search for the ans and check valid


# MY SOLUTION:
#       If the current sum is larger than aver, stop add new element into
#       this partition, and check whether this new number should be add or not
#       Then continue to add new number
#       WHY THIS IS WRONG: This solution tries to give out an ans without traveling
#       all the elements in the list. The solution is partly optimal.

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def check_validation(target):
            cnt = 1
            this_sum = 0
            for i,num in enumerate(nums):
                if num > target:
                    return False
                this_sum += num
                if this_sum > target:
                    cnt += 1
                    this_sum = num
            if cnt > m:
                return False
            return True

        # special cases
        if not nums: return 0
        if m == 1: return sum(nums)
        if m == len(nums): return max(nums)

        total_sum = sum(nums)
        aver = total_sum / m

        start, end = aver, total_sum
        while start <= end:
            mid = (start + end) / 2
            if not check_validation(mid):
                # an invalid `ans` means that cannot create the splits
                # such that all sum is smaller or equal to `ans`
                # which means that this `ans` is too small
                start = mid + 1
            else:
                # an valid `ans` means that we could create the splits
                # such that all sum is smaller or equal to `ans`
                # store this `ans`, and make `ans` smaller
                ans = mid
                end = mid - 1
        # now we have end < start <= ans
        if check_validation(end):
            return end
        # if check_validation(start):
        #     return start
        return ans


    def splitArray_myAns(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # special cases
        if not nums: return 0
        if m == 1: return sum(nums)
        if m == len(nums): return max(nums)
        
        aver = sum(nums) / m
        this_sum = 0
        ans = 0
        
        prev_dist = aver
        for num in nums:
            this_sum += num
            if this_sum >= aver:
                # judge whther this `num` should be added or not
                if this_sum - aver < prev_dist:
                # add `num` into this partition, update this_sum and prev_dist
                    ans = max(ans, this_sum)
                    prev_dist = aver
                    this_sum = 0
                else:
                # not add `num` into this partition, this `num` should be in the next partition
                    ans = max(ans, this_sum - num)
                    prev_dist = abs(aver - num)
                    this_sum = num
            else:
                # continue to add new element to this partition
                prev_dist = aver - this_sum
        return ans
