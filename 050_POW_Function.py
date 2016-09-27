# Implement pow(x, n).

# Subscribe to see which companies asked this question

# Key Points: Binary
# Time Complexity: O(log N)
# Run time: 48 ms

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 or x==1:
            return 1.0
        if x == 0:
            return 0.0        
        if n < 0:
            x = 1.0/x
            n = -n

        fact, power = 1, n
        this_x = x
        while power>1:
            if power&1:
                fact *=this_x
            if power>>1:
                this_x *=this_x
            power = power >> 1
        return float(this_x)*fact

if __name__ =="__main__":
    test = Solution()
    query = [
        (0,0), # 1
        (0,1), # 0
        (1,12), # 1
        (1,100), # 1
        (2,1), # 2
        (2,2), # 4
        (2,3), # 8
        (2,4), # 16
        (2,-5) # 0.03125
    ]
    for q in query:
        x,n = q
        ans = test.myPow(x,n)
        print ans