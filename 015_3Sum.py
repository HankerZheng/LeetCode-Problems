class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		def TwoSum(sortNums, target):
			start, end = 0, len(sortNums)-1
			solution_set = []
			while start < end:
				if sortNums[start] + sortNums[end]== target:
					if not [sortNums[start] , sortNums[end]] in solution_set:
						solution_set.append([sortNums[start] , sortNums[end]])
					start, end = start +1, end -1
				elif sortNums[start] + sortNums[end] < target:
					start +=1
				else:
					end -= 1
			return solution_set
		#first sort the array
		n, sortNums= len(nums), []
		for i in xrange(n):
			sortNums.append(nums[i])
		sortNums.sort()
		#set one element in sortNums as cali, and do two sum
		solution_set = []
		for i, num in enumerate(sortNums):
			target = 0 - num
			TwoSum_solu = TwoSum(sortNums[i+1:], target)
			if len(TwoSum_solu) == 0:
				continue
			else:
				for item in TwoSum_solu:
					this_solution = [num]+item
					if not this_solution in solution_set:
						solution_set.append(this_solution)
		return solution_set

mysolu = Solution()
print mysolu.threeSum([0,0,0,2,0])