class Solution(object):

	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) <= 1:
			return len(nums)
		ans, swap, length = 1,1,len(nums)
		while ans+swap < length:
			if nums[ans] == nums[ans+swap]:
				swap += 1
			else:
				nums[ans] = nums[ans+swap]
				ans+=1
				swap+=1
		return nums[:ans], ans
	# this sol takes 96 ms, beating 48.22%
	def removeDuplicates_improved(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) <= 1:
			return len(nums)
		i, old, same, length = 1, nums[0], 0, len(nums)
		while i < length:
			while same+i < length and nums[same+i] == old :
				same += 1
			old = nums[same+i] if same+i < length else nums[0]
			nums[i] = old
			i+=1
		return length - same

	# this sol takes 144 ms, beating 12.00%
	def removeDuplicates_original(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
		    return 0
		i, old = 1, nums[0]
		while i < len(nums):
			if old == nums[i]:
				del nums[i]
				continue
			old = nums[i]
			i+=1
		return len(nums)

sol = Solution()
print sol.removeDuplicates([1,1,1,2,2,3,4,5,5,5])