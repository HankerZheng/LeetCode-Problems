"""
https://leetcode.com/problems/the-skyline-problem/

A city's skyline is the outer contour of the silhouette
formed by all the buildings in that city when viewed from 
a distance. 

Now suppose you are given the locations and height of all the
buildings as shown on a cityscape photo (Figure A), write a program
to output the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet
of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the
left and right edge of the ith building, respectively, and Hi is its height.

It is guaranteed that 0 <= Li, Ri <= INT_MAX, 0 < Hi <= INT_MAX, and
Ri - Li > 0. You may assume all buildings are perfect rectangles
grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are
recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format
of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. 

A key point is the left endpoint of a horizontal line segment. 
Note that the last key point, where the rightmost building ends,
is merely used to mark the termination of the skyline, 
and always has zero height. 

Also, the ground in between any two adjacent buildings should be 
considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:
[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:
- The number of buildings in any input list is guaranteed to 
be in the range [0, 10000].

- The input list is already sorted in ascending order by the left x position Li.

- The output list must be sorted by the x position.

- There must be no consecutive horizontal lines of equal height in
the output skyline. 
For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable;
the three lines of height 5 should be merged into one in the final output 
as such: [...[2 3], [4 5], [12 7], ...]

"""


# Key Points: Abstract every building into 2 lines and store all the lines
#             into one list and sort them in x-axis value.
#
#             For the starter line,
#                 1) push the height into height max heap
#                 2) compare line-height with cur_h, if larger
#                    append new ans point
#             For the ending line,
#                 1) compare the line with cur_h, if equal to
#                    pop this height from heights, the highest line
#                    shorter than cur_h, append new ans point.
#                    if not equal to, push this height into popped
#
#             This method consider each building as 2 lines, ans traverse
#             every line from left to right.
#
# Time Complexity: 1) Traverse and create line-list: O(N)
#                  2) Sorted: O(NlogN)
#                  3) Heap operation for each line: O(NlogN)
#   Total is O(NlogN)
#
# Run time: 264 ms



from heapq import *
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        def line_compare(x,y):
            if x[0] != y[0]:
                return x[0] - y[0]
            elif x[2] != y[2]:
                return x[2] - y[2]
            elif x[2] == 0:
                return y[1] - x[1]
            elif x[2] == 1:
                return x[1] - y[1]
            else:
                return 0

        def pop_height(popped, heights):
            while len(popped) and heights[0] == popped[0]:
                heappop(heights)
                heappop(popped)

        if buildings is None:
            return None

        ans, heights, popped = [], [0], []
        lines = []
        for build in buildings:
            lines.append([build[0], build[2], 0])
            lines.append([build[1], build[2], 1])
        lines = sorted(lines, cmp=line_compare)
        cur_h = 0
        print lines
        for line in lines:
            if line[2] == 0:
                # this line is a start line
                heappush(heights, -line[1])
                if line[1] > cur_h:
                    ans.append([line[0], line[1]])
            else:
                # this line is an end line
                if line[1] == cur_h:
                    heappop(heights)
                    pop_height(popped, heights)
                    if -heights[0] < cur_h:
                        ans.append([line[0], -heights[0]])
                else:
                    heappush(popped, -line[1])
            pop_height(popped, heights)
            cur_h = -heights[0]
        return ans




if __name__ == "__main__":
    test = Solution()
    # res = test.getSkyline([ [2,9,10],[3,7,15],[5,12,12], [15,20,10], [19,24,8] ])
    # print res
    # res = test.getSkyline([ [2,9,10],[3,7,10],[5,12,10] ])
    # print res
    # res = test.getSkyline([])
    # print res
    # res = test.getSkyline([ [2,9,10] ])
    # print res
    # res = test.getSkyline([ [2,9,10],[3,7,2],[5,12,4] ])
    # print res
    # res = test.getSkyline([ [2,9,10],[9,10,2],[10,12,4] ])
    # print res
    res = test.getSkyline([[1,2,1],[1,2,2],[1,2,3]])
    print res
    # res = test.getSkyline([[1,2,1],[1,2,1],[1,2,1]])
    # print res