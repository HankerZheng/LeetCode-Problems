# Given n points on a 2D plane, find the maximum number of points
# that lie on the same straight line.

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


# Rumtine: 88ms
# testcase: [], [[0,0]], [[0,0], [0,0]]
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def calculate_k(point1, point2):
            dx = point1.x - point2.x
            dy = point1.y - point2.y
            if dx == 0:
                return float('inf')
            return float(dy)/float(dx)
        def isSamePoint(point1, point2):
            return point1.x == point2.x and point1.y == point2.y
        # this problem is kind like hand shake problem
        # for each new point, shake hands with all the old one
        # so that we can traverse all the line
        maxcount = 0
        for i, new_point in enumerate(points):
            j = 0
            same_point = 1 # add 1 if there is a same point
            hashtable = {} # store the number of point that has the same k
            while j < i:
                this_point = points[j]
                if isSamePoint(this_point, new_point):
                    same_point += 1
                else:
                    k = calculate_k(new_point, this_point)
                    # because two points can form a line whatever
                    hashtable[k] = hashtable.get(k, 0) + 1
                j += 1 # always forget this in while-loop
            maxcount = max(maxcount, max([0]+hashtable.values())+same_point )
        return maxcount
