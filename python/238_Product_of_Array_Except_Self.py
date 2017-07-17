class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        if nums == [0]:
            return [1]
        first = [1 for num in nums]
        second = [1 for num in nums]
        res = [0 for num in nums]
        for i,num in enumerate(nums):
            if i == 0:
                first[i] = 1
            elif i == 1:
                first[i] = nums[i-1]
            else:
                first[i] = first[i-1]*nums[i-1]
        while i >= 0:
            if i == len(nums)-1:
                second[i] = 1
            elif i == len(nums)-2:
                second[i] = nums[i+1]
            else:
                second[i] = second[i+1]*nums[i+1]
            i -= 1
        for i,num in enumerate(nums):
            res[i] = first[i] * second[i]
        # print first, second
        return res

if __name__ == '__main__':
    sol = Solution()
    # print sol.productExceptSelf([0,0])
    # print sol.productExceptSelf([1,0])
    print sol.productExceptSelf([9,0,-2])