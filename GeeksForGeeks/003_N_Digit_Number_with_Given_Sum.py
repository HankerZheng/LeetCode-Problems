# Reference: http://www.geeksforgeeks.org/count-of-n-digit-numbers-whose-sum-of-digits-equals-to-given-sum/
# Given two integers 'n' and 'sum', find count of all n digit numbers with sum of digits as 'sum'. Leading 0's are not counted as digits.
# 1 <= n <= 100 and 1 <= sum <= 50000

# Example:

# Input:  n = 2, sum = 2
# Output: 2
# Explanation: Numbers are 11 and 20

# Input:  n = 2, sum = 5
# Output: 5
# Explanation: Numbers are 14, 23, 32, 41 and 50

# Input:  n = 3, sum = 6
# Output: 21

def numberWithGivenSum(n, target):
    def getCount(n, target):
        if n == 1:
            return int(0 <= target < 10)
        elif n*9 < target:
            return 0
        elif target < 0:
            return 0
        if (n, target) in history:
            return history[(n, target)]

        thisCnt = 0
        for i in xrange(max(10, target)):
            thisCnt += getCount(n - 1, target - i)
        history[(n, target)] = thisCnt
        return thisCnt


    if n == 1:
        return int(0 <= target < 10)
    elif n*9 < target:
        return 0
    cnt = 0
    history = {}
    # handle the condition for the first digit without leading 0
    for i in xrange(1, max(10, target)):
        cnt += getCount(n - 1, target - i)
    return cnt

if __name__ == '__main__':
    assert numberWithGivenSum(2, 2) == 2
    assert numberWithGivenSum(2, 5) == 5
    assert numberWithGivenSum(3, 6) == 21