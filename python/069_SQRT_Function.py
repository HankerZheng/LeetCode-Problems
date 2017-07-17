# Implement int sqrt(int x).

# Compute and return the square root of x.

# Key Points: Binart Search
#
# Run Time: 64 ms
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x

        start, end = 2, x
        while start <= end:
            mid = start + (end-start)/2
            this = mid*mid
            if this>x:
                end = mid-1
            elif this<x:
                start = mid+1
            else:
                return mid
        return end