# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

# Example:

# Given nums = [5, 2, 6, 1]

# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Return the array [2, 1, 1, 0].

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.smallerCnt = 0
        self.selfCnt = 1

    def insert(self, val):
        cnt = 0
        tmp = self
        while tmp:
            if val < tmp.val:
                tmp.smallerCnt += 1
                if not tmp.left:
                    tmp.left = TreeNode(val)
                    break
                tmp = tmp.left
            elif val > tmp.val:
                cnt += tmp.smallerCnt + tmp.selfCnt
                if not tmp.right:
                    tmp.right = TreeNode(val)
                    break
                tmp = tmp.right
            else:
                tmp.selfCnt += 1
                cnt += tmp.smallerCnt
                break
        return cnt
            


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:  return [0] * len(nums)
        ans = [0]
        dataTree = TreeNode(nums[-1])
        for num in nums[-2::-1]:
            ans.insert(0,dataTree.insert(num))
        return ans