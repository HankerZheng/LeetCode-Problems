'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Subscribe to see which companies asked this question
'''
import sys, bisect

class Solution(object):

	# after peeking the best sol in discusion
	# by using bisect.bisect_left to prune the unnecessary leaves
	# this sol takes only 54 ms
    def threeSumClosest_fastest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    sort_nums, ans, length = sorted(list(nums)), sys.maxint, len(nums)
    for i in xrange(length - 2):
    	if sort_nums[i] > target + abs(ans - target):
    		break
    	end   = length- 1
    	start = bisect.bisect_left(sort_nums, target - sort_nums[end] - sort_nums[i], i+1, end) -1
    	start += (start == i)
    	while start < end:
    		this_value = sort_nums[i] + sort_nums[start] + sort_nums[end]
    		if abs(this_value - target) < abs(ans - target):
    			ans = this_value
    		if this_value > target:
    			end -= 1
    		elif this_value == target:
    			return this_value
    		else: 
    			start += 1
    return ans

# by using lambda, the time rises. 
# because lambda is a function call, and in lambda abs is also a function call
# this sol takes 340 ms
    def threeSumClosest_with_lambda(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sort_nums, n, ans = sorted(nums), len(nums), float('inf')
        get_dist = lambda x: abs(x-target)

        for i in xrange(n-2):
        	if sort_nums[i] > target + get_dist(ans):
        		break
        	start, end = i+1,  n - 1
        	while start < end:
        		this_value = sort_nums[i] + sort_nums[start] + sort_nums[end]
        		if this_value == target:
        			return this_value
        		ans = min(this_value, ans, key = get_dist)
        		end -= this_value > target
        		start += this_value < target
        return ans

# the original sol
# this sol takes 144 ms
    def threeSumClosest_original(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sort_nums, ans, length = sorted(list(nums)), sys.maxint, len(nums)
        for i in xrange(length - 2):
        	if sort_nums[i] > target + abs(ans - target):
        		break
        	start, end = i+1, length- 1
        	while start < end:
        		this_value = sort_nums[i] + sort_nums[start] + sort_nums[end]
        		if abs(this_value - target) < abs(ans - target):
        			ans = this_value
        		if this_value > target:
        			end -= 1
        		elif this_value == target:
        			return this_value
        		else: 
        			start += 1
        return ans
