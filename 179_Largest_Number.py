# Given a list of non negative integers, arrange them such that they form the largest number.

# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question

# Show Tags

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def mycmp(a,b):
            return cmp(str(b)+str(a), str(a)+str(b))
        nums.sort(cmp=mycmp)
        ans = []
        for num in nums:
            ans.append(str(num))
        while ans and ans[0] == "0":
            ans.pop(0)
        if not ans:
            return 0
        return "".join(ans)

if __name__ == '__main__':
    sol = Solution()
    print sol.largestNumber([60,12,9,2])
    print sol.largestNumber([0,0])
    print sol.largestNumber([])