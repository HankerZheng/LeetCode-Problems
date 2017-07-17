// Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

// You may assume that the intervals were initially sorted according to their start times.

// Example 1:
// Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

// Example 2:
// Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

// This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]

/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        int newStart = newInterval.start, newEnd = newInterval.end;
        List<Interval> mergedIntervals = new ArrayList<>();
        int index = 0;
        while(index < intervals.size() && intervals.get(index).end < newInterval.start){
            mergedIntervals.add(intervals.get(index++));
        }
        while(index < intervals.size() && isOverlaped(intervals.get(index), newInterval)){
            newStart = Math.min(newStart, intervals.get(index).start);
            newEnd = Math.max(newEnd, intervals.get(index).end);
            index++;
        }
        mergedIntervals.add(new Interval(newStart, newEnd));
        while(index < intervals.size()){
            mergedIntervals.add(intervals.get(index++));
        }
        return mergedIntervals;
    }
    
    public boolean isOverlaped(Interval a, Interval b){
        boolean overlapCon1 = b.start <= a.start && a.start <= b.end;
        boolean overlapCon2 = a.start <= b.start && b.start <= a.end;
        return overlapCon1 || overlapCon2;
    }
}