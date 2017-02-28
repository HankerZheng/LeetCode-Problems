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
    public List<Interval> merge(List<Interval> intervals) {
        List<Interval> ans = new ArrayList();
        if (intervals.size() == 0){
            return ans;
        }
        Collections.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval a, Interval b){
                int order1 = a.start - b.start;
                int order2 = a.end - b.end;
                return order1==0? order2: order1;
            }
        });
        int thisStart = intervals.get(0).start;
        int thisEnd = intervals.get(0).end;
        for (int i = 1; i < intervals.size(); i++){
            Interval thisInterval = intervals.get(i);
            if (thisInterval.start <= thisEnd){
                thisEnd = Math.max(thisEnd, thisInterval.end);
            }else{
                ans.add(new Interval(thisStart, thisEnd));
                thisStart = thisInterval.start;
                thisEnd = thisInterval.end;
            }
        }
        ans.add(new Interval(thisStart, thisEnd));
        return ans;
    }
}