'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
Subscribe to see which companies asked this question
'''
import bisect
class Solution(object):
	# two pointer do exhaustive and the other two do bi-search
	# add into limit 
	# limits have done the function that bisect should do
	# this sol only takes 156ms
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		sort_nums, length, ans, limit = sorted(nums), len(nums), [], target >> 2
		low1, high1 = 0, length - 1
		for low1 in xrange(length - 3):
			if sort_nums[low1] > limit:
				break
			if low1 != 0 and sort_nums[low1] == sort_nums[low1-1]:
				continue
			for high1 in xrange(length - 1, low1+2, -1):
				if sort_nums[high1] < limit:
					break
				if high1 != length - 1 and sort_nums[high1] == sort_nums[high1 + 1]:
					continue
				high2 = high1 - 1
				low2 = low1 + 1
				limit1 = (target - sort_nums[high1] - sort_nums[low1])>>1
				while low2 < high2 and sort_nums[low2] <= limit1 and sort_nums[high2] >= limit1: 
					thisvalue =  sort_nums[high1] + sort_nums[low1] + sort_nums[high2] + sort_nums[low2]
					if thisvalue == target:
						ans.append([sort_nums[low1] , sort_nums[low2] ,sort_nums[high2] , sort_nums[high1]])
						low2 += 1
						high2 -= 1
						while low2<high2 and sort_nums[high2] == sort_nums[high2+1]:
							high2 -= 1
						while low2<high2 and sort_nums[low2] == sort_nums[low2-1]:
							low2 += 1
					low2 += thisvalue < target
					high2 -= thisvalue > target
		return ans


	# two pointer do exhaustive and the other two do bi-search
	# this sol takes 964 ms
	def fourSum_original(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		import bisect
		sort_nums, length, ans= sorted(nums), len(nums), []
		for i in xrange(length-3):
			if sort_nums[length - 1] + sort_nums[length - 2] + sort_nums[length - 3] + sort_nums[i] < target:
				continue
			for j in xrange(i+1,length-2):
				if sort_nums[length - 1] + sort_nums[length - 2] + sort_nums[j] + sort_nums[i] < target:
					continue
				left, high= target - sort_nums[i] - sort_nums[j] - sort_nums[length - 1], length - 1
				low = bisect.bisect_left(sort_nums, left, j+1, length - 1) - 1
				low += (low == j)
				while low < high:
					thisvalue = sort_nums[low] + sort_nums[high] + sort_nums[i] + sort_nums[j]
					if thisvalue < target:
						low += 1
					elif thisvalue > target:
						high -= 1
					else:
						thistuple = [sort_nums[i], sort_nums[j], sort_nums[low], sort_nums[high]]
						if not thistuple in ans:
							ans.append(thistuple)
						low += 1
						high -= 1
		return ans

if __name__ == '__main__':
	a = Solution()
	print a.fourSum([-5,5,4,-3,0,0,4,-2],4)
	print a.fourSum_original([-5,5,4,-3,0,0,4,-2],4)