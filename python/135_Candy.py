# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Subscribe to see which companies asked this question


# Key Point: to find the consecutive monotonic subarray.


class Solution(object):
    def candy(self, ratings):
        if len(ratings) <= 1:
            return len(ratings)
        pre = 0
        count = 0
        peak = 1
        for i, rate in enumerate(ratings):
            if i == 0:
                count += 1
                pre = 1
            elif ratings[i-1] < rate:
                pre += 1
                count += pre
            elif ratings[i-1] == rate:
                count += peak
                pre = peak
            else:
                pre -= 1
                count += pre
                peak = min(pre, peak)
        return count + len(ratings)*(1-peak)

    def candy_TLE(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        def memo_search(index):
            if dp[index] != 0:
                return dp[index]
            # the case that dp[i] == 1
            if index == 0 and ratings[index] <= ratings[index+1]:
                dp[index] = 1
            elif index == len(ratings)-1 and ratings[index-1] >= ratings[index]:
                dp[index] = 1
            elif 0<index<len(ratings)-1 and ratings[index-1] >= ratings[index] <= ratings[index+1]:
                dp[index] = 1
            # other cases
            elif index == 0 and ratings[index] > ratings[index+1]:
                dp[index] = memo_search(index+1) + 1
            elif index == len(ratings)-1 and ratings[index-1] < ratings[index]:
                dp[index] = memo_search(index-1) + 1

            elif ratings[index-1] < ratings[index] <= ratings[index+1] or ratings[index-1] <= ratings[index] < ratings[index+1]:
                dp[index] = memo_search(index-1) + 1
            elif ratings[index-1] > ratings[index] >= ratings[index+1] or ratings[index-1] >= ratings[index] > ratings[index+1]:
                dp[index] = memo_search(index+1) + 1
            else:
                dp[index] = max(memo_search(index-1), memo_search(index+1)) + 1
            return dp[index]

        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1
        dp = [0 for i in ratings]
        for i, rate in enumerate(ratings):
            memo_search(i)
        return sum(dp)

if __name__ == '__main__':
    sol = Solution()
    assert sol.candy([1,2,3]) == 6
    assert sol.candy([9,8,7,7,6,5]) == 12
    assert sol.candy([2,3,2]) == 4
    assert sol.candy([1,0,2]) == 5
    assert sol.candy([4,3,2,3,4]) == 11
    assert sol.candy([1,3,4,3,2,1]) == 13
    assert sol.candy([1,2,4,4,2]) == 9