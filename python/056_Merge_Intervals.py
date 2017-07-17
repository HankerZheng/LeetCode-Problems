# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Subscribe to see which companies asked this question

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return '%d, %d' % (self.start, self.end)
    __repr__ = __str__

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        
        res = []
        intervals.sort(key=lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end
        i = 1
        while i < len(intervals):
            if intervals[i].start > end:
                res.append(Interval(start,end))
                start = intervals[i].start
                end = intervals[i].end
            elif intervals[i].start <= end:
                end = max(end, intervals[i].end)
            i += 1
        res.append(Interval(start, end))
        return res
        
if __name__ == '__main__':
    sol = Solution()
    print sol.merge([Interval(1,4),Interval(2,5)])