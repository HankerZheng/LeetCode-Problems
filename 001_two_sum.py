'''
Total Accepted: 179927 Total Submissions: 869560 Difficulty: Medium
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

Subscribe to see which companies asked this question
'''
class Solution(object):
	#first solution by sort and search from two ends
    def twoSum_sort_and_search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

   		#List.sort() sort the list at original address
   		#thus, we have to make some arrengement before call sort()
        n = len(nums)
        sortNums = []
        	#xrange() returns a generator, more efficient than range(), which returns an array
        for i in xrange(n):
        	sortNums.append((nums[i],i + 1))
        sortNums.sort()
        #or, we can just call sortNums = sorted(nums)
        #    and use nums.index(sortNums[i]) gets its original position
        #	 but in this case, repeatitions are allowed, this methods is inadmisible

        start, end = 0, n-1
        while end > start:
        	if sortNums[start][0] + sortNums[end][0] == target:
        		if sortNums[start][1] < sortNums[end][1]:
        			return sortNums[start][1], sortNums[end][1] 
        		else:
        			return sortNums[end][1], sortNums[start][1] 
        	elif sortNums[start][0] + sortNums[end][0] < target:
        		start += 1
        	else:
        		end -= 1
        return None

    #second solution by hashtable
	def twoSum(self, nums, target):
		hashtable = dict()
		for i, item in enumerate(nums):
			if hashtable.has_key(target - item):
				return hashtable.get(target - item), i
			else:
				hashtable.update({item:i})

