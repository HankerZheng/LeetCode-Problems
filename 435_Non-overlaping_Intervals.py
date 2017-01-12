# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note:
# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
# Example 1:
# Input: [ [1,2], [2,3], [3,4], [1,3] ]

# Output: 1

# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:
# Input: [ [1,2], [1,2], [1,2] ]

# Output: 2

# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:
# Input: [ [1,2], [2,3] ]

# Output: 0

# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
# Subscribe to see which companies asked this question

# Show Tags



# GREEDY SOLUTION: depend on the input intervals are sorted by .start
#       Once the interval[i] is overlap with the previous interval, there must be one interval need 
#       to be removed.
#       Our greedy strategy is to remove the interval with a larger end attribute.
#
#       For interval[i], we have already know the min removal to make the first (i-1) intervals
#       non-overlaping, thus, if interval[i].start is less than curEnd, there must be one overlaping.
#       we increment our `cnt` count by one and update `curEnd` with the smaller value.
# 
#       Greedy solution works because there would only be one interval coverint the same range.
#       Thus, we would always choose the shorter range to make the ans smaller.


# MY SOLUTION: depend on the input intervals are sorted by .start
#       dp[i] = (removals, endBound) - the number of removal and the endBound of that non-overlaping
#       For each interval, we could keep it in the area, or remove it.
#       If we remove it, then dp[i] = (dp[i-1][0] + 1, dp[i-1][0])
#       If we choose it, then dp[i] = best_choice(dp[k][0] + i - k - 1, intervals[i].end) for all k
#                                 and best_choice(i, intervals[i].end)
# 
#       Why I think this solution needs prove is that in the `best_choice` function, we greedily choose
#       the method make the `cnt` smaller. That is between (1, 4) and (2, 2), we choose (1, 4).



# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        # Greedy solution
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.end)
        cnt = 0
        end = intervals[0].end
        for inter in intervals[1:]:
            if inter.start < end:
                cnt += 1
                end = min(end, inter.end)
            else:
                end = inter.end
        return cnt



    def eraseOverlapIntervals_mySol(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        def better_choice(a, b):
            if a[0] < b[0]:
                return a
            elif a[0] > b[0]:
                return b
            elif a[1] < b[1]:
                return a
            elif a[1] > b[1]:
                return b
            else:
                return a
        if not intervals:
            return 0
        dp = [0 for _ in intervals]
        for i, inter in enumerate(intervals):
            # if only choose this interval
            tmp = (i, inter[1])
            if i == 0:
                dp[0] = tmp
                continue
            # if not choose this interval
            tmp = better_choice(tmp, (dp[i-1][0] + 1, dp[i-1][1]))
            k = i - 1
            while k >= 0 and dp[k][1] > inter[1]:
                k -= 1
            if k >= 0:
                tmp = better_choice((dp[k][0] + i - k - 1, inter[1]), tmp)
            dp[i] = tmp
        return dp[-1][0]
            
                
if __name__ == '__main__':
    sol = Solution()
    print sol.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])