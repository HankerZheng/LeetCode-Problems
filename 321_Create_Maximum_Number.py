# Given two arrays of length m and n with digits 0-9 representing two numbers.
# Create the maximum number of length k <= m + n from digits of the two. 
# The relative order of the digits from the same array must be preserved. 
# Return an array of the k digits.
# You should try to optimize your time and space complexity.

# Example 1:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# return [9, 8, 6, 5, 3]

# Example 2:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# return [6, 7, 6, 0, 4]

# Example 3:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# return [9, 8, 9]

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getMaxArray(nums, digitNum):
            """
            Given an array of digits, keep the original order,
            return the MAX number consists of digitNum digits.
            """
            if len(nums) < digitNum:
                return []
            ansStack = []
            idx = 0
            toRemove = len(nums) - digitNum
            while idx < len(nums):
                while ansStack and toRemove and ansStack[-1] < nums[idx]:
                    ansStack.pop(-1)
                    toRemove -= 1
                ansStack.append(nums[idx])
                idx += 1
            finalLength = len(ansStack)
            return ansStack[:finalLength - toRemove]

        def mergeArray(arr1, arr2):
            ans = []
            while arr1 or arr2:
                if arr1 > arr2:
                    ans.append(arr1.pop(0))
                else:
                    ans.append(arr2.pop(0))
            return ans

        ans = [0]
        for i in xrange(k+1):
            arr1 = getMaxArray(nums1, i)
            arr2 = getMaxArray(nums2, k - i)
            if len(arr1) + len(arr2) == k:
                thisAns = mergeArray(arr1, arr2)
                ans = max(ans, thisAns)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # print sol.maxNumber([3, 9], [8, 9], 2)
    print sol.maxNumber([6,7],[6,0,4],5)