# Given an array of integers, every element appears three times except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Subscribe to see which companies asked this question


# Runtime: 252/84ms
class Solution(object):
    def singleNumber(self, nums):
        def convert2base10(num):
            ans = 0
            for i in xrange(len(num)):
                ans = ans*3 + num[i]
            return ans
        def convert2base3(num):
            if num == 0:
                return [0]
            flag = num>=0
            tmp = num
            ans = []
            if not flag:
                tmp = -num
            while tmp > 0:
                ans.insert(0, tmp%3)
                tmp = tmp/3
            if flag:
                return ans+[0]
            else:
                return ans+[1]
        def xor_base3(num1, num2):
            l1, l2 = len(num1), len(num2)
            ans = []
            if l1>l2:
                num2 = [0]*(l1-l2)+num2
            else:
                num1 = [0]*(l2-l1)+num1
            for i,_ in enumerate(num1):
                ans.append((num1[i]+num2[i])%3)
            return ans
        res = [0]
        for num in nums:
            res = xor_base3(res, convert2base3(num))
        flag = res.pop(-1)
        print res
        res = convert2base10(res)
        if flag:
            return -res
        return res


    def singleNumber_sumup(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mysum = 0
        i = 31
        while i >= 0:
            ans = 0
            mask = 1<<i
            for num in nums:
                if num&mask:
                    ans += 1
            mysum = (mysum<<1) + (ans%3)
            i-=1
        if mysum&(1<<31):
            return -((mysum^0xffffffff)+1)
        else:
            return mysum

if __name__ == '__main__':
    sol = Solution()
    print sol.singleNumber([2])
    print sol.singleNumber([2,2,3,2])
    print sol.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])