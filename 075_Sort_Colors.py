# Given an array with n objects colored red,
# white or blue, sort them so that objects of
# the same color are adjacent, with the colors
# in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to
# represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.

# Runtime: 68/48 ms
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]

        left, right, pos = -1,len(nums), 0
        while pos < right:
            while nums[pos]!=1 and pos>left and pos<right:
                if nums[pos] == 0:
                    swap(pos, left+1)
                    left+=1
                if nums[pos] == 2:
                    swap(pos, right-1)
                    right-=1
            pos+=1


    def sortColors_Bad(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = {0:0, 1:0, 2:0}
        for num in nums:
            count[num]+=1
        nums[:count[0]] = [0] * count[0]
        nums[count[0]: count[0]+count[1]] = [1]*count[1]
        nums[count[0]+count[1]:] = [2]*count[2]


if __name__ == '__main__':
    sol = Solution()
    tests = [[0,2,1,0,1,2,2,2,1,0],
             [],
             [1],
             ]
    for test in tests:
        sol.sortColors(test)
    print tests